import tkinter as tk
root = tk.Tk()


def callback(e):
    print(e.x, e.y)


def callback1(e):
    print(e.char)
    print(e.keysym)
    print(e.keycode)


frame = tk.Frame(root, width=200, height=200)
frame.bind("<Motion>", callback)
frame.bind("<Key>", callback1)
frame.focus_set()
frame.pack()

root.mainloop()
