from tkinter import *
#калькулятор только для целых ЧИСЕЛ
root = Tk()
e1 = Entry(width=9)
e1.pack()

e2 = Entry(width=9)
e2.pack()

def plus():
  a=int(e1.get())
  b=int(e2.get())
  c=a+b
  l['text']=c
def ymno():
  a=int(e1.get())
  b=int(e2.get())
  c=a*b
  l['text']=c

def delit():
  a=int(e1.get())
  b=int(e2.get())
  if b==0:
    l['text'] = "На нуль делить нельзя"
  else:
    c=a/b
    l['text']=c


def minus():
  a=int(e1.get())
  b=int(e2.get())
  c=a-b
  l['text']=c


b1 = Button(text="+",width=9)
b1.pack()
b1.config(command=plus)

b2 = Button(text="-",width=9)
b2.pack()
b2.config(command=minus)

b3 = Button(text="*",width=9)
b3.pack()
b3.config(command=ymno)

b4 = Button(text="/",width=9)
b4.pack()
b4.config(command=delit)

l = Label()
l.pack()
root.mainloop()