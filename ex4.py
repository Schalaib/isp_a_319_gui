from tkinter import *
 
root = Tk()
e=Entry()
e.pack()
b1=Button(text="Открыть")
b1.pack()
b2=Button(text="Сохранить")
b2.pack()
te = Text()
te.pack()
def open3():
    v = open(e.get(), 'r')
    g=v.readlines()
    for item in g:
        te.insert(END, item)
    v.close()
def save():
    y = open(e.get(), 'w')
    y.writelines(te.get(1.0, END))
    y.close()
b1.config(command=open3)
b2.config(command=save)
root.mainloop()