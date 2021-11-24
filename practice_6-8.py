# 8 turtle graphics: 10 stars
import turtle
t = turtle.Pen()
t.shape("turtle")
t.color("red")

for n in range(10):
    for i in range(5):  # 별
        t.bk(200)
        t.rt(144)
    t.lt(10)    # 시작각도 조절

t._screen.exitonclick()