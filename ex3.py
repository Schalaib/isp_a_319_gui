from cgitb import text
from tkinter import *
from turtle import bye
root = Tk()
bRED = Button(text = "",width=3,height=1)
bOrange = Button(text = "",width=3,height=1)
bBLUE = Button(text = "",width=3,height=1)
bYel = Button(text = "",width=3,height=1)
bGre = Button(text = "",width=3,height=1)
l = Label()
e = Entry()
def change():
    l['text'] = "RED"
    e.delete("0", END)
    e.insert(0,"#ff0000")
    bRED['bg'] = '#ff0000'
    bRED['activebackground'] = '#555555' 
    bRED['fg'] = '#ffffff'
def change1():
    l['text'] = "ORANGE"
    e.delete("0", END)
    e.insert(0,"#ff7d00")
    bOrange['bg'] = '#ff7d00'
    bOrange['activebackground'] = '#555555'
    bOrange['fg'] = '#ffffff'
def change2():
    l['text'] = "BLUE"
    e.delete("0", END)
    e.insert(0,"#0000ff")
    bBLUE['bg'] = '#0000ff'
    bBLUE['activebackground'] = '#555555'
    bBLUE['fg'] = '#ffffff'
def change3():
    l['text'] = "YELLOW"
    e.delete("0", END)
    e.insert(0,"#ffff00")
    bYel['bg'] = '#ffff00'
    bYel['activebackground'] = '#555555'
    bYel['fg'] = '#ffffff'
def change4():
    l['text'] = "GREEN"
    e.delete("0", END)
    e.insert(0,"#00ff00")
    bGre['bg'] = '#00ff00'
    bGre['activebackground'] = '#555555'
    bGre['fg'] = '#ffffff'
bRED.config(command=change)
bOrange.config(command=change1)
bBLUE.config(command=change2)
bYel.config(command=change3)
bGre.config(command=change4)
l.pack(side=TOP)
e.pack()
bRED.pack(side=LEFT,padx=5, pady=5)
bOrange.pack(side=LEFT,padx=5, pady=5)
bBLUE.pack(side=LEFT,padx=5, pady=5)
bYel.pack(side=LEFT,padx=5, pady=5)
bGre.pack(side=LEFT,padx=5, pady=5)
root.mainloop()