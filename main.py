from turtle import Screen
import time
from food import Food
from snake import Snake
from score import Score_Tracker

COLORS_LST = ['red', 'purple', 'violet', 'pink']
screen = Screen()
screen.tracer(0)
screen.setup(width=700, height=700)
screen.bgcolor('white')
screen.title('My snake Game')


snake = Snake()
food = Food()
score_tracker1 = Score_Tracker()
screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

repeat_the_game = True
a = 1


def a_determinator():  # a determinator is to used to skip some steps while changing colour.
    global a
    if a < 3:
        a += 1
        return a
    else:
        a = 1
        return a


while repeat_the_game:
    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.09)
        snake.move()
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()

            for name in snake.name_lst:
                name.color(COLORS_LST[a_determinator() - 1])
            score_tracker1.update_score()
            score_tracker1.increase_score()
            print("nom, nom ,nom")

        x_co = snake.head.xcor()
        y_co = snake.head.ycor()

        if x_co > 340 or x_co < -340 or y_co > 340 or y_co < -340:
            score_tracker1.reset()
            snake.reset()
            screen.update()
            game_is_on = False

        for name in snake.name_lst[1:]:
            if snake.head.distance(name) < 10:
                score_tracker1.reset()
                snake.reset()
                screen.update()
                game_is_on = False

screen.exitonclick()
