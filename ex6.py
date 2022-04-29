from audioop import reverse
from tkinter import *
 
root = Tk()

tovar= ['cucumber','carrot',"burgar","chips"]
lbox = Listbox(width=15,height=8)
for tov in tovar:
    lbox.insert(END,tov)
lbox.pack(side=LEFT)
lbox2 = Listbox(width=15,height=8)
lbox2.pack(side=RIGHT)
def change1():
    select = lbox.curselection()
    for i in select:
        lbox2.insert(END,lbox.get(i))
    for i in reversed(select):
        lbox.delete(i)
def change2():
    select = lbox2.curselection()
    for i in select:
        lbox.insert(END,lbox2.get(i))
    for i in reversed(select):
        lbox2.delete(i)

b1 = Button(width=3,height=2,command=change1,text=">>").pack(expand=1)
b2 = Button(width=3,height=2,command=change2,text="<<").pack(expand=1)

root.mainloop()
