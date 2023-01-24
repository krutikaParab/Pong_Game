from turtle import Turtle
WIDTH = 5
HEIGHT = 1
X_POS = 350
Y_POS = 0


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        self.penup()
        self.goto(position)
        # self.setpos(X_POS, Y_POS)
        
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
