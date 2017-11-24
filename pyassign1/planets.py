#!/usr/bin/env python3

"""Planet.py: Description of how the six planets in the solar system circulates.

__author__ = "Liuziyu"
__pkuid__  = "1700011766"
__email__  = "1700011766@pku.edu.cn"
"""

import turtle
import math
wn = turtle.Screen()


def planet(name, color, n, r):
    """using name, color, n and r, return the trace
    """
    t = turtle.Turtle()
    t.color(color)
    t.shapesize(n)
    t.shape("circle")
    t.speed(0)
    t.penup()
    t.goto(1.3*r,0)
    t.pendown()
    for i in range(900):
        a=math.cos(i/3)
        b=math.sin(i/3)
        x = 1.3*r*a
        y=r*b
        t.goto(x,y)


def main():
    """main module
    """
    a = "sun"
    b = "yellow"
    planet(a, b , 4.5, 0)
    c = "mercury"
    d = "blue"
    planet(c, d, 0.5, 50)
    e = "venus"
    f = "green"
    planet(e, f, 1, 80)
    g = "earth"
    h = "red"
    planet(g, h, 2, 120)
    i = "mars"
    j = "orange"
    planet(i, j, 1.5, 160)
    k = "jupiter"
    l = "black"
    planet(k, l, 3, 200)
    m = "saturn"
    n = "hotpink"
    planet(m, n, 2.5, 235)
    wn.exitonclick()
    
    
if __name__ == '__main__':
    main()
