
# 숫자열


# print(2**3) #2의 3제곱
# print(5%3) # 나머지 구하기 2
# print(5//3) # 몫구하기 1
# print(3 == 3) # 같은지 참 거짓 비교 

# print(abs(-9)) #절대값
# print(pow(4,2))
# print(round(3.14)) # 반올림
# print(round(4.9))

from math import *
# print(floor(4.99)) #나머지 내림
# print(ceil(3.8)) # 나머지 올림
# print(sqrt(16)) # 제곱근 


from random import * 
# print(random())  # 0.0 이상 1.0 미만의 임의의값으 생성
# print(random()* 10)
# print(int(random()* 10))
# print(int(random()* 10))
# print(int(random()* 10))
# print(int(random()* 10) + 1) # 1~ 10 이하의 랜덤 값

# 로또 숫자 뽑기 

# print(int(random() * 45 +1))
# print(int(random() * 45 +1))
# print(int(random() * 45 +1))
# print(int(random() * 45 +1))
# print(int(random() * 45 +1))
# print(int(random() * 45 +1))
# print(int(random() * 45 +1))


# print(randrange(1,46)) #1부터 46미만의 임의의 값
# print(randint(1, 45)) #1부터 45이하의 임의의값 

# 퀴즈 월 4회의 스터디를 하는데 3번은 온라인 모임으로 하고 1번은 오프라인으로 하기로 했습니다ㅣ
# 아래 조건에 맞는 오프라인 모임날짜를 정해주는 프로그램을 작성하시오
# 조건 1: 랜덤으로 날짜를 선정하시오
# 조건 2: 월별 날짜는 다름으로 최소일수 28일 이내로 정함
# 조건 3: 매월 1~3일은 스터디 준비를 해야 하므로 제외
# 출력문 예제: 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.


from random import * 

date = int(randint(4, 28))
print("오프라인 스터디 모임 날짜는 매월", date ,"일로 선정되었습니다.")
print("오프라인 스터디 모임 날짜는 매월" + str(date) + "일로 선정되었습니다.")