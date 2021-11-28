# 3 turtle graphics: 함수 그래프
# f(x) = x^2 + 1

# x축, y축도 그리기

import turtle
t = turtle.Pen()
t.shape("turtle")

def leggo(x, y):    # up - goto - down 함수
    t.up()
    t.goto(x, y)    # 절대좌표로 이동
    t.pd()

def f(x):   # x를 넣으면
    y = x**2 + 1
    return y    # 결과값 y를 반환

def graph():   # 함수식을 넣으면 그래프를 그리는 함수
    leggo(0, 0)     # 초기 좌표
    for x in range(150):    # x = 150까지
        t.goto(x, f(x)*0.01)   # y값이 너무 크니까 0.01을 곱한다.
        
        if x == 100:    # 제대로 됐는지 테스트
            t.dot() # x = 100인 좌표에 점을 찍기
            t.write(str(t.pos())+"(x, 0.01y)")  # 좌표값을 반환하는 함수 pos()
            
            
t.fd(300); t.write("x")   # x축
leggo(0, 0); t.write("O", align="right")   # 원점(서식: 오른쪽 정렬)
t.goto(0, 300); t.write("y")    # y축

x = 0
graph() # y = x**2 + 1 의 그래프를 그리는 커맨드

t._screen.exitonclick()