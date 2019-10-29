from tkinter import *
import time
import random

WIDTH = 900
HEIGHT = 800

tk = Tk()
canvas = Canvas(tk,width = WIDTH, height = HEIGHT)
tk.title('Bouncing balls')
canvas.pack()

class Ball:
    def __init__(self, color, size=50):
        self.shape = canvas.create_rectangle(10,10,size,size, fill = color)
        self.xspeed = random.randrange(-20,20)
        self.yspeed = random.randrange(-20,20)

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)

        pos = canvas.coords(self.shape)
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.yspeed = -self.yspeed
        elif pos[2] >= WIDTH or pos[0] <= 0:
            self.xspeed = -self.xspeed


colorList = ['blue', 'green', 'purple', 'red', 'orange', 'pink','cyan','dodgerblue',
               'grey', 'gold', 'turquoise', 'magenta', 'yellow' ]
ballList = []
for x in range(200):
    ballList.append(Ball(random.choice(colorList),random.randrange(20,50)))

while True:

    #move each ball in list
    for ball in ballList:
        ball.move()
    #update the balls
    tk.update()

    #slow down 0.01 secods pause after each frame
    time.sleep(0.03)

tk.mainloop()