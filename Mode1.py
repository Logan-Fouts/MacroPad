from adafruit_hid.keycode import Keycode
def getKeys0():
    keymap = {
    (0): ((Keycode.LEFT_ALT, Keycode.F6)),
    (1): (Keycode.LEFT_ALT, Keycode.F5),
    (2): (Keycode.GUI, Keycode.TAB),
    (3): (Keycode.LEFT_ALT, Keycode.F12),
    (4): ([Keycode.KEYPAD_FIVE]),
    (5): ([Keycode.KEYPAD_TWO]),
    (6): (Keycode.LEFT_ALT, Keycode.G),
    (7): (Keycode.LEFT_ALT, Keycode.F4),
    (8): ([Keycode.LEFT_ALT, Keycode.F2]),
    (9): (Keycode.LEFT_CONTROL, Keycode.K),
    (10): (Keycode.LEFT_CONTROL, Keycode.D),
    (11): (Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.P)
}
    return keymap