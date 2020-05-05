import tkinter as tk

root = tk.Tk()
m1 = tk.PanedWindow(showhandle=True,sashrelief=tk.SUNKEN)
m1.pack(fill=tk.BOTH, expand=1)

left = tk.Label(m1, text="left pane")
m1.add(left)

m2 = tk.PanedWindow(orient=tk.VERTICAL,showhandle=True,sashrelief=tk.SUNKEN)
m1.add(m2)
top = tk.Label(m2, text="top pane")
bottom = tk.Label(m2, text="bottom pane")
m2.add(top)
m2.add(bottom)

root.mainloop()
