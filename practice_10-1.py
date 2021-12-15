# 1 하나의 레이블과 2개의 버튼을 갖는 GUI 프로그램 만들기

from tkinter import *   

window = Tk()   # 창 만들기
label = Label(window, text="간단한 GUI 프로그램!")  # 텍스트
label.pack()
button1 = Button(window, text="환영합니다") # 버튼
button1.pack()
button2 = Button(window, text="종료")   # 버튼
button2.pack()


window.mainloop()   # 루프 (실행하자마자 바로 꺼지는 것을 방지)