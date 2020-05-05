from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser

root = Tk()


def cakkback():
    file_name = filedialog.askopenfilename(defaultextension='.py')
    print(file_name)


def cakkback2():
    flag = messagebox.askokcancel('提示', '是否完成？')
    print(flag)


def cakkback3():
    color = colorchooser.askcolor()
    print(color)


Button(root, text='打开文件', command=cakkback).grid()
Button(root, text='打开询问对话框', command=cakkback2).grid()
Button(root, text='打开颜色对话框', command=cakkback3).grid()

root.mainloop()
