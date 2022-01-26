import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("S N A K E")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
# Save high score

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.listen()

    # Detect collision with food.

    if snake.head.distance(food) < 15:
        food.refresh()
        score.update()
        snake.extend()

    # Detect collision with wall.

    if snake.head.xcor() > 280 or snake.head.ycor() > 280 \
            or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()
