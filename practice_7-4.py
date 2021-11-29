# 4 turtle graphics: 움직이지 않고 선을 긋는 함수?
# 거북이는 항상 중앙에 위치
# 거미줄 모양을 그리자

import turtle
t = turtle.Pen()
t.shape("turtle")

def draw_line():
    t.fd(100)
    t.bk(100)
    
for i in range(12):
    draw_line()
    t.lt(30)

t._screen.exitonclick()