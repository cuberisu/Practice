# 7 PI = 3.14를 전역변수로 하여 원에 대한 함수 작성
# 면적 circleArea(radius), 둘레 circleCircumference(radius)

PI = 3.14

def circleArea(r):
    area = PI * r**2    # 전역변수를 갖다 쓴 거다.
    print(area)     # 만약 return으로 했다면.. 함수 호출만 하면 값이 출력은 안 된다.
                    # return값을 출력하고 싶으면 print(함수명(인수)) 하면 된다.

def circleCircumference(r):
    ccf = 2 * PI * r    # 이것도.
    print(ccf)


circleArea(12)  # 3.14 * 144 = 452.16
circleCircumference(12) # 3.14 * 24 = 75.36
# 결과가 잘 나옴!!!
