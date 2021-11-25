# 12 turtle graphics: sine graph
import turtle, math
t = turtle.Pen()
t.shape("turtle")
t.color("orange")   # 주황색
rad = 0     # 초기 라디안 값

t.write(t.pos())    # 초기 좌표 리턴
t.write("y = sin(200x)  ",align="right")  
# 2번째 인자(opt): 거북이를 기준으로 오른쪽정렬로 함수 표시

for x in range(360):    # sin(x) 1cycle: 360 degrees
    t.goto(x, math.sin(rad)*200)    # y좌표는 라디안으로 함
    rad += math.pi/180
    
    if x % 90 == 0:   # x좌표가 90의 정수배일 때
        t.write(t.pos())    # 현재 좌표 리턴

t.write(t.pos())    # 마지막 좌표 리턴

t._screen.exitonclick()