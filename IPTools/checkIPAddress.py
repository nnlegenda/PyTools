import json
import re
import tkinter as tk
import urllib.request

import pyperclip


def main():
    """
    从剪切板获取第一个IP地址, 查询并返回结果弹窗
    :return:
    """

    clipboardValue = pyperclip.paste()
    ipSearch = re.search("((?:(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d)\\.){3}(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d))",
                         clipboardValue)
    if ipSearch is None:
        root = tk.Tk()
        w = 300
        h = 350
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - h
        root.title("提示")
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root.resizable(0, 0)
        label = tk.Label(root, text="找不到合法IP")
        label.pack(side="top", fill="both", expand=True)
        button = tk.Button(root, text="OK", command=lambda: root.destroy())
        button.pack(side="bottom", fill="none", expand=True)
        root.mainloop()

    else:
        ipAddress = ipSearch.group()
        queryUrl = "http://ip-api.com/json/" + ipAddress + "?lang=zh-CN"
        result = urllib.request.urlopen(queryUrl)
        resultJson = json.load(result)

        root = tk.Tk()
        w = 300
        h = 350
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - h
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root.title("查询")
        root.resizable(0, 0)
        label = tk.Label(root, text=resultJson["query"])
        label.pack(side="top", fill="both", expand=True)
        label = tk.Label(root, text=resultJson["country"])
        label.pack(fill="both", expand=True)
        label = tk.Label(root, text=resultJson["regionName"])
        label.pack(fill="both", expand=True)
        label = tk.Label(root, text=resultJson["city"])
        label.pack(fill="both", expand=True)
        label = tk.Label(root, text=resultJson["isp"])
        label.pack(fill="both", expand=True)
        button = tk.Button(root, text="OK", command=lambda: root.destroy())
        button.pack(side="bottom", fill="none", expand=True)
        root.mainloop()


main()
