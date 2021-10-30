# 1 정수를 입력받아 합, 차, 곱, 평균, 큰수 작은수를 계산하여 출력
# 파이썬이 제공하는 내장함수 max(x, y), min(x, y) 활용

x = int(input("정수1: "))
y = int(input("정수2: "))

print("두 수의 합:", x+y)
print("두 수의 차:", x-y)
print("두 수의 곱:", x*y)
print("두 수의 평균:", (x+y)/2)
print("큰 수:", max(x, y))
print("작은 수:", min(x, y))
