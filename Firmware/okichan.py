import os
import sys
import time
import threading
import subprocess
import webview

# Attempt to load native Linux I/O drivers
try:
    import gpiod
    HARDWARE_AVAILABLE = True
except ImportError:
    HARDWARE_AVAILABLE = False
    print("[WARN] gpiod library missing. Initializing in desktop emulation mode.")

# ==========================================
# HARDWARE CORE PIN CONFIGURATION
# ==========================================
GPIO_CHIP_NAME = "gpiochip4"
PIN_BUTTON_1 = 10   # Cycle App Pages
PIN_BUTTON_2 = 11   # Trigger Buzzer Pulse
PIN_BUTTON_3 = 12   # System Volume Up
PIN_BUTTON_4 = 13   # System Volume Down
PIN_LIGHT_IN = 14   # Digital Input from Photoresistor Module
PIN_BUZZER_OUT = 15 # Digital Output to Piezo Buzzer

SOUND_FILE_PATH = "/usr/share/sounds/alsa/Front_Center.wav"

class WebAppHardwareBridge:
    """API Object exposed directly to JavaScript inside the WebView window container."""
    def __init__(self):
        self.window = None
        self.volume_level = 70
        self.running = True
        self.init_gpio_lines()

    def init_gpio_lines(self):
        if not HARDWARE_AVAILABLE:
            return
        try:
            self.chip = gpiod.Chip(GPIO_CHIP_NAME)
            
            # Map out hardware inputs with active-low safety bounds
            self.btn1 = self.chip.get_line(PIN_BUTTON_1); self.btn1.request(consumer="WebHub", type=gpiod.LINE_REQ_DIR_IN)
            self.btn2 = self.chip.get_line(PIN_BUTTON_2); self.btn2.request(consumer="WebHub", type=gpiod.LINE_REQ_DIR_IN)
            self.btn3 = self.chip.get_line(PIN_BUTTON_3); self.btn3.request(consumer="WebHub", type=gpiod.LINE_REQ_DIR_IN)
            self.btn4 = self.chip.get_line(PIN_BUTTON_4); self.btn4.request(consumer="WebHub", type=gpiod.LINE_REQ_DIR_IN)
            self.light_sensor = self.chip.get_line(PIN_LIGHT_IN); self.light_sensor.request(consumer="WebHub", type=gpiod.LINE_REQ_DIR_IN)
            
            # Map out output lines
            self.buzzer = self.chip.get_line(PIN_BUZZER_OUT); self.buzzer.request(consumer="WebHub", type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])
        except Exception as err:
            print(f"[GPIO Initialization Failure]: {err}")

    # --- Methods triggered directly from user interface clicks inside the Web UI ---
    def play_audio_alert(self):
        """Fired when UI Audio buttons are clicked."""
        if os.path.exists(SOUND_FILE_PATH):
            subprocess.run(["aplay", SOUND_FILE_PATH], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return {"status": "success"}

    def pulse_hardware_buzzer(self):
        """Fired when UI Test Buzzer buttons are clicked."""
        def run_pulse():
            if HARDWARE_AVAILABLE:
                self.buzzer.set_value(1)
                time.sleep(0.15)
                self.buzzer.set_value(0)
            else:
                print("[EMULATION] *Buzzer Beep*")
        threading.Thread(target=run_pulse, daemon=True).start()
        return {"status": "activated"}

    def change_system_volume(self, target_direction):
        if target_direction == "up" and self.volume_level < 100:
            self.volume_level += 5
        elif target_direction == "down" and self.volume_level > 0:
            self.volume_level -= 5
        subprocess.run(["amixer", "sset", "Master", f"{self.volume_level}%"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return self.volume_level

    # --- Background Loop pushing data back into the Web DOM ---
    def start_hardware_polling(self):
        """Monitors input lines and executes javascript strings inside the runtime window context."""
        current_page_idx = 0
        pages_list = ["page-main-hub", "page-alarms", "page-tasks"]
        dht_ticks = 0

        while self.running:
            if HARDWARE_AVAILABLE:
                try:
                    # 1. Hardware Buttons mapped directly to Application Navigation Events
                    if self.btn1.get_value() == 0:  # Page Cycle Switch Button
                        current_page_idx = (current_page_idx + 1) % len(pages_list)
                        self.window.evaluate_js(f"switchPage('{pages_list[current_page_idx]}')")
                        time.sleep(0.3)

                    if self.btn2.get_value() == 0:  # Physical Trigger for the Buzzer
                        self.pulse_hardware_buzzer()
                        time.sleep(0.3)

                    if self.btn3.get_value() == 0:  # Volume Up Pin
                        self.change_system_volume("up")
                        time.sleep(0.15)

                    if self.btn4.get_value() == 0:  # Volume Down Pin
                        self.change_system_volume("down")
                        time.sleep(0.15)

                    # 2. Update Webpage UI based on Photoresistor state
                    # Automatically dismisses screensaver overlay if light status changes significantly
                    if self.light_sensor.get_value() == 0:
                        self.window.evaluate_js("userActivityRegistered();")

                    # 3. Read Temp/Humidity Data from SysFS nodes into Web Screensaver View
                    dht_ticks += 1
                    if dht_ticks >= 20: # Query hardware roughly every 2 seconds
                        temp_path = "/sys/bus/iio/devices/iio:device0/in_temp_input"
                        if os.path.exists(temp_path):
                            with open(temp_path, "r") as f:
                                current_temp = float(f.read().strip()) / 1000.0
                            # Dynamically modifies the target text node within the screensaver stack layout
                            js_update = f"document.querySelector('#idle-screensaver .saver-widget-row span').textContent = '{current_temp:.1f}°C';"
                            self.window.evaluate_js(js_update)
                        dht_ticks = 0

                except Exception as loop_error:
                    print(f"Polling loop hiccup: {loop_error}")

            time.sleep(0.1)

    def cleanup(self):
        self.running = False
        if HARDWARE_AVAILABLE:
            try:
                for line in [self.btn1, self.btn2, self.btn3, self.btn4, self.light_sensor, self.buzzer]:
                    line.release()
            except:
                pass

if __name__ == "__main__":
    bridge = AppHardwareBridge()
    
    # Establish full view window matching your 7-inch display dimensions
    window = webview.create_window(
        title="Smart Task Multi-Hub",
        url="Oki-chan Webui.html",
        js_api=bridge,
        fullscreen=True, # Launches app borderless covering window environment elements
        background_color="#0c0f12"
    )
    
    bridge.window = window
    
    # Fire off background hardware monitor loop right as the Web View engine stabilizes
    window.events.loaded += lambda: threading.Thread(target=bridge.start_hardware_polling, daemon=True).start()
    
    webview.start()
    bridge.cleanup()
