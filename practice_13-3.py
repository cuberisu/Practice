import turtle
lee = turtle.Pen()
park = turtle.Pen()

lee.shape("turtle")
lee.fd(100)
lee.rt(90)
lee.fd(20)
lee.lt(90)
lee.fd(100)

park.shape("circle")
park.fd(-100)
park.rt(90)
park.fd(-20)
park.lt(90)
park.fd(-100)

turtle.Pen()._screen.exitonclick()