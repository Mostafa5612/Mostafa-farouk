import turtle

# initialize screen
wind = turtle.Screen()
wind.title("Ping Pong with (Mostafa)")
wind.bgcolor("dark blue")
wind.setup(width=800, height=600)
wind.tracer(0)

# madrb 1
madrb1 = turtle.Turtle()
madrb1.speed(0)
madrb1.shape("square")
madrb1.color("white")
madrb1.shapesize(stretch_wid = 5, stretch_len = 1)
madrb1.penup()
madrb1.goto(-350, 0)

# madrb 2
madrb2 = turtle.Turtle()
madrb2.speed(0)
madrb2.shape("square")
madrb2.color("white")
madrb2.shapesize(stretch_wid=5, stretch_len=1)
madrb2.penup()
madrb2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(100)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.5
ball.dy = 2.5
#score
score1 = 0
score2 = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

# Main game loop
def update_game():
    global score1, score2
    wind.update()

# functions
def madrb1_up():
    y = madrb1.ycor()
    y += 20
    madrb1.sety(y)

def madrb1_down():
    y = madrb1.ycor()
    y -= 20
    madrb1.sety(y)

def madrb2_up():
    y = madrb2.ycor()
    y += 20
    madrb2.sety(y)

def madrb2_down():
    y = madrb2.ycor()
    y -= 20
    madrb2.sety(y)

# keyboard bind
wind.listen()
wind.onkeypress(madrb1_up, "w")
wind.onkeypress(madrb1_down, "s")
wind.onkeypress(madrb2_up, "Up")
wind.onkeypress(madrb2_down, "Down")

# Main game loop
def update_game():
    global score1, score2
    wind.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    wind.ontimer(update_game, 10)
    

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score_display.clear()
        score_display.write("Player 1: {}  Player 2: {}".format(score1 , score2), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score_display.clear()
        score_display.write("Player 1: {}  Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))


    # Check for collision with madrb1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < madrb1.ycor() + 50 and ball.ycor() > madrb1.ycor() - 50):
        ball.dx *= -1

    # Check for collision with madrb2
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < madrb2.ycor() + 50 and ball.ycor() > madrb2.ycor() - 50):
        ball.dx *= -1
        
        # Start the game loop
update_game()

# Run the game
wind.mainloop()