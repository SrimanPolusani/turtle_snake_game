from turtle import Turtle


class Score_Tracker(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 310)
        self.hideturtle()
        with open("high_score.txt") as data:
            self.highscore = int(data.read())

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.highscore}", align='Center',
                   font=('Arial', 20, 'normal'))

    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.update_score()

    # def end_game(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", align='Center', font=('Arial', 30, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("high_score.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()
