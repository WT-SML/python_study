import tkinter as tk

root = tk.Tk()

# # pack
# listbox = tk.Listbox(root)
# listbox.pack(fill=tk.BOTH, expand=True)

# for i in range(10):
#   listbox.insert(tk.END,str(i))

# tk.Label(root,text='red',bg='red',fg='white').pack(fill=tk.X)
# tk.Label(root,text='green',bg='green',fg='white').pack(fill=tk.X)
# tk.Label(root,text='blue',bg='blue',fg='white').pack(fill=tk.X)
# tk.Label(root,text='red',bg='red',fg='white').pack(side=tk.LEFT)
# tk.Label(root,text='green',bg='green',fg='white').pack(side=tk.LEFT)
# tk.Label(root,text='blue',bg='blue',fg='white').pack(side=tk.LEFT)

# grid

tk.Label(root, text='用户名').grid(row=0, sticky=tk.W)
tk.Label(root, text='密码').grid(row=1, sticky=tk.W)

tk.Entry(root).grid(row=0, column=1)
tk.Entry(root, show='*').grid(row=1, column=1)

tk.Button(text='登录').grid(row=3,column=0,columnspan=3,pady=5)
# # 绝对中心
# def callback():
#   print('正中靶心')
# tk.Button(text='点我',command=callback).place(relx=0.5,rely=0.5,anchor=tk.CENTER)

root.mainloop()
