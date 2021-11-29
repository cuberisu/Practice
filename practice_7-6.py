# 6 두 정수를 입력받아 수학문제 만들기
def question(num1, num2):   # num1 = a, num2 = b가 된다.
    # num1 = int(input("첫 번째 정수: "))
    # num2 = int(input("두 번째 정수: ")) 귀찮은데 매개변수로 하래요!
    ans = int(input("정수 " + str(num1) + " + " + str(num2)+" 의 합은? "))
    if ans == num1 + num2:
        print("정답입니다.")
    else:
        print("틀렸습니다.")

a = int(input("첫 번째 정수: "))
b = int(input("두 번째 정수: "))
question(a, b)  # a와 b가 인수가 된다.