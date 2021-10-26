# 2-6 turtle graphics: 변수를 활용한 삼각형 그리기-2

import turtle
t = turtle.Pen()
t.shape("turtle")
side = 200  # 한 변의 길이를 바꿀 때 변수를 활용하면 편리하다. 
t.fd(side)  # 200만큼 전진
t.lt(120)
t.fd(side)
t.lt(120)
t.fd(side)

t._screen.exitonclick()