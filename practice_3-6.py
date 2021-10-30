# 6 turtle graphics: 입력받은 두 점을 거북이로 잇고 길이 계산하기

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

import turtle
t = turtle.Pen()
t.shape("turtle")

t.up()  # 맨 처음에 goto를 해도 (0,0)에서 (x1,y1)로 선이 그어지므로...
t.goto(x1, y1)
t.pd()
t.goto(x2, y2)
print("두 점 사이의 거리는", ((x1-x2)**2+(y1-y2)**2)**0.5)

t._screen.exitonclick()