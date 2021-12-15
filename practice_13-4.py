# 4 상속
# Turtle 클래스를 상속받아 MyTurtle 클래스 작성
# MyTurtle: 사각형을 그리는 함수를 Turtle 클래스에 추가하는 클래스

import turtle
class MyTurtle(turtle.Turtle):
    def drawSquare(self):
        for i in range(4):
            self.rt(90)
            self.fd(100)

my_turtle = MyTurtle()
my_turtle.fd(100)
my_turtle.drawSquare()
my_turtle._screen.exitonclick()