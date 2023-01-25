import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from Mode1 import getKeys0
from Mode2 import getKeys1

kbd = Keyboard(usb_hid.devices)

button0 = digitalio.DigitalInOut(board.GP0)
button0.direction = digitalio.Direction.INPUT
button0.pull = digitalio.Pull.DOWN

button1 = digitalio.DigitalInOut(board.GP3)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.DOWN

button2 = digitalio.DigitalInOut(board.GP28)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.DOWN

button3 = digitalio.DigitalInOut(board.GP22)
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.DOWN

button4 = digitalio.DigitalInOut(board.GP1)
button4.direction = digitalio.Direction.INPUT
button4.pull = digitalio.Pull.DOWN

button5 = digitalio.DigitalInOut(board.GP4)
button5.direction = digitalio.Direction.INPUT
button5.pull = digitalio.Pull.DOWN

button6 = digitalio.DigitalInOut(board.GP27)
button6.direction = digitalio.Direction.INPUT
button6.pull = digitalio.Pull.DOWN

button7 = digitalio.DigitalInOut(board.GP21)
button7.direction = digitalio.Direction.INPUT
button7.pull = digitalio.Pull.DOWN

button8 = digitalio.DigitalInOut(board.GP2)
button8.direction = digitalio.Direction.INPUT
button8.pull = digitalio.Pull.DOWN

button9 = digitalio.DigitalInOut(board.GP5)
button9.direction = digitalio.Direction.INPUT
button9.pull = digitalio.Pull.DOWN

button10 = digitalio.DigitalInOut(board.GP26)
button10.direction = digitalio.Direction.INPUT
button10.pull = digitalio.Pull.DOWN

button11 = digitalio.DigitalInOut(board.GP20)
button11.direction = digitalio.Direction.INPUT
button11.pull = digitalio.Pull.DOWN

mode = 0

keymap0 = getKeys0()
keymap1 = getKeys1()

while True:
    if mode == 0:
        if button0.value:
            kbd.send(*keymap0[0])
        if button1.value:
            kbd.send(*keymap0[1])
        if button2.value:
            kbd.send(*keymap0[2])
        if button3.value:
            kbd.send(*keymap0[3])
        if button4.value:
            kbd.send(*keymap0[4])
        if button5.value:
            kbd.send(*keymap0[5])
        if button6.value:
            kbd.send(*keymap0[6])
        if button7.value:
            kbd.send(*keymap0[7])
        if button8.value:
            kbd.send(*keymap0[8])
        if button9.value:
            kbd.send(*keymap0[9])
        if button10.value:
            kbd.send(*keymap0[10])
        if button11.value:
            kbd.send(*keymap0[11])
        if button0.value and button3.value:
            time.sleep(2)
            if button0.value and button3.value:
                mode = 1
    if mode == 1:
        if button0.value:
            kbd.send(*keymap1[0])
        if button1.value:
            kbd.send(*keymap1[1])
        if button2.value:
            kbd.send(*keymap1[2])
        if button3.value:
            kbd.send(*keymap1[3])
        if button4.value:
            kbd.send(*keymap1[4])
        if button5.value:
            kbd.send(*keymap1[5])
        if button6.value:
            kbd.send(*keymap1[6])
        if button7.value:
            kbd.send(*keymap1[7])
        if button8.value:
            kbd.send(*keymap1[8])
        if button9.value:
            kbd.send(*keymap1[9])
        if button10.value:
            kbd.send(*keymap1[10])
        if button11.value:
            kbd.send(*keymap1[11])
        if button0.value and button3.value:
            time.sleep(2)
            if button0.value and button3.value:
                mode = 0
    time.sleep(0.1)
