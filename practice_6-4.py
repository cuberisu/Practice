# 4 곱셈 퀴즈 - 정답이 입력될 때까지 반복하기
import random
num1 = random.randint(1,10)
num2 = random.randint(1,10)
# 1이상 10이하 범위 내 정수 난수 생성

answer = int(input(str(num1)+"*"+str(num2)+"= "))
# input()에는 최대 1개 argument만 들어갈 수 있다. 
# 콤마(,)로 연결하지 말고 덧셈 연산자(+)로 연결하자.

while answer != num1*num2:  # 오답이 입력되면 다시 출력
    answer = int(input(str(num1)+"*"+str(num2)+"= "))
print("정답입니다.")    # 정답이 입력되면 while을 탈출해서 출력
