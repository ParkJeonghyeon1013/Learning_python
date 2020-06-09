#human 클래스
class human:
    def character(self,name,HP,MP):
        self.name = name
        self.HP = HP
        self.MP = MP

    def meet (self):
        print("안녕하세요?")

#enemy 클래스
#DP 속성
class enemy(human):
    def __init__(self, DP):
        self.DP = DP

#player 클래스
#human 상속 / AD / att 메소드: (player AD - enemy DP)만큼 enemy.HP 감소
class player(human):
    def __init__(self, AD):
        self.AD = AD

    def att(self, enemy):
        enemy.HP = enemy.HP - (self.AD - enemy.DP)

#NPC 클래스
#Human meet 메소드를 오버라이딩 해서 "반갑습니다."
class NPC(human):
    def meet(self):
        print("반갑습니다!")

player = player(30)
enemy = enemy(10)

player.character("플레이어", 100, 100)
enemy.character("적", 100, 100)

while True:
    user = input("1-시작, 2-전투 \n")
    if user == "1":
        player.meet()
        NPC.meet(NPC)
    elif user == '2':
        player.att(enemy)
        if enemy.HP == 0:
            print("전투가 종료됩니다.")
            break
