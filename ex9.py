from tkinter import *
root = Tk()
c = Canvas(root, width=200, height=200, bg='white')
c.pack()
c.create_oval(160, 10, 190, 40, width=2,fill='orange',outline='yellow')
di = 0
x0=0
y0=340
x1=40
y1=170
c.create_line(100, 180, 100, 60, fill='lightblue',
                width=80,arrow=LAST,arrowshape="40 40 30")
while di < 100:
    d = 8
    x0 = x0+d
    y0 = y0
    x1 = x1+d
    y1 = y1
    c.create_arc(x0, y0, x1, y1, start=160, extent=-70, style=ARC, outline='green', width=2)
    di +=1

root.mainloop()