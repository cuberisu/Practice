# 1 파일 내 글자 개수 세기
filename = input("파일 이름을 입력하세요: ").strip()
infile = open(filename, "r")    # "r" 읽기모드
count = 0

for line in infile:
    for ch in line:
        count += 1
        
print("파일 안에는 총 ", count , "개의 글자가 있습니다.")
infile.close()