import tkinter as tk
# 顶级窗口
root = tk.Tk()


def create():
    top = tk.Toplevel()
    top.attributes("-alpha", 0.5)  # 透明度
    top.title('wutong')
    msg = tk.Message(top, text='wutong sumoli')
    msg.pack()


tk.Button(root, text="创建顶级窗口", command=create).pack()

root.mainloop()
