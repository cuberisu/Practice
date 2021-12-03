# 2 주사위값 빈도
# 리스트를 사용

import random

counters = [0, 0, 0, 0, 0, 0]  # 여기에 빈도를 저장하라고 함

for i in range(1000):
    value = random.randint(0, 5)    # 리스트에 접근하기 위해 주사위 눈을 0부터 시작
    counters[value] += 1    # 인덱스로 항목에 접근하여 +1

for j in range(6):
    print(j+1,":", counters[j]) # 주사위 눈 : 빈도수


