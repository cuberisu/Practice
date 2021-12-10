# 7 국가별 도메인 딕셔너리
domains = {"kr": "대한민국", "sk": "슬로바키아", "no": "노르웨이", "us": "미국", "jp": "일본", "hu": "헝가리", "de": "독일"}
# dict = {key1: value1, key2: value2, ...}

for k, v in domains.items():    # 괄호 안에 argument는 넣지 않는다.
    print(k, ":", v)

# Python view objects
# items() 함수: key, value 쌍 모두를 가져옴
# keys() 함수: key 모두 가져옴
# values() 함수: value 모두 가져옴

# 2째 방법
# for key in domains.keys():
#     print(key, ":", domains[key])