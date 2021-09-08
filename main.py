from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # turning off the tracer

snake = Snake()
food = Food()
game_scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Move the snake
game_is_on = True
while game_is_on:
    screen.update()  # then our snake will appear not piece by piece,
    # but in it's entirety, and it will move along as an entire piece
    time.sleep(0.1)  # slowing down the process of moving
    snake.move()

    # Detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        game_scoreboard.increase_score()

    # Detect collision with wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        # game_is_on = False
        # game_scoreboard.game_over()
        game_scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    # if head collides with any segment in the tail:
    #   trigger game_over
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            # game_is_on = False
            # game_scoreboard.game_over()
            game_scoreboard.reset()
            snake.reset()







screen.exitonclick()
