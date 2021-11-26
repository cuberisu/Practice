# 1 turtle graphics: 랜덤 눈사람
import turtle, random
t = turtle.Pen()
s = turtle.Screen()  # bgcolor() 함수 쓰려면 필요
t.shape("turtle")
t.color("black", "white")   # pencolor, fillcolor
s.bgcolor("skyblue")  # 배경 하늘색 만들기

def leggo(a, b):    # up - goto - down 함수
    t.up()
    t.goto(a, b)
    t.pd()

def fillcircle(r):  # 원을 그리고 색을 채우는 함수
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def snowman():  # 눈사람 그리기
    x = random.randint(1, 150)
    y = random.randint(1, 10)
    
    leggo(x, y) # 랜덤좌표 이동
    fillcircle(30)      # 3층
    
    leggo(x, y-30)
    fillcircle(20)      # 2층
    
    leggo(x-20, y-15)   # 2층 왼쪽
    t.goto(x-60, y+10)  # 왼쪽 팔 
    
    leggo(x+20, y-20)   # 2층 오른쪽
    t.goto(x+60, y)     # 오른쪽 팔
    
    leggo(x, y-90)
    fillcircle(40)      # 1층
    
snowman()
snowman()
snowman()
t._screen.exitonclick()
