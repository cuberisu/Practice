# 7 turtle graphics: list와 fillcolor()

print("색상을 입력하세요(english).")
c1 = input("1: ")
c2 = input("2: ")
c3 = input("3: ")
colors = [c1, c2, c3]

import turtle
t = turtle.Pen()
t.shape("turtle")

t.fillcolor(colors[0])   # 채워지는 색(거북이 색상 또한 바뀐다)
t.begin_fill()  # 색 채우기 시작
t.circle(50)
t.end_fill()    #색 채우기 종료. 이제 색이 채워진다

t.up()
t.goto(100, 0)
t.pd()
t.fillcolor(colors[1])
t.begin_fill()
t.circle(50)
t.end_fill()


t.up()
t.goto(200, 0)
t.pd()
t.fillcolor(colors[2])
t.begin_fill()
t.circle(50)
t.end_fill()

t._screen.exitonclick()