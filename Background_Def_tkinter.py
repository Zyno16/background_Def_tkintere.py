from tools import *
from tkinter import *
frm =form("600x400")

label(frm,"hello").pack(pady=7)
button(frm,"ok").pack(pady=7)
textbox(frm).pack(pady=5)
checkbox(frm).pack(pady=5)
combobox(frm,["ahmed","amr"],True).pack()


Label(frm,text="name").pack()
Entry(frm).pack()
Button(frm,text="text").pack()
bgall(frm,"lightblue")
frm.mainloop()
