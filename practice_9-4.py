# 4 turtle graphics: 리스트에 색깔 저장하여 사각형 그리기

import turtle, random
t = turtle.Pen()
t.shape("turtle")
colors = ["yellow", "green", "purple", "red", "blue", "skyblue"]

def place():    # 랜덤 좌표 이동
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.up()
    t.goto(x, y)
    t.pd()

for j in colors[:]: # 리스트 인덱스 전체 슬라이싱, 인덱스 0부터 접근
    place()
    t.fillcolor(j)  # 인덱스 0인 컬러부터 시작
    t.begin_fill()  # 채우기 시작함수
    for i in range(4):  # 사각형 그리기
        t.fd(100)
        t.lt(90)
    t.end_fill()    # 색채우기 함수

t._screen.exitonclick()

