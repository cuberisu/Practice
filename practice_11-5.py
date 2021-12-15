# 5 data.txt ... 실수값들을 읽어서 합계와 평균을 계산하기
inFileName = input("입력 파일 이름: ")
outFileName = input("출력 파일 이름: ")
infile = open(inFileName, "r")
outfile = open(outFileName, "w")
total = 0.0
count = 0
line = infile.readline()
while line != "" :
    value = float(line)
    total = total + value
    count = count + 1
    line = infile.readline()
outfile.write("합계="+ str(total)+"\n")
avg = total / count
outfile.write("평균="+ str(avg)+"\n")
infile.close()
outfile.close()