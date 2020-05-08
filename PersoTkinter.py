# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from tkinter import *
import sqlite3 as sq
########Kantbra mn ay crise tqder tjik laqrity hdxi Cordialement
#Tkinter
conn=sq.connect('Study.db')
cur=conn.cursor()
cur.execute("""  CREATE TABLE IF NOT EXISTS Student(
                NP TEXT,
                Note INT,
                Redoublant TEXT,
                Appreciation TEXT
                )""")
cur.close()
conn.commit()
conn.close()
window = Tk()
window.title("Gestion Des Notes!")
#functions
def Ajout():
    conn=sq.connect('Study.db')
    cur=conn.cursor()
    cur.execute("INSERT INTO Student VALUES (:NP, :Note, :Redoublant, :Appreciation)",
                {   
                    'NP': NomPrenom.get(),
                    'Note': Notes.get(),
                    'Redoublant': selected.get(),
                    'Appreciation': Apprec.get()
                    
                })
    cur.close()
    conn.commit()
    conn.close()
    messagebox.showinfo('Nouvel ajout', 'Ajout avec succes!')
    NomPrenom.delete(0,END)
    Notes.delete(0,END)
    selected.delete(0,END)
    Apprec.delete(0,END)
	
def Liste():
    conn=sq.connect('Study.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM Student")
    list=cur.fetchall()
    aff=''
    for l in list:
        aff+=str(l)+"\n"
    cur.close()
    conn.commit()
    conn.close()
    txt = Tk()
    txt.title("FetchingData!")
    text=Text(txt, height=20, width=30)
    text.grid(column=1, row=1)

def Modify():
	print('Modify')

def Delete():
    #conn=sq.connect('Study.db')
    #cur=conn.cursor()
    #cur.execute("DELETE FROM Student WHERE")
    #cur.close()
    #conn.commit()
    #conn.close()
    print('deleted')

NomPrenom=StringVar()
Notes=IntVar()
selected = StringVar()
Apprec=StringVar()
lbl1 = Label(window, text="Nom ET Prénom: ")
lbl1.grid(column=0, row=0)
txt1 = Entry(window,textvariable=NomPrenom, width=10)
txt1.grid(column=1, row=0)
lbl2 = Label(window, text="Notes: ")
lbl2.grid(column=0, row=1)
txt2 = Entry(window, width=10)
txt2.grid(column=1, row=1)
lbl3 = Label(window, text="Redoublant: ")
lbl3.grid(column=0, row=2)
rad1 = Radiobutton(window,text='Oui', value='Oui', variable=selected)
rad1.grid(column=1, row=2)
rad2 = Radiobutton(window,text='Non', value='Non', variable=selected)
rad2.grid(column=2, row=2)
lbl4 = Label(window, text="Appréciation: ")
lbl4.grid(column=0, row=3)
txt3 = Entry(window,textvariable=Apprec, width=10)
txt3.grid(column=1, row=3)
btn1 = Button(window, text="Listes Des Notes", command=Liste())
btn1.grid(column=1, row=4)
btn2 = Button(window, text="Ajouter", command=Ajout)
btn2.grid(column=2, row=4)
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='Modifier_Note', command=Modify)
new_item.add_separator()
new_item.add_command(label='Supprimer_eleve', command=Delete)
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)
window.mainloop()

