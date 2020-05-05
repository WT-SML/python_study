import tkinter as tk

root = tk.Tk()


def callback():
    print(type(True))
    print(type(0))
    print('你好')


menu = tk.Menu(root)
menu1 = tk.Menu(menu, tearoff=0)
menu1.add_command(label='打开', command=callback)
menu1.add_command(label='保存', command=callback)
menu1.add_separator()
menu1.add_command(label='退出', command=root.quit)
menu.add_cascade(label='文件', menu=menu1)

menu2 = tk.Menu(menu, tearoff=0)
menu2.add_command(label='剪切', command=callback)
menu2.add_command(label='拷贝', command=callback)
menu2.add_command(label='粘贴', command=callback)
menu.add_cascade(label='编辑', menu=menu2)

check1 = tk.IntVar()
check2 = tk.IntVar()
check3 = tk.IntVar()
menu3 = tk.Menu(menu, tearoff=0)
menu3.add_checkbutton(label='多选1', variable=check1)
menu3.add_checkbutton(label='多选2', variable=check2)
menu3.add_checkbutton(label='多选3', variable=check3)
menu.add_cascade(label='多选', menu=menu3)

root.config(menu=menu)

root.mainloop()
