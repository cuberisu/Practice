# 5 0을 입력하기 전까지 정수를 계속 입력받아 더하는 프로그램

sum = 0
num = int(input("정수를 입력하세요.: "))

while num != 0:     # 0 입력 전까지
    sum += num      # 값을 더하고
    num = int(input("정수를 입력하세요.: "))    # 입력받음

print("합은", sum, "입니다.")   # 0 입력받으면 sum값 그대로 출력하기