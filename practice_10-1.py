# 1 하나의 레이블과 2개의 버튼을 갖는 GUI 프로그램 만들기

from tkinter import *

window = Tk()
label = Label(window, text="간단한 GUI 프로그램!")
label.pack()
button1 = Button(window, text="환영합니다")
button1.pack()
button2 = Button(window, text="종료")
button2.pack()


window.mainloop()   