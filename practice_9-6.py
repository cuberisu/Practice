# 6 turtle graphics: 리스트의 색상으로 랜덤 별 그리기

import turtle, random
t = turtle.Pen()
s = turtle.Screen() # bgcolor() 함수 쓰기 위해
t.shape("turtle")
t.speed(0)
s.bgcolor("black")  # 배경 색 바꾸기

colors = ["red", "blue", "green", "yellow", "orange", "skyblue", "white"]

def leggo():    # 거북이 랜덤좌표
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.up(); t.goto(x, y); t.pd()

def draw():
    length = random.randint(10, 200)
    color_list = random.randint(0, 6) 
    color_name = colors[color_list]
    t.color(color_name, color_name) # 랜덤 색
    
    leggo() # 랜덤 이동
    
    t.begin_fill()  # 색 채우기
    for i in range(5):  # 별 그리기
        t.fd(length)
        t.rt(144)
    t.end_fill()

for j in range(20):
    draw()

t._screen.exitonclick()