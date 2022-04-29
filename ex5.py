from tkinter import *
 
 
def change():
    if var.get() == 0:
        label['text'] = "+7992948485"
    elif var.get() == 1:
        label['text'] = '+7938477474'
    elif var.get() == 2:
        label['text'] = '+7947466464'
 
 
root = Tk()
 
var = IntVar()
var.set(0)
red = Radiobutton(text="Дмитрий",
                  variable=var, value=0,command= change,indicatoron=0,width=7,height=2)
green = Radiobutton(text="Денис",
                    variable=var, value=1,command=change, indicatoron=0,width=7,height=2)
blue = Radiobutton(text="Егор",
                   variable=var, value=2,command=change,indicatoron=0,width=7,height=2)
label = Label()
label.pack(side=RIGHT)
red.pack()
green.pack()
blue.pack()

 
root.mainloop()