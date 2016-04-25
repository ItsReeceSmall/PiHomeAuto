from tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.grid()

        self.titleLabel = Label(frame, text=('Home Automation System'), borderwidth=1).grid(row=1,column=2,padx=10,pady=10)
        self.LoopLabel = Label(frame, text=('Loop ' + str(loopVal)), borderwidth=1).grid(row=2,column=2,padx=10,pady=10)

        self.PirLabel = Label(frame, text=('Pir Value: '), borderwidth=1).grid(row=3,column=1,padx=10,pady=10)
        self.TempLabel = Label(frame, text=('Temperature: '), borderwidth=1).grid(row=4,column=1,padx=10,pady=10)
        self.LightLabel = Label(frame, text=('Light Sensor Value: '), borderwidth=1).grid(row=5,column=1,padx=10,pady=10)
        self.DistLabel = Label(frame, text=('Distance: '), borderwidth=1).grid(row=6,column=1,padx=10,pady=10)

        self.PirValue = Label(frame, text=(pir), borderwidth=1).grid(row=3, column=2, padx=10, pady=10)
        self.TempValue = Label(frame, text=(temp), borderwidth=1).grid(row=4, column=2, padx=10, pady=10)
        self.LightValue = Label(frame, text=(light), borderwidth=1).grid(row=5, column=2, padx=10,pady=10)
        self.DistValue = Label(frame, text=(dist), borderwidth=1).grid(row=6, column=2, padx=10, pady=10)

        self.close = Button(frame, text="Close", command=frame.quit).grid(row=7,column=2,padx=10,pady=10)

root = Tk()
root.title('Home Automation System v0.3 by Reece Small')
app = App(root)
root.mainloop()
root.destroy()