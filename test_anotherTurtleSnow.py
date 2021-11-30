import turtle
t = turtle.Pen()
t.shape("turtle")
t.lt(90)    # 시작 각도 (위를 바라봄)

for i in range(1, 7):   # 123456 반복
    t.fd(100)
    t.fd(-30)
    t.lt(60); t.fd(30); t.fd(-30)
    
    t.rt(120); t.fd(30); t.fd(-30)
    
    t.lt(60)    # 제자리 각도
    t.fd(-70)   # goto(0, 0)
    t.lt(60)    # 다음 사이클 시작 각도

t._screen.exitonclick()