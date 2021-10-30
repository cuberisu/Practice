# 7 time() 함수 써서 지금 몇시몇분인지 구하기

import time     # time 모듈 불러와서 time() 쓸 수 있게 하기
# time()은 1970 01 01 이후 흘러온 전체 초를 반환함
fseconds = time.time()   # 이 값은 float이다

# 현재 시각은 24시, 60분을 넘겨 표시할 수 없음
nowhrs = int((fseconds//(60*60))%24)
if nowhrs > 12:     # 12시간 표기 형식
    nowhrs -= 12
    nowhrs = "오후 " + str(nowhrs)
elif nowhrs == 12:
    nowhrs = "오후 " + str(nowhrs)
elif nowhrs < 12:
    nowhrs = "오전 " + str(nowhrs)
    
nowmnts = int((fseconds//60)%60)

print("현재 시각(GMT):", nowhrs+"시", str(nowmnts)+"분")
