# 리스트

subway = ["유재석", "조세호", "박명수"]

print(subway.index("조세호")) # 몇번쨰에 탓는가?

subway.append("하하") # 마지막에 추가
print(subway)

# 정현돈을 유재석 / 조세호 사이에 태워봄 
subway.insert(1,"정형돈")
print(subway)

#지하철 사람을 뒤에서 한몀씩 꺼냄
print(subway.pop()) # 맨 뒤의 값을 빼냄 리스트에서 사라짐
print(subway) # 맨뒤에 값은 팦되어 삭제 되었고 

# print(subway.pop()) # 맨 뒤의 값을 빼냄 리스트에서 사라짐
# print(subway) # 맨뒤에 값은 팦되어 삭제 되었고 

# print(subway.pop()) # 맨 뒤의 값을 빼냄 리스트에서 사라짐
# print(subway) # 맨뒤에 값은 팦되어 삭제 되었고 


# 리스트에 같은 값이 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))


# 정렬
num_list = [4,2,3,1]
num_list.sort()
print(num_list)

# 정렬 뒤집기 가능 
num_list.reverse()
print(num_list)

# 모두 지우기
# num_list.clear()
# print(num_list)

# 다야한 자료형과 함께 사용가능 
mix_list = ["조세호", 1 , True]
print(mix_list)

# 리스트 확장 
num_list.extend(mix_list)
print(num_list)


# 키 할당 
# cabinet = {3: "유재석", 100: "김태호"} # 키번호: 할당 내용
# print(cabinet[3])
# print(cabinet.get(3))

# print(cabinet[5]) 에러가 발생하고 실행이 멈춤 
# print(cabinet.get(5)) 에러가 발생하고 None일 출려되고 계속 실행
# print(cabinet.get(5, "사용가능")) 키값 5에 값이 없으면 뒤에 값인 사용가능이 나옴


cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님 
print(cabinet)
cabinet["A-3"] = "김종국" # 유재석 값이 빠지고 김종국으로 업데이트
cabinet["C-20"] = "조세호"
print(cabinet)

# 값 삭제

del cabinet["A-3"]
print(cabinet)

# 현재 키 값들만 확인 
print(cabinet.keys())

# 현재 밸류 값들만 확인 
print(cabinet.values())

# 현재 키, 밸류 값들 확인 
print(cabinet.items())

# 세트 집합이고 순서가 없음 중복 안됨
my_set = {1, 2, 3, 3, 3}
print(my_set)


# 교집합
Java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

print(Java & python)
print(Java.intersection(python))

# 합집합
print(Java | python)
print(Java.union(python))

# 차집합
print(Java - python)
print(Java.difference(python))

# 세트에 추가
python.add("김태호")
print(python)

# 세트에서 삭제
Java.remove("김태호")
print(Java)

#자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

# 퀴즈 당신의 학교에서는 파이썬 코딩 대회를 주최합니다. 
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다.
# 댓글 참석자들 중에서 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다. 
# 조건 1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정 
# 조건 2: 댓글 내용과 상관업이 무작위로 추첨하되 중복 불가 
# 조건 3: random 모듈과 shuffle 과 sample 을 활용

from random import * 

users = range(1, 21)
users = list(users)

print(users)
shuffle(users)
print(users)

winners = sample(users, 4)

print(" -- 당첨자 발표 --")
print("치킨 당첨자 {}".format(winners[0]))
print("커피 당첨자 {}".format(winners[1:]))
print(" -- 축하합니다. --")
