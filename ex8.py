from tkinter import *
#не понимаю, как перемещать кнопки
root = Tk() 
b = Button(text='Изменить') 
e1=Entry(width=5)
e1.pack()
e2=Entry(width=5)
e2.pack()
b.pack()
t = Text(height=5,width=20)
t.pack()
def enter(event):
    t['bg'] = 'lightgrey'
def exit(event):
    t['bg'] = 'white'
def change(event):
    t.configure(height= e1.get())
def change2(event):
    t.configure(width= e2.get())
def change3():
    t.configure(height= e1.get(),width= e2.get())
t.bind('<FocusIn>',enter)
t.bind('<FocusOut>',exit)
e1.bind('<Return>',change)
e2.bind('<Return>',change2)
b.config(command=change3)
root.mainloop()
