from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle = Turtle()
paddle.color("white")
paddle.shape("square")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(x=350, y=0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
