import tkinter as tk
import webview
import webbrowser

computer = "llixtop"

def handleclick(e):
    f = open(f"/media/{computer}/CIRCUITPY/Mode1.py", "w")
    code = "from adafruit_hid.keycode import Keycode\ndef getKeys0():\n    keymap = {\n"  
    for i in range (12):
        code += "    " + entries[i].get()
    code += "}\n    return keymap"
    print(code)
    f.write(code)
    f.close()

def open_browser():
    webbrowser.open_new("https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html")

window = tk.Tk()
window.title("Macro Pad Gui")
title1 = tk.Label(text="Key")
title1.grid(row=0, column=2)

title2 = tk.Label(text="Binds")
title2.grid(row=0, column=3)

button = tk.Button(window, text="Open Help", command=open_browser)
button.grid(row=0, column=4)

f = open(f"/media/{computer}/CIRCUITPY/Mode1.py", "r")
content1 = f.readlines()
f.close()

f = open(f"/media/{computer}/CIRCUITPY/Mode2.py", "r")
content2 = f.readlines()
f.close()

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
        button = tk.Button(master=frame, text=f"Update {k}", command=lambda: handleclick(entries))
        button.pack()
        k += 1

window.mainloop()
