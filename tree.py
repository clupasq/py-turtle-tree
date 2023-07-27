from turtle import Turtle, mainloop, mode, tracer, update, colormode

mode("logo")
colormode(255)
tracer(10, 0)

MAX_LEVEL = 5

CHILD_BRANCH_COUNT = 5

MIN_WIDTH = 5
MAX_WIDTH = 50

MIN_LENGTH = 70
MAX_LENGTH = 200

A_WIDTH = (MIN_WIDTH - MAX_WIDTH) / MAX_LEVEL
B_WIDTH = MAX_WIDTH

A_LENGTH = (MIN_LENGTH - MAX_LENGTH) / MAX_LEVEL
B_LENGTH = MAX_LENGTH

from random import randint
from dataclasses import dataclass

t = Turtle()

@dataclass
class Stats:
    count: int = 0

def draw_branch(from_x, from_y, from_heading, stats, level=0):
    if level > MAX_LEVEL:
        return

    stats.count += 1

    # set state (position + heading), without leaving a trace
    t.penup()
    t.setx(from_x)
    t.sety(from_y)
    t.setheading(from_heading)
    t.pendown()

    # draw
    t.pencolor((42, 20 + level * 30, 42))
    t.width(level * A_WIDTH + B_WIDTH)
    t.forward(level * A_LENGTH + B_LENGTH)

    x, y = t.position()
    h = t.heading()

    for _ in range(CHILD_BRANCH_COUNT):
        draw_branch(x, y, h + randint(-50, 50), stats, level + 1)

s = Stats()
draw_branch(0, -300, 0, s)

update()

print(f"Number of branches drawn: {s.count}")

mainloop()



