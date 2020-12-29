from random import*
class Unit:
    def __init__(self, name, hp, speed): #__init__ 생성자 개체를 만들때 자동을 호출
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{} 유닛이 생성되었습니다.".format(self.name))
        
        # print("{} 유닛이 생성 되었습니다.".format(self.name))

    def move(self, location):
        print("{} : {} 방향으로 이동합니다. [속도 {}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))


class AttackUnit(Unit): #상속받고싶은 class를 ()안에 적으면 그 클래스의 변수를 사용가능
    def __init__(self, name, hp, speed, damage): #__init__ 생성자 개체를 만들때 자동을 호출
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다.[공격력 {}]".format(self.name, location, self.damage))


class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1 ,5)

    def  stimpack(self):
        if self.hp >10 :
            self.hp -= 10
            print("{} : 스팀팩을 사용합니다. (HP 10 감소".format(self.name))
        else:
            print("{} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        if self.seize_mode == False:
            print("{} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False
    
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name,location):
        print("{} : {} 방향으로 날아갑니다. [속도 {} ]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드는 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)


class wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked ==  True:
            print("{} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{} : 클로킹 모드를 설정합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을시작합니다.")

def game_over():
    print("Player : GG.")
    print("[Player] 님이 게임을 나갔습니다.")

#게임 시작
game_start()
#유닛 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()
t1 = Tank()
t2 = Tank()
w1 = wraith()
#유닛 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)
#유닛 이동
for unit in attack_units:
    unit.move("1시")
#시즈모드 개발    
Tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

#공격모드준비 탱크 시즈 레이스 클러킹 마린 스팀팩
for unit in attack_units:
    if isinstance(unit, Marine): # 인스턴스를 비교하여 확인  인스턴스가 마린인가요? 맞으면 아래로
        unit.stimpack()
    elif isinstance(unit, Tank): # 인스턴스가 탱크인가요 맞으면 아래로
        unit.set_seize_mode()
    else:
        unit.clocking()


# 전군 공격
for unit in attack_units:
    unit.attack("1시")


# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5,21))

#게임 종료
game_over()