import tkinter as tk

class App():

  def __init__(self,master):
    frame=tk.Frame(master)
    frame.pack()
    self.hi_there=tk.Button(frame,text='打招呼',fg='blue',command=self.say_hi)
    self.hi_there.pack()

  def say_hi(self):
    print('My name is wutong')

root=tk.Tk()
app= App(root)
root.mainloop()