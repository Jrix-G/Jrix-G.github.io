from tkinter import *
import time

fenetre = Tk()
fenetre.config(background="#3d423c")
fenetre.title("Calcul Mental")
fenetre.minsize(1400, 700)
fenetre.maxsize(1400, 700)



main_title = Label(fenetre, text="Effectuer l'opération", background="#3d423c", foreground="white", font=("Roboto", 15))
main_title.place(x=620, y=100)

title_select = Label(fenetre, text="De la table: ", background="#3d423c", foreground="white", font=("Roboto", 10))
title_select.place(x=10, y=20)
se = Spinbox(fenetre, from_ = 1, to = 30, width=3)
se.place(x=80, y=22)

title_select2 = Label(fenetre, text="à:  ", background="#3d423c", foreground="white", font=("Roboto", 10))
title_select2.place(x=64, y=40)
se2 = Spinbox(fenetre, from_ = 2, to = 30, width=3)
se2.place(x=80, y=42)

def Run():
    global run
    fenetre.after(100, Run)
    print("Ok")

fenetre.after(1, Run)

mainloop()