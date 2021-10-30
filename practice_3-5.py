# turtle graphics: 거북이로 두 점 사이의 거리 확인하기
import turtle
t = turtle.Pen()
t.shape("turtle")
t.lt(45)
t.fd(141)

t.hideturtle()  # 거북이 숨기기
t.up()
t.goto(0,0)     # 이때 각도는 여전히 45도이므로 각도를 재설정해야한다
t.pd()
t.rt(45)    # 이전 각도와 상관없이 각도를 설정하려면 setheading()을 활용하는 것이 편리
t.showturtle()      # 거북이 나타나기

t.fd(100)
t.lt(90)
t.fd(100)

t._screen.exitonclick()