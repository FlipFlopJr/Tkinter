from tkinter import *
from random import randint, shuffle, randrange, random
import time

root = Tk()
root.geometry('400x200')
colors =[f'grey{i}' for i in range(91,10,-10)]
colors = ['white'] + colors + ['black']

# print(colors)

canvas = Canvas(root, background='black', width=400,height=200)
canvas.pack()

def callback(event):  
    print( event.x, event.y)

canvas.bind("<Button-1>", callback)


class Oval():
    colors = colors
    def __init__(self, canvas, x1,y1,x2,y2) -> None:
        self.x_plus = randrange(0,2)
        self.x1 = x1 - self.x_plus
        self.y1 = y1 - self.x_plus
        self.x2 = x2 + self.x_plus
        self.y2= y2 + self.x_plus
        print(self.x1,self.y1,self.x2,self.y2)
        self.level = 0
        self.canvas = canvas
        self.x_sum, self.y_sum = 0,0
        self.shape = canvas.create_oval(self.x1,self.y1,self.x2,self.y2, fill = Oval.colors[self.level])
        self.canvas.after(randrange(0,1000), self.move)


    def change_color(self,):
        self.canvas.itemconfig(self.shape, fill = colors[self.level])
        self.level += 1
        
    def move(self):
        x_rand = randrange(-12, 12)
        y_rand = randrange(8,20)
        if self.level == 11:
            self.level = 0
            self.canvas.move(self.shape, -self.x_sum, self.y_sum)
            self.x_sum, self.y_sum = 0,0
        else:
            self.x_sum+=x_rand
            self.y_sum+=y_rand
            self.canvas.move(self.shape, x_rand, - y_rand)
        self.change_color()
        self.canvas.after(75, self.move)

    

for i in range(20):
    a = Oval(canvas=canvas, x1 = 180,y1=160,x2=190,y2=170)



root.mainloop()
