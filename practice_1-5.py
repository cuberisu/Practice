# 5 turtle graphics: 선의 두께

import turtle
t = turtle.Pen()
t.shape("turtle")
t.width(10)     # 선의 두께를 10픽셀로 한다
t.fd(100)       # = t.forward(100)
t.lt(90)        # = t.left(90)
t.fd(100)
t._screen.exitonclick()
