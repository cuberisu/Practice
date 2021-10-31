# 5 난수 사용

import random   # 난수 생성 모듈
x = random.randint(1, 100)  # 1~100 난수1 x
y = random.randint(1, 100)  # 난수2 y

ans = int(input(str(x)+"-"+str(y)+" = "))
# 형변환하여 문자열들을 더하면 x-y = 가 출력된다.

if ans == x-y:  # 입력값이 정답이면
    print("정답입니다.")
else:   # 오답이면
    print("틀렸습니다.")