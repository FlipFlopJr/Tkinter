from tkinter import *

root = Tk()
root.geometry('400x200')
colors =[f'grey{i}' for i in range(91,10,-10)]
colors = ['white'] + colors + ['black']
# print(colors)

canvas = Canvas(root, background='black', width=400,height=200)
canvas.pack()


def create_oval(canvas,x1,y1,x2,y2, **kwargs):
    global colors
    if 'transparent' in kwargs:
        transparent = kwargs.pop('transparent')
        print(transparent)
        canvas.create_oval(x1,y1,x2,y2, fill = colors[transparent])
    # elif kwargs['transparent'] not in range(0,10):
    #     raise IndexError('Слишком большое значение прозрачности')
    else:
        canvas.create_oval(x1,y1,x2,y2, fill = colors[0])


create_oval(canvas,180,180,190,190,transparent = 10)
root.mainloop()
