import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
########### Challenge 3 - Draw Shapes ########

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    my_rgb = (r, g, b)
    return my_rgb


directions = [0, 90, 180, 270]
# for i in range(200):
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#     tim.color(random_color())
#     tim.width(15)
tim.speed("fast")

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)
        tim.circle(100)

draw_spirograph(5)