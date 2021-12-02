# 8 사칙연산 수행 함수 작성하기

def plus(num1, num2):
    print(num1, "+", num2, "=", num1+num2)
    
def minus(num1, num2):
    print(num1, "-", num2, "=", num1-num2)
    
def times(num1, num2):
    print(num1, "*", num2, "=", num1*num2)

def divide(num1, num2):
    print(num1, "/", num2, "=", num1/num2)



print("계산기")
print("1. 덧셈  2. 뺄셈  3. 곱셈  4. 나눗셈")
cal = 0
while cal != 1 and cal != 2 and cal != 3 and cal != 4:
    print("1, 2, 3, 4 중 하나를 입력하세요.")
    cal = int(input("원하시는 연산을 선택하세요.: "))

num1 = float(input("첫 번째 실수: "))
num2 = float(input("두 번째 실수: "))

if cal == 1:
    plus(num1, num2)
elif cal == 2:
    minus(num1, num2)
elif cal == 3:
    times(num1, num2)
elif cal == 4:
    divide(num1, num2)