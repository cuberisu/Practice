# 10 turtle graphics: 왕복 달리기
import turtle
t = turtle.Pen()
t.shape("turtle")

for i in range(5):
    t.fd(200)
    t.rt(90)
    t.fd(20)
    t.rt(90)

    t.fd(200)
    t.lt(90)
    t.fd(20)
    t.lt(90)

t._screen.exitonclick()