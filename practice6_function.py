#함수

def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print("입금이 완료되었습니다.  잔액은 {0} 원입니다. ".format(balance + money))
    return balance + money

balance = 0 # 현재 잔액 0원
balance = deposit(balance, 1000) #1000원 입금
print(balance)

def withdraw(balance, money):
    if balance >= money :
        print("출금이 완료 되었습니다. 잔액은 {0}원 입니다.".format(balance-money))
        return balance-money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

# balance = withdraw(balance,500)


# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission

# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {}원이고 잔액은 {}입니다.".format(commission, balance))



# 기본값

# def profile(name,age, main_lng):
#     print("이름: {}\t나이: {}\t주 사용언어: {}".format(name,age,main_lng))


# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")


# def profile(name, age = 17, main_lng = "파이썬"): # 값이 들어오지 않으면 기본값이 나감 17 / 파이썬 
#     print("이름: {}\t나이: {}\t주 사용언어: {}".format(name,age,main_lng))

# profile("유재석")
# profile("김태호")


# 키워드 값 

# def profile(name, age, main_lng): 
#     print(name, age, main_lng)

# profile(name = "유재석", main_lng = "파이썬",age = 20)
# profile(main_lng = "자바",age = 25, name = "김태호")

#가변 인자

#기존방법
# def profile(name, age, lang1, lang2, lang3, lang4, lang5): 
#     print("이름 : {}\t나이 : {}\t".format(name, age),end=" ") # end 사용시 줄바꿈을 하지않고 이어서 작성 
#     print(lang1, lang2,lang3, lang4, lang5)

#가변인자사용
def profile(name, age, *lnaguage): # *을 이용해서 가변인자 사용
    print("이름 : {}\t나이 : {}\t".format(name, age),end=" ") # end 사용시 줄바꿈을 하지않고 이어서 작성 
    for lang in lnaguage:
        print(lang, end=" ")
    print()    

profile("유재석", 20, "파이썬","자바","C","C++","C#","javascript")
profile("김태호", 25, "코틀린","스위프트")


#지역변수 전역변수 

gun = 10

def checkpoint(soldiers): 
    global gun # 전역변수 사용 비추
    gun = gun - soldiers 
    print("함수 내 남은 총: {}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers 
    print("함수 내 남은 총: {}".format(gun))
    return gun # 함수 내의 결과로 gun 변수의 값을 밖으로 빼내줌

print("전체총: {}".format(gun))
# checkpoint(2)
gun = checkpoint_ret(gun,2)
print("전체총: {}".format(gun))


#퀴즈

def std_weight(height, gender):
    if gender == "man":
        man = round(height*height*22*0.0001, 2)    # 소수 둘째 자리 까지 표현
        print("키 {}cm의 {}의 표준 체중은 {}kg 입니다. ".format(height,gender,man))
        return man
    elif gender == "woman":
        woman = round(height*height*21*0.0001, 2) # 소수 둘째 자리까지 표현
        print("키 {}cm의 {}의 표준 체중은 {}kg 입니다. ".format(height,gender,woman))
        return woman 

std_weight(173, "man")