# 7장 12페이지: 함수 안에서 전역 변수 변경하기
# 예제의 올바른 코드이다.

def calculate_area(radius):
    global area     # 함수 내에서 전역변수의 값을 변경하고 싶을 때 global
    area = 3.14 * radius**2     # (global 선언과 동시에 =을 쓸 수 없다. 따로 해야함.)
    return      # (이렇게 하면 리턴값이 None인데....?)

area = 0    # 사실 이 줄은 없어도 실행 자체는 된다.

r = float(input("원의 반지름: "))
calculate_area(r)   # 함수를 호출해야 계산이 된다. 안하면 area = 0 이다.
print(area) # 5 입력 시 78.5 나오면 정상이다.


''' 이거는 당연히 0이 출력된다.

def calculate_area(radius):
    area = 3.14 * radius**2    # 새로운 지역변수 area가 선언된 셈이다.
    return  # (사실 이 함수의 리턴값은 0도 아니고 None이다...)

area = 0    # 전역변수. print문은 이 값을 출력하게 된다.

r = float(input("원의 반지름: "))
calculate_area(r)
print(area)   # 전역변수의 값 0이 출력된다.

'''


''' 이거는 None이 출력된다.

def calculate_area(radius):
    area = 3.14 * radius**2
    return  # 0도 아니고 None이 리턴된다. area를 붙이면 이 코드도 정상 작동한다.

area = 0

r = float(input("원의 반지름: "))
print(calculate_area(r))    # 함수의 리턴값이 출력된다.

'''