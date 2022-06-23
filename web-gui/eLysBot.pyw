#!/bin/pyw
from statistics import geometric_mean
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from cProfile import label
from cgitb import text
from doctest import master
from multiprocessing import connection
#from tkhtmlview import HTMLLabel
import webbrowser


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

# Deuxième personnalisation fenetre (windows2)
def openwindows2():
    windows2 = Toplevel(windows)
    windows2.geometry("1781x856")
    windows2.title("eLys BotNet")
    windows2["bg"] = "#0D1117"
    windows2.iconbitmap("eLysCi.ico")

    # Deuxième fenetre tab
    notebook = ttk.Notebook(windows2)
    tab1 = Frame(notebook)
    tab2 = Frame(notebook)
    tab3 = Frame(notebook)
    tab4 = Frame(notebook)
    tab5 = Frame(notebook)
    tab6 = Frame(notebook)

    notebook.add(tab1, text="Map & Panel")
    notebook.add(tab2, text="Build Bot")
    notebook.add(tab3, text="Remote Access")
    notebook.add(tab4, text="Terminal")
    notebook.add(tab5, text="Scanner")
    notebook.add(tab6, text="Face Mapper")
    notebook.pack()

    label(tab1, text="test", width=50,height=25).pack()
    label(tab2, text="test", width=50,height=25).pack()
    label(tab3, text="test", width=50,height=25).pack()
    label(tab4, text="test", width=50,height=25).pack()
    label(tab5, text="test", width=50,height=25).pack()
    label(tab6, text="test", width=50,height=25).pack()

# Button Connection (windows)
connection_button = Button(windows, text="Connection", command=openwindows2)
connection_button.place(x="800",y="680")
connection_button.pack(expand=YES)


#label_HTML = HTMLLabel(windows, html=""" code here """)
#label_HTML.pack(pady=20, padx=20)

# Afficher la boucle fenetre (windows)
windows.mainloop()
