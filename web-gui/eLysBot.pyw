#!/bin/pyw
from cProfile import label
from cgitb import text
from multiprocessing import connection
#from tkhtmlview import HTMLLabel
import webbrowser
from tkinter import *

def open_buy_license():
    webbrowser.open_new("https://aex03.sellix.io/")
    

# Premiere fenetre (windows)
windows = Tk()

# Personnaliser la fenetre (windows)
windows.geometry("1781x856")
windows.title("eLys BotNet")
windows["bg"] = "#0D1117"
windows.iconbitmap("eLysCi.ico")

# Text fenetre (windows)
picture = PhotoImage(file="eLysC2.png")
label_biglogo = Label(windows, image=picture)
label_biglogo.place(x="460", y="150")
label_biglogo.pack(expand=YES)

# Button Connection (windows)
connection_button = Button(text="Connection", font=(
    "Courrier", 25), bg='#0D1117', fg='#5F4944')
connection_button.place(x="800",y="680")
connection_button.pack(expand=YES)

#label_HTML = HTMLLabel(windows, html=""" code here """)
#label_HTML.pack(pady=20, padx=20)

# Afficher la boucle fenetre (windows)
windows.mainloop()
