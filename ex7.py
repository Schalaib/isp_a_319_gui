from tkinter import *
root = Tk()
 

lbox = Listbox( width=10, height=5)
lbox.pack()
def enter(event):
    lbox.insert(0,e.get())
def copy(event):
    e.delete(0,END)
    select = lbox.curselection()
    for i in select:
        e.insert(END,lbox.get(i))
e = Entry()
lbox.bind('<Double-Button-1>',copy)
e.bind('<Return>',enter)
e.pack()
root.mainloop()

