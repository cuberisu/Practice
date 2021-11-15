# 2 잘못된 점 찾기
year = 0
balance = 1000

while balance <= 2000:  # 조건이 잘못됨. >=를 <=로 고쳐야 함.
    year = year + 1
    interest = balance * 0.07
    balance = balance + interest
    
print(year, "년이 걸립니다.")
