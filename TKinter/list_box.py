import tkinter as tk

root = tk.Tk()

tk.Listbox(root).grid()
tk.Entry().grid()
tk.Button(master=root,text='获取翻译').grid()


root.mainloop()