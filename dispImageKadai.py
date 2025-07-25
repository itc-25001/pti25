import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    newImage=(
            PIL.Image.open(path)
            .convert("L")
            .resize((300,300))
            .rotate(90)
            .transpose(PIL.Image.FLIP_LEFT_RIGHT)
    )
    imageData=PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image=imageData)
    imageLabel.image=imageData

def openFile():
    fpath=fd.askopenfilename()

    if fpath:
        dispPhoto(fpath)

root=tk.Tk()
root.geometry("400x350")

btn=tk.Button(text="ファイルを開く",command=openFile)
imageLabel=tk.Label()
btn.pack()
imageLabel.pack()
tk.mainloop()
