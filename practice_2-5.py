# 2-5 turtle graphics: 변수를 활용한 삼각형 그리기

import turtle
t = turtle.Pen()
t.shape("turtle")
side = 100  # 문제에서 요구된 초기값이 100임. 한 변의 길이 변수
t.fd(side)  # side만큼, 100만큼 전진
t.lt(120)   # left() = lt()
t.fd(side)
t.lt(120)
t.fd(side)

t._screen.exitonclick()
