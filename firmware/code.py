print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.extensions.RGB import RGB
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

keyboard.extensions.append(RGB(pixel_pin = board.MOSI, num_pixels = 4))
keyboard.modules.append(Layers())

keyboard.row_pins = (board.D2, board.D3, board.D4, board.D5, board.D6)
keyboard.col_pins = (board.D7, board.D8, board.D9, board.D10)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

RAISE_OR_0 = KC.TD(KC.KP_0, KC.MO(1))

keyboard.keymap = [
    [
        KC.NUMLOCK, KC.KP_SLASH, KC.KP_ASTERISK, KC.KP_MINUS,
        KC.KP_7, KC.KP_8, KC.KP_9, KC.KP_PLUS,
        KC.KP_4, KC.KP_5, KC.KP_6, KC.NO,
        KC.KP_1, KC.KP_2, KC.KP_3, KC.KP_ENTER,
        RAISE_OR_0, KC.KP_DOT, KC.NO, KC.NO
    ],
    [
        KC.RGB_MODE_PLAIN, KC.RGB_MODE_BREATHE, KC.RGB_MODE_RAINBOW, KC.RGB_MODE_SWIRL,
        KC.NO, KC.RGB_VAI, KC.NO, KC.NO,
        KC.RGB_HUI, KC.RGB_TOG, KC.RGB_HUD, KC.NO,
        KC.NO, KC.RGB_VAD, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO
    ]
]

keyboard.debug_enabled = False

if __name__ == '__main__':
    print("Executing")
    keyboard.go()
