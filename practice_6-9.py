# 9 turtle graphics: 10 random circles
import turtle, random
t = turtle.Pen()
t.shape("turtle")

for i in range(10):
    r = random.randint(1, 100)  # 반지름
    x = random.randint(1, 100)  # 거북이 좌표 (x, y)
    y = random.randint(1, 100)
    t.up(); t.goto(x, y); t.pd()
    t.circle(r)
    
t._screen.exitonclick()