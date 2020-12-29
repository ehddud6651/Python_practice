# weather = input("오늘 날씨는 어때요?")

# if weather == "비" or "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")   


# temp = int(input("기온은 어떄요?"))
# if 30 <= temp :
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp <= 30 :
#     print("괜찮은 날씨에요")
# elif 0 <= temp and temp <= 10 :
#     print("외투를 챙기세요")
# else :
#     print("너무 추워요 나가지 마세요")    


# for 반복문 

# for Waititng_no in [0, 1, 2, 3, 4]:
#     print("대기번호 : {0}".format(Waititng_no))

# for Waititng_no in range(5):
#     print("대기번호 : {0}".format(Waititng_no))


# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))


# while 반복문 

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 주문되었습니다. {1}번 남았어요".format(customer, index)) 
#     index -= 1
#     if index == 0 :
#         print("커피는 폐기처분되었습니다.") 

# customer = "아이언맨"
# index = 1
# while True:
#      print("{0}, 커피가 주문되었습니다. {1}번 남았어요".format(customer, index))
#      index += 1

# customer = "토르"
# person = "Unknown"

# while person != customer :
#       print("{0}, 커피가 주문되었습니다. {1}번 남았어요".format(customer, index))


# customer = "토르"
# person = "Unknown"

# while person != customer :
#       print("{0}, 커피가 주문되었습니다.".format(customer))
#       person = input("이름이 어떻게 되나요?")


# break continue

# absent =  [2, 5]
# no_book = [7]
# for student in range(1,11):
#       if student in absent:
#             continue # continue를 맞나면 다음 문장을 실행하지 않고 돌아감
#       elif student in no_book:
#             print("오늘 수업은 여기까지. {0}는 교무실로 따라와".format(student))
#             break # break만나면 그냥 실행 중지 
#       print("{0}, 책을 읽어봐".format(student))
      

# 한줄 for
# students = [1,2,3,4,5]
# students = [i+100 for i in students]
# print(students)

# #단어의 길이
# students = ["iron man", "thor", "i am groot"]
# # students = [len(i) for i in students]
# print(students)
# students_1 = [i.upper() for i in students]
# print(students_1)


# 퀴즈
from random import * 
num = range(1,51)
cnt =0 # 탑승한 사람의 수를 세아리기 위해 저장할 변수
for i in num:
      time = randint(5,50)
      if time >= 5 and time <=15 :
            print("[0] {}번째 손님 (소요시간 : {}분)".format(i,time))
            cnt += 1 
      else:
            print("[ ] {}번째 손님 (소요시간 : {}분)".format(i,time))

print(" 총 탑승 승객 : {0} 명".format(cnt))