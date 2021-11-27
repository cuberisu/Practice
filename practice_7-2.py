# 2 turtle graphics: 벌집
import turtle
t = turtle.Pen()
t.shape("turtle")

def leggo(x, y):    # up - goto - down 함수
    t.up()
    t.goto(x, y)    # 절대좌표로 이동
    t.pd()

def draw_hexa(a, b):    # 좌표를 받아 한변 100 크기 정육각형을 그리기
    leggo(a, b)
    for i in range(6):
        t.fd(100)
        t.lt(60)

draw_hexa(0, 0) # 가운데

h1 = (200**2 - 100**2)**0.5  # 육각형 내부에 대각선이 아닌 선을 그었을 때의 길이
h2 = 3**0.5 / 2 * h1    # 정삼각형의 높이 공식을 이용, 
    # 요 애매한 길이를 이용해 육각형의 좌표를 맞출 것임

draw_hexa(-h2, h1/2)    # 왼쪽 위
draw_hexa(-h2, -h1/2)   # 왼쪽 아래
draw_hexa(150, h1/2)    # 오른쪽 위
draw_hexa(150, -h1/2)   # 오른쪽 아래
draw_hexa(0, -h1)       # 가운데 아래
draw_hexa(0, h1)        # 가운데 위

t._screen.exitonclick()