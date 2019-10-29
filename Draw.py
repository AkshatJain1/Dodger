from tkinter import *
import random
#init tk system
tk = Tk()
#create canvas
canvas = Canvas(tk,width=500,height=400)
#create title
tk.title("Drawing")
#we done with settings
canvas.pack()


#creates line
canvas.create_line(0, 0, 500, 400)

canvas.create_rectangle(100,150,200,250,fill='red')

canvas.create_oval(200,250,500,350,fill='green')

canvas.create_polygon(400,10,300,300,500,300,fill='blue')

for i in range(100):
    x1 = random.randrange(500)
    y1 = random.randrange(400)
    x2 = random.randrange(500)
    y2 = random.randrange(400)
    canvas.create_rectangle(x1,y1,x2,y2)


#It will wait
canvas.mainloop()

