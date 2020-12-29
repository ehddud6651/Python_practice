# import sys

# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)


# print("Python" + "java")
# print("Python", "java", "javaScript", sep=" vs ") # sep 사이에 넣기
# print("Python", "java", "javaScript", sep=",", end="?") # 줄바꿈없이 계속
# print("무엇이 더 재밌을까요")


# scores = {"수학":0, "영어":0, "코딩":100}
# for subject, score in scores.items():
#     # print(subject,score)
#     print(subject.ljust(8),str(score).rjust(4), sep=":") # 8개의 공간을 확보하고 왼쪽정렬 / 4개의 공간을 확보하고 우로 정렬

# # 은행 대기표
# for num in range(1,21):   
#     print("대기번호 : "+ str(num).zfill(3)) # 3칸에서 비워져있는 칸에 0을 채워넣는다

# 표준 입력
# answer = input("아무 값이나 입력하세요 : ")
# print(type(answer)) # 항상 문자열 str 형태로 나옴
# print("입력하신 값은 " + answer + "입니다.")

# #빈자리는 빈공간으로 두고 오른쪽 정렬을 하되 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 땐 +로 표시 음수일때 - 표시 
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고 빈칸으로 _로 채움
# print("{0:_<10}".format(500)) 
# # 3자리마다 콤마로 찍어주기
# print("{0:,}".format(1000000000))
# # 3자리마다 콤마로 찍어주기 + +-부호도 붙이기
# print("{0:+,}".format(1000000000))
# print("{0:+,}".format(-1000000000))
# # 3자리마다 콤마로 찍어주기 + +-부호도 붙이기 + 자리수 확보 + 빈자리는 ^ 표시
# print("{0:^<+30,}".format(100000000))
# # 소수점출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자리수(여기서는 소수점 2자리수) 까지만 표시 (소수점 3째 자리에서 반올림)
# print("{0:.2f}".format(5/3))

# # 파일 입출력 w 덮어쓰기 a 이어쓰기 r읽어오기
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close() #항상 닫아줘야함

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80") # 줄바꿈이 안됨
# score_file.write("\n코딩 : 100") #\n 줄바꿈이 됨

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) # 한줄만 읽어오고 커서가 다음줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# print(score_file.readline(), end="") # 줄바꿈 하기 싫으면
# print(score_file.readline(), end="") # 줄바꿈 하기 싫으면

# 리스트로만들어서 저장

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end="")

# score_file.close()


# import pickle
# profile_file = open("profile.pickle","wb") # w 쓰기 b 바이너리
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# profile_file
# pickle.dump(profile, profile_file) #profile에 있는 정보를 file
# profile_file.close()

# profile_file = open("profile.pickle", "rb") # 읽어오기
# profile = pickle.load(profile_file) #파일에 있는 정보를 변수에 불러오기
# print(profile)
# profile_file.close()


# with 파일을 open후 close 하지 않아도 되는 간단하게 파일을 쓰고 불러올수 있음
# with open("study.txt", "w", encoding="utf8") as study_file: # study_file에 write 하겠다
#     study_file.write("파이썬을 열심히 공부하고 있어요")


# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())


# 퀴즈
for i in range(1,51):
    with open("{}주차.txt".format(i) , "w", encoding="utf8") as report_file:
        report_file.write("- {} 주차 주간보고 -".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")

