from Tkinter import *

master = Tk()

def printstate():
    print (val)

w = Spinbox(master, from_=62.0, to=83.5, command=(printstate))
w.pack()
b = Button(master, text=('print val'), command=(printstate))
b.pack()

mainloop()