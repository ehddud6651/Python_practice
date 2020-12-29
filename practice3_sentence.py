# 문자열


sentence = "나는 소년입니다."
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 직장인이고
회사의 노예입니다.
"""
print(sentence3)

# 슬라이싱 

jumin = "990120-1234567"

print("성별 : " + jumin[7]) # index의 7번째 값을 가져왔습니다
print("연 : " + jumin[0:2]) # 0번부터 2번째 전까지의 2자리수를 자여옵니다
print("월 : " + jumin[2:4]) # 2번 부터 4번 직전까지의 수를 가져옵니다
print("일 : " + jumin[4:6]) # 4번 부터 6번 직전까지의 수를 가져옵니다.
print("생년월일 : " + jumin[0:6])
print("생년월일 : " + jumin[:6]) # 위와 동일 
print("뒤 : " + jumin[7:14])
print("뒤 : " + jumin[7:])
print("뒤 : " + jumin[-7:]) # 맨뒤에서 부터 -7번째 부터 맨뒤 끝까지 


# 문자열 처리함수 
python = "Python is Amazing"
print(python.lower()) # 소문자로 바꿈
print(python.upper()) # 대문자로 바꿈
print(python[0].isupper()) # 대문자 참 거짓 확인 
print(len(python)) # 문자열 길이 확인
print(python.replace("Python", "Java")) #문자 대체 

index = python.index("n") # 해당 문자 위치 확인
print(index)
index = python.index("n", index + 1) # 앞에서 찾은 문자열 다음부터 위치 찾음
print(index)
print(python.find("n"))
print(python.find("Java")) # 없으면 -1 나옴
# print(python.index("Java")) # 없으면 오류가 나옴
print(python.count("n")) # n 사용된 횟수

print("a", "b")

# 문자열 포맷
# 방법 1
print("나는 20살 입니다.")
print("나는 %d살 입니다." % 20) # d 정수
print("나는 %s을 좋아합니다." % "파이썬") # s 문자열 
print("Apple은 %c로 시작해요" % "A") # 문자

# %s 는 모두 가능 
print("나는 %s살 입니다." % 20) # d 정수
print("나는 %s과 %s을 좋아합니다." % ("빨간색", "파란색")) # s 문자열 
print("Apple은 %s로 시작해요" % "A") # 문자

#방법2 

print("나는 {}살입니다.".format(22))
print("나는 {}과 {}을 좋아합니다.".format("빨간색", "파란색"))
print("나는 {0}과 {1}을 좋아합니다.".format("빨간색", "파란색")) # 0 = 첫번쨰, 1 = 두번째
print("나는 {1}과 {0}을 좋아합니다.".format("빨간색", "파란색")) # 0 = 첫번쨰, 1 = 두번째

#방법3

print("나는 {age}살이고 {color}색을 좋아합니다.".format(age = 20, color = "빨간"))

#방법4

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아합니다.")


# 탈출문자
#\n 줄바꿈
print("백문이 불여일견 \n백견이 불여일타")
#\"문장에 큰따움표 출력 \"
print("저는 \"김동영\"입니다.")
# \\ = \출력
# \r = 커서를 맨 앞으로 이동 
# \b = 백스페이스 한 글자 삭제
# \t = 탭 여러칸 띄우기

# 퀴즈
#사이트 별로 비밀번호를 만들어 주는 프로그램을 작성하시오 
# 예) http://naver.com
#규칙 1: http://부분은 제외 => naver.com
#규칙 2: 처음 만나는 점(.) 이후 부분은 제외 => naver
#규칙 3: 남은 글자 중 처음 세자리 + 글자개수 + 글자 내 'e' 개수 + "!" 로 구성 
#                   nav                 5               1           !
#생성된 비밀번호 : nav51!


address = "http://daum.com"

address = address.replace("http://", "")  # 대체 = 빈칸으로 대체해서 삭제 
print(address)
address = address[:address.index(".")]
print(address)
address_passwrd = address[0:3]

lengh = len(address)
print(lengh)
count_e = address.count("e")
print(count_e)

print(address_passwrd + str(lengh) + str(count_e) + "!")
password = address_passwrd + str(lengh) + str(count_e) + "!"

print("{}의 패스워드는 {}입니다." .format(address, password))