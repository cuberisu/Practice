# 1 Error 고치기
print("나는"+str(12)+"개의 사과를 먹었다.")

# 2 문자열과 숫자와의 연산(결과 예측하기)
print("apple"+"apple")  # appleapple
print("apple"*3)    #appleappleapple

# 3 입력받은 문자열 중 특정 위치 글자를 추출하기
data = input("문자열을 입력하세요: ")
print(data[0:2] + data[-2:])    
# data에 저장된 문자열 중 왼쪽부터 1,2번째 문자 + 오른쪽부터 1, 2번째 문자 출력하기

# 4 특정 문자열을 더하여 출력하기
data = input("문자열을 입력하세요: ")
print(data+"하는 중")

# 5 입력받은 기호 사이에 문자열을 집어넣기
symbol = input("기호를 입력하세요(2개): ")
data = input("중간에 삽입할 문자열을 입력하세요: ")
print(symbol[0:1] + data + symbol[-1:])

# 6 4개의 숫자가 든 리스트의 숫자를 꺼내서 그 합계를 출력
arr = [1,2,3,4]
print("리스트 숫자들의 합 =", arr[0]+arr[1]+arr[2]+arr[3])  
# 파이썬은 저절로 리스트 원소를 숫자로 인식한다