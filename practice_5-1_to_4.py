# 1 조건문의 개념
# 다음 프로그램의 출력은?
age = 20
if age < 20:    # 20살보다 어리면 이것만 출력됨
    print("20살 미만")
else:           # 20살부터의 나이라면 이것만 출력됨
    print("20살 이상")


# 2 age의 범위 체크하기: 논리연산자
if age >=30 and age <=50:   # 30 <= age <= 50 모두 만족 시 출력
    print("30살 이상 50살 이하")
else:
    print("30살 미만 or 50살 초과")


# 3 입력받은 온도에 따른 조건문
t = int(input("현재 온도: "))
if t >= 25:
    print("반바지를 입으세요.")
else:
    print("긴바지를 입으세요.")
    
    
# 4 입력받은 시험점수에 대응하여 학점(ABCDF) 출력
score = int(input("점수를 입력하세요.: "))
if score >= 90:
    print("A학점입니다.")
elif score >= 80:
    print("B학점입니다.")
elif score >= 70:
    print("C학점입니다.")
elif score >= 60:
    print("D학점입니다.")
else:
    print("F학점입니다.")