from tkinter import *
from .window import Window

class Mind:
    def __init__(self,title,width,height):
        self.width = width
        self.height = height
        self.window = Tk()
        self.window.resizable(False, False)
        self.canvas = Canvas(self.window,width=self.width,height=self.height,bg="black")
        self.canvas.pack()
        self.win = Window(self.window,self.canvas,title, width, height)
        
        
    def mainloop(self):
        self.window.mainloop()
        
    def explode(self):
        self.window.destroy()
        
    def configure(self,option):
        self.option = option
        if self.option == "-splash":
            self.window.overrideredirect(True)