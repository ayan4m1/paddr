# Paddr

Paddr is a DIY numpad built using [KMK](https://github.com/KMKfw/kmk_firmware).

## Schematic

![schematic](./hardware/schematic.png)

## Board

![board](./hardware/board.png)

## PCB

[OSH Park](https://oshpark.com/shared_projects/GSJlJusC)

## BOM

| Vendor    | Part                                                                                                           | Quantity |
| --------- | -------------------------------------------------------------------------------------------------------------- | -------- |
| onsemi    | [1N4148 Diode](https://www.mouser.com/ProductDetail/onsemi-Fairchild/1N4148?qs=i4Fj9T%2FoRm8RMUhj5DeFQg%3D%3D) | 17       |
| Kailh     | [Hotswap Sockets](https://shop.keyboard.io/products/kailh-hotswap-sockets-for-mx-style-keyswitches-x-25)       | 17       |
| Adafruit  | [KB2040](https://www.adafruit.com/product/5302)                                                                | 1        |
| Worldsemi | [WS2812B](https://www.adafruit.com/product/1655)                                                               | 4        |

## Firmware

Copy all files from the firmware directory to the root of the CIRCUITPY drive. The keymap lives in code.py.

After you install the firmware, the CIRCUITPY drive and USB serial port will be hidden on subsequent restarts of the numpad. To override this behavior, hold down the dash key while plugging the numpad in.
