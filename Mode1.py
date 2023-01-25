from adafruit_hid.keycode import Keycode
def getKeys0():
    keymap = {
    (0): (Keycode.LEFT_ALT, Keycode.F6),
    (1): (Keycode.LEFT_ALT, Keycode.F12),
    (2): (Keycode.LEFT_ALT, Keycode.G),
    (3): (Keycode.LEFT_CONTROL, Keycode.K),
    (4): (Keycode.LEFT_ALT, Keycode.F5),
    (5): ([Keycode.A]),
    (6): (Keycode.LEFT_ALT, Keycode.F4),
    (7): ([Keycode.O]),
    (8): ([Keycode.LEFT_ALT, Keycode.F2]),
    (9): (Keycode.LEFT_CONTROL, Keycode.K),
    (10): (Keycode.LEFT_CONTROL, Keycode.D),
    (11): (Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.P)
}
    return keymap
