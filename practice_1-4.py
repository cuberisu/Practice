# 4 turtle graphics: 주어진 그림 (직진과 회전)

import turtle   # turtle 모듈 불러오기
t = turtle.Pen()    # t라는 변수가 거북이가 된다
t.shape("turtle")   # 커서를 거북이 모양으로 한다
t.forward(100)  # 100픽셀 전진
t.left(90)      # 왼쪽으로 90도 회전
t.forward(100)
t.right(90)     # 오른쪽으로 90도 회전
t.forward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)

t._screen.exitonclick()     # 클릭해야 종료