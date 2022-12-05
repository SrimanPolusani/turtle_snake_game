from turtle import Turtle

DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

POSITIONS = [(-20, 0), (0, 0), (20, 0)]
COLORS_LST = ['red', 'purple', 'violet', 'pink', 'SkyBlue', 'tomato', 'gold', 'chartreuse', 'cyan', 'DarkMagenta', 'DarkCyan', 'DarkOrchid1', 'DeepPink1', 'DarkOrange1', 'coral2']


class Snake:  # (Disco_colors)

    def __init__(self):
        # super().__init__()
        self.name_lst = []
        self.create_snake()
        self.move()
        self.head = self.name_lst[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_name(position)

    def move(self):
        for position_number in range((len(self.name_lst) - 1), 0, -1):
            new_x = self.name_lst[position_number - 1].xcor()
            new_y = self.name_lst[position_number - 1].ycor()
            self.name_lst[position_number].goto(new_x, new_y)
            # self.name_lst[position_number].color(COLORS_LST[self.b])
            # self.disco_colors()
        self.name_lst[0].forward(DISTANCE)

    def add_name(self, position):
        name = Turtle()
        name.penup()
        name.turtlesize(1)
        name.shape('square')
        name.setpos(position)
        self.name_lst.append(name)

    def extend(self):
        self.add_name(self.name_lst[-1].pos())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def reset(self):
        for name in self.name_lst:
            name.goto(350, 350)
        self.name_lst.clear()
        self.create_snake()
        self.head = self.name_lst[0]


