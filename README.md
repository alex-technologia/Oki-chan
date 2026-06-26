<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=250&text=Oki-chan&fontSize=70&fontAlign=50&fontAlignY=40&color=gradient" />
</p>

<table>
<tr>
<td width="40%">

<img width="520" height="695" alt="Untitled(22)" src="https://github.com/user-attachments/assets/e1430b2a-f67f-4d0d-8791-9740b5bb4019" />

</td>

<td width="60%">

<h3>Oki-chan (Okiru = wake up / Ooki = big)</h3>

A digital interactive customizable alarm clock with a touch screen. Normal alarm clocks are boring—animate whatever you want and put it on the display. I'm probably going to use an anime character, but it's completely customizable on the software side.

This alarm clock runs Linux/Android, so you can run almost anything you want on it—even Doom.

We created software that functions as both an alarm clock and a character display. The default character is
<img width="25" height="25" alt="giphy" src="https://github.com/user-attachments/assets/df07eccb-a773-40a9-ace7-93a759818156" />,
but you can replace it with whoever you like. (work in progress)

We made this project to prove that waking up doesn't have to be frustrating or painful while still giving users complete freedom to customize their experience. ps. I hate waking up so I'm trying to make waking up fun!

It is super simple to use, just install the android firmware from radxa's official website and you're ready to go! It's touchscreen so u can use it like any mobile gadget but in the form of an alarm clock.

</td>
</tr>
</table>

## Onshape link 
https://cad.onshape.com/documents/88c036c3c5f450a3cafc0f79/w/50fab2545bc89d9e2dabb88b/e/1d1f4fe3c64da217baa0164f?renderMode=0&uiState=6a3d236724a01d036d5c05a1

## 3D Model

<table>
  <tr>
    <img width="311" height="283" alt="image" src="https://github.com/user-attachments/assets/ceacdf5c-3ade-44a3-9434-927a9415a644" />
</td>
    <td><img width="347" height="305" alt="image" src="https://github.com/user-attachments/assets/064f41d8-812a-4ffa-99af-9cd9be51316c" />

</td>
  </tr>
  <tr>
    <td><img width="316" height="287" alt="image" src="https://github.com/user-attachments/assets/ee6c53c0-5b13-46f5-bdb2-bc6c417877fd" />

</td>
    <td><img width="249" height="203" alt="image" src="https://github.com/user-attachments/assets/ee5f1b04-baad-436b-9e16-20d13a111dd0" />

</td>
  </tr>
</table>

### Wiring Diagram
<img width="600" height="500" alt="Wiring schematic" src="https://github.com/user-attachments/assets/2c343380-a818-4350-8475-bc1a51762744" />


🟥RED = +wire
⬛BLACK = -wire
🟩GREEN = Data wire
🟧ORANGE = Audio+/-
🟨YELLOW = AUX Wire

## BOM
<img width="610" height="334" alt="image" src="https://github.com/user-attachments/assets/cdfd3e86-47aa-411b-b1d1-43a0bb3caf78" />



## Flashing Firmware
Android
Compatible with microSD cards, eMMC modules, and UFS modules.


<table>
  <tr>
    <td colspan="2">

## 1. Download Firmware

### Radxa Cubie A7A Android 13 Images

[Radxa Cubie A7A Android 13 **20250814**](https://github.com/radxa/allwinner-android-manifests/releases/download/A733-Android13-20250814/a733_android13_radxa_a7a_20250814_uart0.zip): for Cubie A7A with **AC101** audio codec

[Radxa Cubie A7A Android 13 **20260206**](https://github.com/radxa/allwinner-android-manifests/releases/download/A733-Android13-20260205/a733_android13_radxa_a7a_20260206_uart0.zip): for Cubie A7A with **AC101B** audio codec

  </tr>

  <tr>
    <td width="50%" valign="top">

## 2A. SD Card Flashing

### SD Card Boot Disk Creation Tool

- [PhoenixCard V4.3.2](https://dl.radxa.com/tools/windows/PhoenixCard_V4.3.2_20250331_1604_Release.zip)

1. Insert SD card into PC.
2. Open PhoenixCard.
3. Select the firmware image from Step 1.
4. Create the bootable SD card.
5. Insert SD card into the Radxa A7A and power on.

    </td>

    <td width="50%" valign="top">

## 2B. USB Flashing

### System Flashing Tools

- [PhoenixSuit](https://dl.radxa.com/tools/windows/PhoenixSuit_V2.0.4.zip) (Windows)
- [LiveSuit](https://dl.radxa.com/tools/linux/LiveSuit_Linux_V3.0.8.zip) (Linux)

1. Unplug power and USB cables from the Radxa A7A.
2. Press and hold the **UBOOT** button.
3. Connect the Radxa A7A to the PC using a USB cable.
4. Release the **UBOOT** button.
5. Open Device Manager and verify the board appears under USB Devices.
6. Open PhoenixSuit/LiveSuit and select the firmware image from Step 1.
7. Choose **Full Flash**.
8. Wait until **"Firmware flashed successfully"** is displayed.
9. The board is now ready to use.
  </tr>
</table>

Official Radxa A7a Android Docs [HERE](https://docs.radxa.com/en/cubie/a7a/other-system/android) 

(Debian&Tina not used in this project), it's available by following [Radxa official docs](https://docs.radxa.com/en/cubie/a7a/download) if you want.

## **Apps**
Oki-chan is not limited by our app, thus you can use any other app you want that is android (side-loading required).

As for our app, it will be running as [Oki-chan Webui.html]() file and is still in devolopment. 

## Preview
What could be possible (we haven't made the software for it yet)  

https://github.com/user-attachments/assets/e6b8e22e-ab00-47f7-8dbc-2a04c18cb579

## Zine 
<img width="520" height="695" alt="Untitled(22)" src="https://github.com/user-attachments/assets/96ec45f2-47ee-4ed7-88e7-776ec1f687fc" />



