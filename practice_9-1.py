# 1 입력받은 숫자를 리스트에 저장하여 평균 출력

nums = []   # 공백 리스트

for i in range(5):  # 5번 반복
    n = int(input("정수를 입력하세요: "))
    nums.append(n)   # 리스트에 추가하는 함수 append()

sum = 0
for j in range(5):  # 귀찮아서 반복문
    sum += nums[j]  # 리스트의 요소들을 더하기

avg = sum/len(nums) # len()은 리스트의 크기(요소의 개수)

print("평균은", avg, "입니다.")


