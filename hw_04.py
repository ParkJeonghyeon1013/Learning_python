word = "i want airpot pro but i do not have money so i can not buy airpot"

#word의 문장을 중복되지 않고 정렬된 단어들의 모음으로 만들어주세요.
#리스트로 변환해서 정렬이 아니라 그냥 set만 해주면 되는건가? // 왜 none이 뜨지

word = word.split()

word = set(word)
print(word)
a = list(word)

#print(a)
#print(list(map(str,word)))
#print(a.sort())

#c = [1,4,2,3,100]
#print(c.sort())


#위에서 수행한 단어들의 모음에서 가장 앞에 있는 단어를 아래 딕셔너리의 키값으로 넣어주세요.
#만약 일치하는 단어가 없다면 "그런 단어 없음"이 출력되어야 합니다.

dict = {"airpot" : "비싸다", "buz" : "좀 싸다", "akg N400" : "17만원주고 이거 샀당"}

dict[a[0]] ="가장 앞에 있는 단어"
dict[a[1]] ="그런 단어 없음"
dict[a[2]] ="그런 단어 없음"
dict[a[3]] ="그런 단어 없음"
dict[a[4]] ="그런 단어 없음"
dict[a[5]] ="그런 단어 없음"
dict[a[6]] ="그런 단어 없음"
dict[a[7]] ="그런 단어 없음"
dict[a[8]] ="그런 단어 없음"
dict[a[9]] ="그런 단어 없음"
dict[a[10]] ="그런 단어 없음"
dict[a[11]] ="그런 단어 없음"
dict["airpot"] = "비싸다"

print(dict.items())

#키값에 해당하는 밸류값을 print에 넣어 출력해주세요.
print(dict.values())
