import time
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
from snake import Snake

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detecting collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detecting collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_game()
        scoreboard.update_scoreboard()
        snake.reset_snake()

    # Detect collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset_game()
            snake.reset_snake()

    # for segment in snake.segments[1:]:
    #     if snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()
screen.exitonclick()

# snake_body = []
# x_index = [0, -20, -40]
# for turtle in range(0, 3):
#     snake = Turtle(shape="square")
#     snake.color("white")
#     snake.goto(x=x_index[turtle], y=0)
