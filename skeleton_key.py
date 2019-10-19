"""
百度云万能钥匙
"""
import tkinter as tk
import requests
from builtins import print
from tkinter import ttk
import json

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"
}
prefix = "BDY-"
url = "https://ypsuperkey.meek.com.cn/api/v1/item/check-data"
e = None
treeview = None


def do_decode():
    decode = e.get()
    uuids = decode.replace("https://pan.baidu.com/s/1", prefix)
    text = requests.post(headers=header, data={
        "client_version": "2019.2",
        "uuids": uuids
    }, url=url).text
    jsons = json.loads(text)
    for temp in jsons:
        state = "INVALID"
        access_code = ""
        print(jsons[temp])
        for attribute in jsons[temp]:
            if attribute == "state":
                state = jsons[temp][attribute]
            if attribute == "access_code":
                access_code = jsons[temp][attribute]

        treeview.insert("", 0, values=(state, temp, access_code))


if __name__ == '__main__':
    win = tk.Tk()
    win.title("百度云万能秘钥")
    win.geometry("400x400")
    e = tk.Entry(win)
    e.insert(0, '请添加要解码的百度云链接，多条链接请以,分割')
    e.pack(fill=tk.X)

    button = tk.Button(win, text="解码", command=do_decode, width=300, height=1)
    button.pack(ipadx=5, ipady=5)
    columns = ("state", "url", "code")
    treeview = ttk.Treeview(win, show="headings", columns=columns)  # 表格

    treeview.column("state", width=100, anchor='center')
    treeview.column("url", width=200, anchor='center')
    treeview.column("code", width=100, anchor='center')

    treeview.heading("state", text="state")  # 显示表头
    treeview.heading("url", text="url")
    treeview.heading("code", text="code")

    treeview.pack()
    win.mainloop()
