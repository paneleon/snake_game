from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# sets up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # turning off the tracer

# creates snake, food, and scoreboard objects
snake = Snake()
food = Food()
game_scoreboard = Scoreboard()

# controls the snake with a keypress
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# moves the snake
game_is_on = True
while game_is_on:
    screen.update()  # the snake will appear not piece by piece,
    # but move along as an entire piece
    time.sleep(0.1)  # slowing down the process of moving
    snake.move()

    # detects collision with food
    # if the snake touches the food
    if snake.snake_head.distance(food) < 15:
        # it moves to a new random location on screen
        food.refresh()
        # and adds a new segment to snake
        snake.extend()
        game_scoreboard.increase_score()

    # detects collision with wall from any side
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        game_scoreboard.reset()
        snake.reset()

    # detect collision with tail
    # if head collides with any segment in the tail
    #   triggers game_over
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            game_scoreboard.reset()
            snake.reset()

screen.exitonclick()
