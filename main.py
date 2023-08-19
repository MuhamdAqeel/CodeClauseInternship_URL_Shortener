import pyshorteners
from tkinter import *

win=Tk()
win.geometry("400x300")
win.configure(bg="Yellow")
def short():
    url=entry1.get()
    s=pyshorteners.Shortener().tinyurl.short(url)
    entry2.insert(END, s)
Label(win, text="Enter Your url link", font="impack 17 bold", bg="light blue", fg="black").pack(fill=X)
entry1=Entry(win, font="10", bd=3,width=30)
entry1.pack(pady=30)
Button(win, text="Shorten", font="impack 12 bold", bg="light green", fg="black", width=14, command=short).pack()
entry2=Entry(win, font="impack 16 bold", bg="light pink", width=24)
entry2.pack(pady=30)
mainloop()