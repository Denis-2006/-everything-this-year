from tkinter import *

click = 0

def test(event):
    global click
    click += 1
    but["text"] = click

root = Tk()

but = Button(text = "Test")

but.pack()

but.bind("<Button-1>", test)

root.mainloop()
