# 1 2부터 100 사이의 모든 짝수를 출력하는 반복 루프
'''
for문 기본형식: for 변수 in 리스트(또는 문자열, 또는 튜플):
                    들여쓰기

*range(start_no, end_no, step)
- 매개변수가 한개, 두개, 세개가 올 수 있음.
- start_no: 시작값(default=0)
- end_no: 종료값(자신은 포함되지 않음)
- step: 증감 단위(default=1)
'''

# 1째 방법
num = 0
for i in range (0, 50):     
    num += 2
    print(num, end=" ")     
    # for문은 한 바퀴 돌면 자동 개행이 되므로 
    # 공백 한 칸으로 마무리시키는 코드 end=" "

print("\n")

# 2째 방법
for j in range (2, 101):
    if j%2 == 0:    # 짝수 판별 조건문
        print(j, end=" ")

