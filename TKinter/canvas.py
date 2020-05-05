import tkinter as tk

root = tk.Tk()

w=tk.Canvas(root,width=400,height=200)
w.pack()

def draw(e):
  x1,y1,=(e.x-1),(e.y-1)
  x2,y2,=(e.x+1),(e.y+1)
  w.create_oval(x1,y1,x2,y2,fill="red")
w.bind("<B1-Motion>",draw)

tk.Label(root,text='拖动鼠标，开始绘图~').pack()
root.mainloop()