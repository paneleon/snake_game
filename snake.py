from turtle import Turtle

# initial 3 segments of the snake
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
# direction degrees
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        # what happens when a new snake object is initialized
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # creates a new part (segment) of the snake
        new_square = Turtle(shape="square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.segments.append(new_square)

    def extend(self):
        # add a new segment to the end of the snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        # loops though each segment in reverse order using range(start, stop, step)
        for seg_number in range(len(self.segments) - 1, 0, -1):
            # get the second to last segment coordinates:
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            # gets the segment to move to the previous position of the next segment
            # (make the tail follow the head)
            self.segments[seg_number].goto(new_x, new_y)
        # moves the first segment as well
        self.snake_head.forward(MOVE_DISTANCE)

    # restricts snake possible moves
    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)  # makes the old snake disappear from the screen
        self.segments.clear()  # removes all segment items from the list
        self.create_snake()  # creates new snake after
        self.snake_head = self.segments[0]


