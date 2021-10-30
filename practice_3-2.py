# 2 원기둥의 부피 계산
import math     # math 모듈 불러와서 math.pi로 파이값을 쓸 수 있음
r = int(input("반지름: "))
h = int(input("높이: "))
print("원기둥의 높이:", math.pi*r**2*h)