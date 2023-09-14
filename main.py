from tkinter import *
from random import randint, shuffle, randrange
import time

root = Tk()
root.geometry('400x200')
colors =[f'grey{i}' for i in range(91,10,-10)]
colors = ['white'] + colors + ['black']

# print(colors)

canvas = Canvas(root, background='black', width=400,height=200)
canvas.pack()

class Oval():
    colors = colors
    def __init__(self, canvas, x1,y1,x2,y2) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.level = 0
        self.canvas = canvas
        self.start_coord = (x1,y1,x2,y2)
        self.shape = canvas.create_oval(self.x1,self.y1,self.x2,self.y2, fill = Oval.colors[self.level])
        self.change_color()

    def update(self):
        pass
    
    def change_color(self,):
        self.canvas.itemconfig(self.shape, fill = colors[self.level])
        self.level += 1
        # print(self.level)
        if self.level == 11:
            self.level = 0
        self.canvas.after(100, self.change_color)

    
    


a = Oval(canvas=canvas, x1 = 180,y1=180,x2=190,y2=190)
# root.after(100, a.)

root.mainloop()
