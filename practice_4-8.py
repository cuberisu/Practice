# turtle graphics: list와 goto를 활용한 이동

print("좌표를 입력하세요.")
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))
x3 = int(input("x3: "))
y3 = int(input("y3: "))
points = [x1, y1, x2, y2, x3, y3]

import turtle
t = turtle.Pen()
t.shape("turtle")

t.up()
t.goto(points[0], points[1])
t.pd()
t.goto(points[2], points[3])
t.goto(points[4], points[5])

t._screen.exitonclick()