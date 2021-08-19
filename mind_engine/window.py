#the basic window module for the mind_engine 
import tkinter as tk

#the main class
class Window:
    def __init__(self,parent,canvas,title,width,height,titlebar=False):
        #setting up the self variabels
        self.parent = parent
        self.title = title
        self.width = width
        self.height = height
        self.titlebar = titlebar
        #start the setup
        self.setup()
    def setup(self):
        #the size fo the window
        self.parent.geometry(str(self.width) + "x" + str(self.height))
        #title
        self.parent.title(str(self.title))