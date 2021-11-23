# 7 turtle graphics: 눈꽃모양 그리기
import turtle
t = turtle.Pen()
t.shape("turtle")
t.color("blue")

t.lt(30)    # 시작 각도
for i in range(6):   # 6번 반복 (012345)
    t.fd(100); t.fd(-30)    # fd(음수)라고 거북이가 뒤를 돌아보진 않는다.
    t.lt(60); t.fd(30); t.fd(-30); # 세미콜론으로 한 줄에 여러 코드 작성
    t.rt(120); t.fd(30)     # 오른쪽으로 60도 차이나는 각도에서 다음 루프 실행
    t.up()
    t.goto(0,0)
    t.pd()
t.seth(0)   # 거북이 이쁘게 놓기
t._screen.exitonclick()
