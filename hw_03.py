# 3강 과제 1번
# 카드 게임 코드입니다. 주어진 문제를 해결하여 코드를 실행시켜주세요.

#deck의 1은 문자 A로, 11,12,13은 각각 문자 J,Q,K로 바꾸고
#리스트를 4번 반복하여 [a,1, ~~]가 리스트에 4개씩 있도록 바꿔주세요.

deck = [1,2,3,4,5,6,7,8,9,10,11,12,13]

deck[0] = 'A'
deck[10:] = 'J','Q','K'
print(deck)

deck = deck * 4
print(deck)

#이 아래쪽에 5장의 카드를 뽑는 코드를 작성해주세요.
#덱에서 카드 5장을 무작위로 뽑아 card_list에 저장한 후
#print 부분을 수정하여 5장을 모두 출력해주세요.
#뽑힌 카드는 덱에 있어서는 안됩니다. <3이 1장 뽑히면 덱에는 3이 3장만 있어야함.>

card = [1,2,3,4,5,6,7,8,9,10,11,12,13]
card_list = []

import random
random.shuffle(card)
#random.shuffle는 랜덤 클래스에 포함된 리스트를 섞어주는 함수입니다.

#여기에 카드를 뽑는 코드를 작성해주세요.
card_list=[card.pop(),card.pop(),card.pop(),card.pop(),card.pop()]
print("\n카드게임 결과:",card_list)

#+  + 부분의 빈 칸을 채워주세요
print("첫번째 카드는 ",card_list[0],"입니다.")
print("두번째 카드는 ",card_list[1],"입니다.")
print("세번째 카드는 ",card_list[2],"입니다.")
print("네번째 카드는 ",card_list[3],"입니다.")
print("마지막 카드는 ",card_list[4],"입니다.")

#마지막으로 sort함수를 이용하여 덱을 정렬한 후 출력해주세요.
#힌트 : 덱을 바로 정렬하면 오류가 발생합니다. map함수를 구글에 검색하여 이용해보세요.
card.sort()
print(card)
print(list(map(int,card)))
