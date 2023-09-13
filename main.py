from tkinter import *
from random import randint, shuffle, randrange

root = Tk()
root.geometry('400x200')
colors =[f'grey{i}' for i in range(91,10,-10)]
colors = ['white'] + colors + ['black']

# print(colors)

canvas = Canvas(root, background='black', width=400,height=200)
canvas.pack()




def create_oval(canvas,x1,y1,x2,y2, level = 0):
    global colors
    if level == 10:
        canvas.create_oval(x1,y1,x2,y2, fill = colors[level])
        return 1
    else:
        canvas.create_oval(x1,y1,x2,y2, fill = colors[level])
        x_rand = randrange(-10,10)
        y_rand = randrange(5,15)
        x1,y1,x2,y2 = x1-x_rand,y1-y_rand,x2-x_rand,y2-y_rand
        return create_oval(canvas,x1,y1,x2,y2, level=level+1)
    
        
create_oval(canvas,180,180,190,190)
create_oval(canvas,180,180,190,190)
create_oval(canvas,180,180,190,190)

# for i in range(11):
#     create_oval(canvas,180,180 - i *10,190,190 - i * 10,transparent = i)
root.mainloop()
