class Unit:
    def __init__(self, name, hp, speed): #__init__ 생성자 개체를 만들때 자동을 호출
        self.name = name
        self.hp = hp
        self.speed = speed
        
        # print("{} 유닛이 생성 되었습니다.".format(self.name))

    def move(self, location):
        print("[지상유닛이동]")
        print("{} : {} 방향으로 이동합니다. [속도 {}]".format(self.name, location, self.speed))

        


# marine1 = Unit("마린", 40, 5) # Unit Class의 인스턴스
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {}, 공격력 : {}".format(wraith1.name, wraith1.damage)) # class내의 멤버 변수로 접근


# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{}는 현재 클로킹 상태입니다. ".format(wraith2.name))

class AttackUnit(Unit): #상속받고싶은 class를 ()안에 적으면 그 클래스의 변수를 사용가능
    def __init__(self, name, hp, speed, damage): #__init__ 생성자 개체를 만들때 자동을 호출
        # self.name = name  #Unit class에서 상속받아서 정의해줄 필요가 없음
        # self.hp = hp      #Unit class에서 상속받아서 정의해줄 필요가 없음
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다.[공격력 {}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))


firebat1 = AttackUnit("파이어뱃",50, 5, 16)
firebat1.attack("5시")

firebat1.damaged(25)
firebat1.damaged(25)


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
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# vulture = AttackUnit("벌쳐", 80, 10, 20)

# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")



# pass

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # 일단은 넘어가자는 내용   

supply_depot = BuildingUnit("서플라이디폿", 500, "7시")


# class Unit:
#     def __init__(self):
#         print("Unit 생성자")

# class Flyable:
#     def __init__(self):
#         print("Flyable 생성자")

# class FlyableUnit(Flyable, Unit):
#     def __init__(self):
#         # super().__init__()
#         Unit.__init__(self)
#         Flyable.__init__(self)

# dropship = FlyableUnit()
