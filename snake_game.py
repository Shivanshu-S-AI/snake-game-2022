import turtle
import time
import random

speed_delay = 0.1

# Game stats
current_score = 0
top_score = 0

# Game window
window = turtle.Screen()
window.title("Classic Snake Game - Shivanshu Edition")
window.bgcolor("darkgreen")
window.setup(width=600, height=600)
window.tracer(0)

# Snake starter block
player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("black")
player.penup()
player.goto(0, 0)
player.direction = "stop"

# Snake food
snack = turtle.Turtle()
snack.speed(0)
snack.shape("circle")
snack.color("red")
snack.penup()
snack.goto(0, 100)

snake_body = []

# Score display
score_writer = turtle.Turtle()
score_writer.speed(0)
score_writer.shape("square")
score_writer.color("white")
score_writer.penup()
score_writer.hideturtle()
score_writer.goto(0, 260)
score_writer.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Controls
def move_up():
    if player.direction != "down":
        player.direction = "up"

def move_down():
    if player.direction != "up":
        player.direction = "down"

def move_left():
    if player.direction != "right":
        player.direction = "left"

def move_right():
    if player.direction != "left":
        player.direction = "right"

def snake_move():
    if player.direction == "up":
        y = player.ycor()
        player.sety(y + 20)
    elif player.direction == "down":
        y = player.ycor()
        player.sety(y - 20)
    elif player.direction == "left":
        x = player.xcor()
        player.setx(x - 20)
    elif player.direction == "right":
        x = player.xcor()
        player.setx(x + 20)

# Keyboard bindings
window.listen()
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")

# Game loop
while True:
    window.update()

    # Border collision
    if player.xcor() > 290 or player.xcor() < -290 or player.ycor() > 290 or player.ycor() < -290:
        time.sleep(1)
        player.goto(0, 0)
        player.direction = "stop"

        for part in snake_body:
            part.goto(1000, 1000)
        snake_body.clear()

        current_score = 0
        speed_delay = 0.1

        score_writer.clear()
        score_writer.write("Score: {}  High Score: {}".format(current_score, top_score), align="center", font=("Courier", 24, "normal"))

    # Food collision
    if player.distance(snack) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        snack.goto(x, y)

        new_part = turtle.Turtle()
        new_part.speed(0)
        new_part.shape("square")
        new_part.color("gray")
        new_part.penup()
        snake_body.append(new_part)

        speed_delay -= 0.001
        current_score += 10

        if current_score > top_score:
            top_score = current_score

        score_writer.clear()
        score_writer.write("Score: {}  High Score: {}".format(current_score, top_score), align="center", font=("Courier", 24, "normal"))

    # Move segments
    for i in range(len(snake_body) - 1, 0, -1):
        x = snake_body[i - 1].xcor()
        y = snake_body[i - 1].ycor()
        snake_body[i].goto(x, y)

    if len(snake_body) > 0:
        x = player.xcor()
        y = player.ycor()
        snake_body[0].goto(x, y)

    snake_move()

    # Self-collision
    for part in snake_body:
        if part.distance(player) < 20:
            time.sleep(1)
            player.goto(0, 0)
            player.direction = "stop"

            for part in snake_body:
                part.goto(1000, 1000)
            snake_body.clear()

            current_score = 0
            speed_delay = 0.1

            score_writer.clear()
            score_writer.write("Score: {}  High Score: {}".format(current_score, top_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(speed_delay)

window.mainloop()
