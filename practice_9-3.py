# 3 딕셔너리로 이름과 전화번호를 입력받아 저장하기
# 엔터키를 누르면 검색모드가 되게 하기

phone = {}

def inputmode():
    while True:
        name = input("[입력모드] 이름을 입력하세요.(q: 프로그램 종료): ")
        if not name:
            searchmode()
            break
        if name == "q":
            break
        number = input("[입력모드] 전화번호를 입력하세요.: ")
        phone[name] = number    # list[key] = value -> key와 value를 연결시킴.
                                # 새로운 항목 생성 방법 중 하나.

def searchmode():
    while True:
        search_name = input("[검색모드] 이름을 입력하세요.(q: 프로그램 종료): ")
        if not search_name:
            inputmode()
            break
        if search_name == "q":
            break
        if search_name in phone:    # 에러코드 띄우지 않기 위한 장치!!!!
            print(search_name, "의 전화번호는", phone[search_name])
        else: 
            print("등록된 전화번호가 없습니다.")

inputmode()