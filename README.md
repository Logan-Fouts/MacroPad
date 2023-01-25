# **Pico Macro Pad** 
#### Logan Fouts
---
![alt text](image.jpg)
##### As a weekend project I decided to create a little macro pad using a Raspberry Pi Pico.
- I created a 3d model in [tinkerCAD](https://tinkercad.com) around a modified version of [this](https://www.thingiverse.com/thing:4781838) models keyswitch plate.
- Then I printed the model and handwired the circuit with some cherry mx browns I have laying around. 

[//]: # (Hello)
![alt text](image.jpg)
- Using [this](https://learn.adafruit.com/diy-pico-mechanical-keyboard-with-fritzing-circuitpython) guide as a template, I finished the python code that runs on the pico.
- Since I wanted to create some sort of simple GUI to control the keybinds I moved the dictonaries to there own seperate files to make them easier to edit.
- To create the GUI I used python with tkinter. The code essentially just overwrites whatever file it must in order to change the key binds [I know this is probably dumb, but it was my first idea so I went with it :)]
- To change profiles on the macro pad you just simply hold buttons 1 and 3 for two seconds then when your window super + tabs you know it worked. (I wanted to use the built in led instead but since Im using a Pico w I cant figure out how to control the led with circuit python)
> **_NOTE:_**  If you're using a normal pico you should be able to use the led. The Pico w's led it controled through the wifi module which I don't think is supported by circuitpython yet.
