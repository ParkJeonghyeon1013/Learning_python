# 과제 2-1 공백2개를 1개로 바꾸고 :는 ,로 바꾼다. 단, 모든 함수는 1번만 사용가능

a = 'My  naMe  is  Son  Chang  Ha:  my  pin  is  000125-3!!!!!!.'

b = a.split()
c = ' '.join(b)
c_1 = c.strip()

print("과제 2-1:",c_1.replace(':',','))

# 과제 2-2 naMe를 소문자로 바꾸고 뒤에 있는 my를 My로 바꿔라.

d = (b[0] , b[1].lower() , b[2] , b[3] , b[4] , b[5] , b[6].replace('my','My') , b[7], b[8], b[9])
e = ' '.join(d)
e_1 = e.strip()
print("\n과제 2-2:",e_1)

# print(a.lower())
# print(a.replace('my','My'))

# 과제 2-3 주민번호를 뒷자리 1자리만 남기고 지워라
#f = b[9]
#g = f[]

f = a.replace('!','\0')
print("\n과제 2-3:",f)

# strip 사용하면 strip('') 를 통해 지우기 원하는거 삭제 가능
