from tkinter import *
from tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedTk
import webbrowser

# You will need to change the file to open location based on where your pico is

computer = "TODO"
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

window = ThemedTk(theme="default")
window.geometry("800x400")
window.title("Macro Pad Gui")

style = ttk.Style()
style.configure("My.TEntry", relief="sunken", borderwidth=2)
style.configure("My.Label", font=("TkDefaultFont", 10, "bold"))

def handlemode():
    global mode
    global entries
    if mode == 0:
        print(mode)
        label = ttk.Label(text="Profile: 0", style="My.Label")
        label.grid(row=0, column=3)
        mode = 1
        k = 0
        entries = []
        for i in range(1, 4):
            if i == 3:
                window.columnconfigure(4, weight=1, minsize=75)
                window.rowconfigure(4, weight=1, minsize=50)
            window.columnconfigure(i, weight=1, minsize=75)
            window.rowconfigure(i, weight=1, minsize=50)

            for j in range(1, 5):
                frame = ttk.Frame(
                    master=window
                )
                frame.grid(row=i, column=j, padx=5, pady=5)
                entry = ttk.Entry(master=frame, width=50, style="My.TEntry")
                entry.insert(0, content1[3+k][4:100])
                entry.pack(padx=5, pady=5)
                entries.append(entry)
                k += 1
    elif mode == 1:
        k = 0
        print(mode)
        mode = 0
        entries = []
        label = ttk.Label(text="Profile: 1", style="My.Label")
        label.grid(row=0, column=3)
        for i in range(1, 4):
            if i == 3:
                window.columnconfigure(4, weight=1, minsize=75)
                window.rowconfigure(4, weight=1, minsize=50)
            window.columnconfigure(i, weight=1, minsize=75)
            window.rowconfigure(i, weight=1, minsize=50)

            for j in range(1, 5):
                frame = tk.Frame(
                    master=window
                )
                frame.grid(row=i, column=j, padx=5, pady=5)
                entry = ttk.Entry(master=frame, width=50, style="My.TEntry")
                entry.insert(0, content2[3+k][4:100])
                entry.pack(padx=5, pady=5)
                entries.append(entry)
                k += 1
          
style = ttk.Style()
style.configure("My.TLabel", font=("TkDefaultFont", 20, "bold"))

      
title1 = ttk.Label(text="Key Binds", style="My.TLabel")
title1.grid(row=0, column=2)

button = ttk.Button(window, text="Open Help", command=open_browser, style="My.TButton")
button.grid(row=0, column=4)

button2 = ttk.Button(text="Save", command=lambda: handleclick(entries), style="My.TButton")
button2.grid(row=4, column=3)

button3 = ttk.Button(text="Switch Mode", command=lambda: handlemode(), style="My.TButton")
button3.grid(row=4, column=2)

handlemode()

window.mainloop()
