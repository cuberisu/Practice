# 8 turtle graphics: 입력받은 원과 조건문

print("큰 원의 중심 좌표(x1, y1)를 입력하세요.")
x1 = int(input("x1: "))
y1 = int(input("y1: "))
r1 = int(input("큰 원의 반지름: "))

print("작은 원의 중심 좌표(x2, y2)를 입력하세요.")
x2 = int(input("x2: "))
y2 = int(input("y2: "))
r2 = int(input("작은 원의 반지름: "))


import turtle
t = turtle.Pen()
t.shape("turtle")

t.up()
t.goto(x1, y1-r1)   # 거북이가 (x1,y1)에서 시작하면 (x1,y1+r1)이 중심좌표가 된다
t.pd()
t.circle(r1)

t.up()
t.goto(x2, y2-r2)
t.pd()
t.circle(r2)

t.hideturtle()  # 거북이 없애기

if x1-r1 <= x2-r2 <= x2+r2 <= x1+r1 and y1-r1 <= y2-r2 <= y2+r2 <= y1+r1:
    # 이걸 어떻게 주석을 달아요...?
    # x축 끝에서 끝이 x-r에서 x+r임 y축도 마찬가지
    # 완전히 들어갔을 때 실행되는 코드임
    t.write("작은 원이 큰 원의 내부에 있습니다.")     # 터틀그래픽 스크린에서 출력
elif ((x1-x2)**2 + (y1-y2)**2)**(1/2) < r1+r2:  # 중심과 중심 간 거리 < 반지름의 합
    t.write("작은 원이 큰 원에 걸쳐있습니다.")
else:
    t.write("작은 원이 큰 원의 바깥에 있습니다.")
    

t._screen.exitonclick()