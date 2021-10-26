# 2-4 turtle graphics: 변수를 활용한 원 그리기

import turtle
t = turtle.Pen()
t.shape("turtle")
radius = 50     # 문제에 주어진 초기값 50을 변수에 대입
t.circle(radius)

radius += 20    # 20씩 증가시키면서 그리라고 함. radius = 70
# radius = radius + 20 과 동일한 수식이다. 3장에 "복합연산자"라고 언급된다.
t.up()
t.goto(100, 0)   # (100, 0) 좌표에 원을 그리라고 함
t.pd()  # down() = pendowm() = pd()
t.circle(radius)    # 반지름 70

radius += 20    # radius = 90
t.up()
t.goto(200, 0)  # 문제에서 요구한 좌표
t.pd()
t.circle(radius)   # 반지름 90

t._screen.exitonclick()