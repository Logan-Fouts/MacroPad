import tkinter as tk
import webbrowser

computer = "lfouts"
mode = 0

def read():
    f = open(f"/media/{computer}/CIRCUITPY/Mode1.py", "r")
    global content1
    content1 = f.readlines()
    f.close()

    f = open(f"/media/{computer}/CIRCUITPY/Mode2.py", "r")
    global content2
    content2 = f.readlines()
    f.close()

def handleclick(e):
    print(mode)
    if mode == 1:
        f = open(f"/media/{computer}/CIRCUITPY/Mode1.py", "w")
        code = "from adafruit_hid.keycode import Keycode\ndef getKeys0():\n    keymap = {\n"  
    else:
        f = open(f"/media/{computer}/CIRCUITPY/Mode2.py", "w")
        code = "from adafruit_hid.keycode import Keycode\ndef getKeys1():\n    keymap = {\n"  
    for i in range (12):
        code += "    " + entries[i].get()
    code += "}\n    return keymap"
    f.write(code)
    f.close()

def open_browser():
    webbrowser.open_new("https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html")

read()

window = tk.Tk()
window.title("Macro Pad Gui")

def handlemode():
    global mode
    global entries
    if mode == 0:
        print(mode)
        label = tk.Label(text="Profile: 0")
        label.grid(row=0, column=3)
        mode = 1
        k = 0
        entries = []
        for i in range(1, 4):
            window.columnconfigure(i, weight=1, minsize=75)
            window.rowconfigure(i, weight=1, minsize=50)

            for j in range(1, 5):
                frame = tk.Frame(
                    master=window,
                    relief=tk.RAISED,
                    borderwidth=1
                )
                frame.grid(row=i, column=j, padx=5, pady=5)
                entry = tk.Entry(master=frame, width=50)
                entry.insert(0, content1[3+k][4:100])
                entry.pack(padx=5, pady=5)
                entries.append(entry)
                k += 1
    elif mode == 1:
        k = 0
        print(mode)
        mode = 0
        entries = []
        label = tk.Label(text="Profile: 1")
        label.grid(row=0, column=3)
        for i in range(1, 4):
            window.columnconfigure(i, weight=1, minsize=75)
            window.rowconfigure(i, weight=1, minsize=50)

            for j in range(1, 5):
                frame = tk.Frame(
                    master=window,
                    relief=tk.RAISED,
                    borderwidth=1
                )
                frame.grid(row=i, column=j, padx=5, pady=5)
                entry = tk.Entry(master=frame, width=50)
                entry.insert(0, content2[3+k][4:100])
                entry.pack(padx=5, pady=5)
                entries.append(entry)
                k += 1
                

title1 = tk.Label(text="Key Binds")
title1.grid(row=0, column=2)

button = tk.Button(window, text="Open Help", command=open_browser)
button.grid(row=2, column=5)

button2 = tk.Button(text="Save", command=lambda: handleclick(entries))
button2.grid(row=0, column=5)

button3 = tk.Button(text="Switch Mode", command=lambda: handlemode())
button3.grid(row=1, column=5)

handlemode()

window.mainloop()
