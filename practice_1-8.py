# turtle graphics: 펜 떼기

import turtle
t = turtle.Pen()
t.shape("turtle")
t.fd(100)
t.up()  # 펜 들기. 펜을 종이에서 뗀다는 뜻이다
t.goto(0, 200)  # (0, 200) 좌표로 이동. up()을 호출하지 않으면 goto()좌표까지 선이 그어진다
t.down()    # 펜 내려놓기. 펜을 종이에 댄다는 뜻이다
t.fd(100)   # (0, 200) 좌표에 100픽셀의 직선이 그려진다
t._screen.exitonclick()