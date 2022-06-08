from cProfile import label
from cgitb import text
#from tkhtmlview import HTMLLabel
from tkinter import *

windows = Tk()
windows.geometry("1781x856")
windows.title("eLys BotNet")
windows["bg"] = "#0D1117"
windows.iconbitmap("eLysCi.ico")

picture = PhotoImage(file="eLysC2.png")
label = Label(windows, image=picture)
label.place(x="460", y="150")

#label_HTML = HTMLLabel(windows, html=""" code here """)
#label_HTML.pack(pady=20, padx=20)

windows.mainloop()