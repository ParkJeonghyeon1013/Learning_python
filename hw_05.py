#사칙연산 함수 만들기
def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

#무한루프 계산기
while True:
    qes = input("원하는 계산식을 입력하시오: ")

#띄어쓰기 있을 때 분리
    space_qes = qes.split()

    if space_qes[0] == "c" or space_qes[0] == "C":
        print("다시 입력하세요")
        continue

    if space_qes[0] == "e" or space_qes[0] == "E":
        print("계산기가 종료됩니다")
        break

    if space_qes[1] == "+":
        numA = int(space_qes[0])
        numB = int(space_qes[2])
        answer = sum(numA, numB)
        print(qes + " = %d"%answer)

    if space_qes[1] == "-":
        numA = int(space_qes[0])
        numB = int(space_qes[2])
        answer = sub(numA, numB)
        print(qes + " = %d"%answer)

    if space_qes[1] == "*":
        numA = int(space_qes[0])
        numB = int(space_qes[2])
        answer = mul(numA, numB)
        print(qes + " = %d"%answer)

    if space_qes[1] == "/":
        numA = int(space_qes[0])
        numB = int(space_qes[2])
        answer = div(numA, numB)
        print(qes + " = %d"%answer)


 #       print(qes+"="+answer)

# 띄어쓰기 없을 때 분리
    add_qes1 = qes.split("+")
    minus_qes1 = qes.split("-")
    mulit_qes1 = qes.split("*")
    divi_qes1 = qes.split("/")




#print(add_qes)

#입력받은 숫자 분리


#print("번호는?")
#print(q+"="+a)