# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import *
import sqlite3 as sq
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Tkinter
#DATABASE
conn=sq.connect('Study.db')
cur=conn.cursor()
cur.execute("""  CREATE TABLE IF NOT EXISTS Student(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NP TEXT,
                Note INT,
                Redoublant TEXT,
                Appreciation TEXT
                )""")
cur.close()
conn.commit()
#Window's ceation
window = Tk()
window.title("Gestion Des Notes!")
#functions
ide=0
def Ajout():
    conn=sq.connect('Study.db')
    cur=conn.cursor()
    if selected.get()==1:
        Redoubl="Oui"
    elif selected.get()==0:
        Redoubl="Non"
    txt=txt3.get("1.0", 'end-1c')
    cur.execute("INSERT INTO Student (NP, Note, Redoublant, Appreciation) VALUES (:NP, :Note, :Redoublant, :Appreciation)",
                {
                    'NP': NomPrenom.get(),
                    'Note': int(Notes.get()),
                    'Redoublant': Redoubl,
                    'Appreciation': txt

                })
    cur.close()
    conn.commit()
    messagebox.showinfo('Nouvel ajout', 'Ajout avec succes!')
    
def Liste():
    liste = Toplevel()
    liste.geometry('640x680')
    conn=sq.connect('Study.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM Student")
    list=cur.fetchall()
    height = len(list) +1
    width = 5
    b0 = Label(liste, text="ID")
    b0.grid(row=0, column=0,padx=10, pady=10)
    b1 = Label(liste, text="Nom Prenom")
    b1.grid(row=0, column=1,padx=10, pady=10)
    b2 = Label(liste, text="Note")
    b2.grid(row=0, column=2,padx=10, pady=10)
    b3 = Label(liste, text="Redoublant")
    b3.grid(row=0, column=3,padx=10, pady=10)
    b4 = Label(liste, text="Appreciation")
    b4.grid(row=0, column=4,padx=10, pady=10)
    for i in range(1,height): 
        for j in range(width): 
            b = Label(liste, text=list[i-1][j])
            b.grid(row=i, column=j,padx=10, pady=10)
    liste.columnconfigure(0, weight=1)
    liste.columnconfigure(1, weight=1)
    liste.columnconfigure(2, weight=1)
    liste.columnconfigure(3, weight=1)
    liste.columnconfigure(4, weight=1)
    cur.close()
    conn.commit()


def ModifyOut():
    def ModifyIn():
        idd = int(entry0.get())
        Nom = entry1.get()
        Notep=int(entry2.get())
        txt=texte.get("1.0", 'end-1c')
        if selected.get()==1:
            Redoubl="Oui"
        elif selected.get()==0:
            Redoubl="Non"
        x=0
        conn=sq.connect('Study.db')
        cur=conn.cursor()
        cur.execute("SELECT * FROM Student")
        list=cur.fetchall()
        for i in range(len(list)):
            if list[i][0]==idd:
                x=1
        if x==1:
            conn=sq.connect('Study.db')
            cur=conn.cursor()
            cur.execute("""UPDATE Student SET Note = :note ,Redoublant = :Redoublant,Appreciation= :Appreciation
                    WHERE NP = :nom And ID = :id""",
                 {'nom':Nom,'id':idd, 'note':Notep,'Redoublant':Redoubl, 'Appreciation':txt})
            conn.commit()
            conn.close()
            messagebox.showinfo('Modification', 'Modification avec succes!')
        else:
            messagebox.showinfo('Modification', 'Modification échoué..RéssayerSVP!')


    mod = Toplevel()
    mod.geometry('480x640+400+40')
    mod.title("Note's Modification")
    lb0= Label(mod,text="Identity:")
    lb0.grid(row=0,column=0,padx=10, pady=15)
    lb1 = Label(mod,text="Nom et Prénom :")
    lb1.grid(row=1,column=0,padx=10, pady=15)
    lb2 = Label(mod,text="Note :")
    lb2.grid(row=3,column=0,padx=10, pady=15)
    lb3 = Label(mod,text="Redoublant :")
    lb3.grid(row=4,column=0,padx=10, pady=15)
    lb4 = Label(mod,text="Appreciation :")
    lb4.grid(row=5,column=0,padx=10, pady=15)
    entry0=Entry(mod,width=40)
    entry0.grid(row=0,column=1,padx=10, pady=10,columnspan=2)
    entry1=Entry(mod,width=40)
    entry1.grid(row=1,column=1,padx=10, pady=10,columnspan=2)
    entry2=Entry(mod,width=40)
    entry2.grid(row=3,column=1,padx=10, pady=10,columnspan=2)
    texte = Text(mod,height=20,width=40)
    texte.grid(row=5,column=1,columnspan=2,padx=10, pady=10)
    selected = IntVar()
    a = Radiobutton(mod,text="Oui",value=1,variable=selected)
    a.grid(row=4,column=1)
    b = Radiobutton(mod,text="Non",value=0,variable=selected)
    b.grid(row=4,column=2)
    apply=Button(mod, text="MODIFY", command=lambda : [ModifyIn(),mod.destroy()])
    apply.grid(row=7,column=1,padx=10, pady=10)
    mod.columnconfigure(0, weight=20)
    mod.columnconfigure(1, weight=1)
    mod.columnconfigure(2, weight=1)
    print('modified')

def DeleteOut():
    def DeleteIn():
        conn=sq.connect('Study.db')
        cur=conn.cursor()
        cur.execute("SELECT * FROM Student")
        conn.commit()
        list=cur.fetchall()
        idd = int(entr.get())
        x=0
        for i in range(len(list)):
            if list[i][0]==idd:
                x=1
        if x==1:
            NomPrenom=list[i][1]
            Notes=list[i][2]
            list[i][3]
            list[i][4]
            conn=sq.connect('Study.db')
            cur=conn.cursor()
            cur.execute("DELETE from Student WHERE ID=:ident",
                                {'ident':idd})
            conn.commit()
            messagebox.showinfo('Suppression', 'Eleve supprimé avec succès')
 
        else:
            messagebox.showinfo('Suppression', 'Suppression échoué..RéssayerSVP!')

    dell= Toplevel()
    dell.geometry('460x100+700+100')
    dell.title("Student's Suppression")
    lb1 = Label(dell,text="Identity:")
    lb1.grid(row=0,column=0,padx=10, pady=15)
    entr = Entry(dell,width=40)
    entr.grid(row=0,column=1,padx=10, pady=10,columnspan=2)
    b=Button(dell, text="DELETE", command=lambda : [DeleteIn(), dell.destroy()])
    b.grid(row=3,column=1,padx=10, pady=10)
    dell.columnconfigure(0, weight=1)
    dell.columnconfigure(1, weight=1)
    dell.columnconfigure(2, weight=1)
    
def Statistics():
    root=Tk()
    root.title('Graphes')
    
    Names=[]
    Notes=[]
    conn=sq.connect('Study.db')
    cur=conn.cursor()
    cur.execute("SELECT * FROM Student")
    list=cur.fetchall()
    for i in range(len(list)):
        Names.append(list[i][1])
        Notes.append(list[i][2])
    Fig1=plt.Figure(dpi=100)
    Subplot1=Fig1.add_subplot(111)
    xAxis=Names
    yAxis=Notes
    Subplot1.bar(xAxis, yAxis, color='green')  
    BAR=FigureCanvasTkAgg(Fig1, root)
    BAR.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=0)
    x=0
    for i in Notes:
        if i<11:
            x+=100/len(Notes)
    Size = [100-x,x]
    Fig2=plt.Figure(dpi=100)
    Subplot2=Fig2.add_subplot(111)
    LabelsPie='Succeded','Failed'
    PieSize=Size
    Colors=['grey','silver']
    Explode = (0, 0.1)
    Subplot2.pie(PieSize, colors=Colors, explode=Explode, labels=LabelsPie,autopct='%1.1f%%',shadow=True, startangle=90)
    Subplot2.axis('equal')
    PIE=FigureCanvasTkAgg(Fig2, root)
    PIE.get_tk_widget().pack() 
    root.mainloop()
        
    
#Variabels
NomPrenom=StringVar()
Notes=IntVar()
selected = IntVar()
Apprec=StringVar()
#Labels and texts
lbl1 = Label(window, text="Nom ET Prénom: ")
lbl1.grid(column=0, row=0,padx=10, pady=10)
txt1 = Entry(window,textvariable=NomPrenom, width=40)
txt1.grid(column=1, row=0,padx=10, pady=10,columnspan=2)
lbl2 = Label(window, text="Notes: ")
lbl2.grid(column=0, row=1,padx=10, pady=10)
txt2 = Entry(window,textvariable=Notes, width=40)
txt2.grid(column=1, row=1,padx=10, pady=10,columnspan=2)
lbl3 = Label(window, text="Redoublant: ")
lbl3.grid(column=0, row=2,padx=10, pady=10)
rad1 = Radiobutton(window,text='Oui', value=1, variable=selected)
rad1.grid(column=1, row=2,padx=10, pady=10)
rad2 = Radiobutton(window,text='Non', value=0, variable=selected)
rad2.grid(column=2, row=2,padx=10, pady=10)
lbl4 = Label(window, text="Appréciation: ")
lbl4.grid(column=0, row=3,padx=10, pady=10)
txt3 = Text(window,height=20,width=30)
txt3.grid(column=1, row=3,padx=10, pady=10,columnspan=2)
btn1 = Button(window, text="Listes Des Notes", command=Liste)
btn1.grid(column=1, row=4)
btn2 = Button(window, text="Ajouter", command=Ajout)
btn2.grid(column=2, row=4)
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='Modifier_Note', command=ModifyOut)
new_item.add_separator()
new_item.add_command(label='Supprimer_eleve', command=DeleteOut)
new_item.add_separator()
new_item.add_command(label='Statistique', command=Statistics)
menu.add_cascade(label='Choices', menu=new_item)
window.config(menu=menu)
window.columnconfigure(0, weight=2)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=2)
window.mainloop()


