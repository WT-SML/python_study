import requests
import hashlib
import time
import random
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('自动翻译@wutong-有道云接口-只用于学习')
# 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
width = 1010
height = 280
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height,
                            (screenwidth-width)/2, (screenheight-height)/2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

_input = tk.Text(root, width=70, height=15)
_input.grid(row=0, column=0, padx=5, pady=10)
_output = tk.Text(root, width=70, height=15)
_output.grid(row=0, column=1, padx=5, pady=10)


def gettrans(_input):
    if _input == '':
        messagebox.showinfo('提示', '输入内容为空，请在左侧输入框输入需要翻译的内容')
        return _input
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {
        'i': _input.replace('\n', '').replace('\r', ''),
        'salt': str(int(time.time()*1000) + random.randint(1, 10)),
        'sign': hashlib.md5(('fanyideskweb' + _input + str(int(time.time()*1000) + random.randint(1, 10)) + 'rY0D^0\'nM0}g5Mm1z%1G4').encode('utf-8')).hexdigest(),
        'doctype': 'json',
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
    }
    res = requests.post(url, data, headers=headers)
    trans = ''
    for item in res.json()['translateResult'][0]:
        trans += item['tgt']
    return trans


def handle_gettrans_click():
    _output.delete(1.0, tk.END)
    _output.insert(tk.INSERT, gettrans(str.strip(_input.get(0.0, tk.END))))


btn = tk.Button(root, text='自动翻译', command=handle_gettrans_click)
btn.grid(row=1, column=0, columnspan=2, pady=10)


root.mainloop()
