from tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.grid()

        self.DistLabel = Label(frame, text=('Distance'), borderwidth=1).grid(row=1,column=1)

        self.hi_there = Button(frame, text="Hello", command=frame.quit)
        self.hi_there.grid(row=1,column=2)

    def say_hi(self):
        print('Hello World!')

print('root = Tk()')
root = Tk()
print('app = App(root)')
app = App(root)
print('root.mainloop()')
root.mainloop()
print('root.destroy()')
root.destroy()