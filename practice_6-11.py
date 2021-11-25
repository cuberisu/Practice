# 11 turtle graphics: 노랑햇님 그리기
# 코드를 분석하기
# 새로운 함수 익히기

import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("red", "yellow")   # color() 함수는 2개의 인자도 설정 가능. 
                           # color(pencolor, fillcolor)

t.begin_fill()  # Called just before drawing a shape to be filled.
                # No argument.
while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos()) < 1:    # pos() 거북이 좌표 반환(Vec2D), abs() 절댓값 반환(float)
        break   # 제자리로 돌아왔을 때 멈추기
t.end_fill()    # Fill the shape drawn after the call begin_fill().
                # No argument.
t._screen.exitonclick()

print(type(abs(t.pos())))
print(type(t.pos()))