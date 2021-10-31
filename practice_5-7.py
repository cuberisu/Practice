# 7 복권 당첨 상금은?

import random
x = random.randint(0, 9)
y = random.randint(0, 9)
num = input("복권 번호를 2자리로 입력하세요.(00~99): ") # num = num[0] + num[1] (str)

print("당첨번호는", str(x)+str(y),"입니다.")    # xy

if int(num[0]) == x and int(num[1]) == y:   # num = xy
    print("당첨금은 100만원입니다.")
elif int(num[0]) == y and int(num[1]) == x: # num = yx
    print("당첨금은 100만원입니다.")
    
elif int(num[0]) == x and int(num[1]) != y: # num = x*
    print("당첨금은 50만원입니다.")
elif int(num[0]) == y and int(num[1]) != x: # num = y*
    print("당첨금은 50만원입니다.")
elif int(num[0]) != x and int(num[1]) == y: # num = *y
    print("당첨금은 50만원입니다.")
elif int(num[0]) != y and int(num[1]) == x: # num = *x
    print("당첨금은 50만원입니다.")
else:
    print("다음 기회에...")