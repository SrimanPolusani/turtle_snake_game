from turtle import Turtle
import random

COLORS_LST = ['red', 'purple', 'violet', 'pink', 'SkyBlue', 'tomato', 'gold', 'chartreuse', 'cyan', 'DarkMagenta',
              'DarkCyan', 'DarkOrchid1', 'DeepPink1', 'DarkOrange1', 'coral2']

a = 1


def a_determinator():
    global a
    if a < 14:
        a += 1
        return a
    else:
        a = 1
        return a


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed('fastest')

    def refresh(self):
        random_x = random.randint(-330, 330)
        random_y = random.randint(-330, 330)
        self.goto(random_x, random_y)
        self.color(COLORS_LST[a_determinator()])
