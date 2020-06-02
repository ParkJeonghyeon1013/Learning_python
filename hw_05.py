능별로 함수로 만들고 계산결과는 txt파일에 저장되도록 만드는거입니다!
while True:
    print("E를 누르면 종료되고 C를 누르면 재입력이 가능합니다")
    qes = input("원하는 계산식을 입력하시오: ")

# C / E 일때 작동방식 저장
    if qes == 'c' or qes == 'C':
        print("다시 입력하세요")
        continue

    if qes == 'e' or qes == 'E':
        print("종료됩니다.")
        break

# 사칙연산 계산식
    if '+' in qes:
        numA, numB = qes.split("+")
        print(numA, numB)
        calc_mark = '+'

    elif '-' in qes:
        numA, numB = qes.split("-")
        print(numA, numB)
        calc_mark = '-'

    elif '*' in qes:
        numA, numB = qes.split("*")
        print(numA, numB)
        calc_mark = '*'

    elif '/' in qes:
        numA, numB = qes.split("/")
        print(numA, numB)
        calc_mark = '/'

    else:
        print("연산자 오류. 다시 입력하세요.")
        continue

# 공백이 있는 부분 삭제
    numA = numA.strip()
    numB = numB.strip()

# 'isdigit'는 숫자 판별 함수로 True, False 반환
    if not numA.isdigit() or not numB.isdigit():
        print("숫자 오류. 다시 입력하세요.")
        continue

# 계산 결과 출력
    if calc_mark == '+':
        answer = int(numA)+int(numB)
        print(str(numA)+str(calc_mark)+str(numB)+"에 대한 결과값은 "+str(answer))

    if calc_mark == '-':
        answer = int(numA)-int(numB)
        print(str(numA)+str(calc_mark)+str(numB)+"에 대한 결과값은 "+str(answer))

    if calc_mark == '*':
        answer = int(numA)*int(numB)
        print(str(numA)+str(calc_mark)+str(numB)+"에 대한 결과값은 "+str(answer))

    if calc_mark == '/':
        answer = int(numA)/int(numB)
        print(str(numA)+str(calc_mark)+str(numB)+"에 대한 결과값은 "+str(answer))