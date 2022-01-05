from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(x=-200, y=200)
        self.write(self.l_score, align='center', font=('Arial', 20, 'normal'))
        self.goto(x=200, y=200)
        self.write(self.r_score, align='center', font=('Arial', 20, 'normal'))

    def left_point(self):
        self.l_score += 1
        self.update()

    def right_point(self):
        self.r_score += 1
        self.update()