import tkinter as tk
import random

def dispLabel():
    messages=["こんにちは","さようなら","またね","ようこそ"]
    lbl.configure(text=random.choice(messages))

root=tk.Tk()
root.geometry("150x75")

lbl=tk.Label(text="LABEL")
btn=tk.Button(text="プッシュ",command=dispLabel)

lbl.pack()
btn.pack()
tk.mainloop()

