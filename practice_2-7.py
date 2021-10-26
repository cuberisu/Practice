# 2-7 turtle graphics: 창문 그리기

import turtle
t = turtle.Pen()
t.shape("turtle")
side = 100  # 작은 사각형 한 변의 길이
angle = 90  # 회전할 각도

t.rt(angle) # right() = rt()

t.fd(side)
t.rt(angle)
t.fd(side)
t.rt(angle)
t.fd(side)
t.rt(angle)
t.fd(side)  # 왼쪽 아래 사각형

t.fd(side)
t.rt(angle)
t.fd(side)
t.rt(angle)
t.fd(side)
t.rt(angle)
t.fd(side)  # 오른쪽 아래 사각형

t.fd(side)
t.rt(angle)
t.fd(side)
t.rt(angle)
t.fd(side)
t.rt(angle)
t.fd(side)  # 오른쪽 위 사각형

t.fd(side)
t.rt(angle)
t.fd(side)
t.rt(angle)
t.fd(side)
t.rt(angle)
t.fd(side)  # 왼쪽 위 사각형

t._screen.exitonclick()