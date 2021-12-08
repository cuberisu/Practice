# 5 turtle graphics: 리스트의 색상으로 다각형 그리기

import turtle, random
t = turtle.Pen()
t.shape("turtle")
t.speed(7)

colors = ["red", "blue", "green", "yellow", "orange", "skyblue"]



def leggo():    # 거북이 랜덤좌표
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.up(); t.goto(x, y); t.pd()
    


def draw():
    n = random.randint(3, 10)   
    length = random.randint(10, 100)
    color_list = random.randint(0, 5) 
    color_name = colors[color_list]
    t.fillcolor(color_name) # 랜덤 색
    
    leggo() # 랜덤 이동
    
    t.begin_fill()  # 색 채우기
    for i in range(n):  # 다각형 그리기
        t.fd(length)
        t.lt(360/n)
    t.end_fill()

for j in range(10):
    draw()


t._screen.exitonclick()