from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # reads the highest score from the text file
        with open("high_score_data.txt") as high_score_data:
            self.high_score = int(high_score_data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        # clears the scoreboard and displays score
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        # if new score is higher than the record score
        if self.score > self.high_score:
            # assigns a new record score
            self.high_score = self.score
            # and saves it into the text file
            with open("high_score_data.txt", mode="w") as high_score_data:
                high_score_data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()



