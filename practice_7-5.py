# 5 happyBirthday() 함수 작성
# 이름 입력, 생축 노래 출력

def happyBirthday(name):
    print("Happy Birthday to you!\n"*3) # 문자열 곱하기 3 = 3번 출력
    print("Happy Birthday, dear", name) # 이게 바로 "매개변수" 라는 거다.
    print("Happy Birthday to you!")     # user이 name 역할을 한다.

user = input("이름을 입력하시겠어요? ")
happyBirthday(user)
