from tkinter import *

checkbox_value = True

class Application(Frame):


    def say_hi(self):
        print("hi there, everyone!")

    def createWidgets(self):
        self.led_label = Label(root, text="LED")
        self.led_label.grid(row=0,column=0,padx=10,pady=10)

        self.led_checkbox = Checkbutton(root, text="on / off", variable=checkbox_value)
        self.led_checkbox.grid(row=0,column=1,padx=10,pady=10)
        

        self.QUIT = Button(root)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.grid(row=1,column=1,pady=10,padx=20,sticky=E)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createWidgets()

root = Tk()
root.title("LED Switch")
app = Application(root)
app.mainloop()
root.destroy()
