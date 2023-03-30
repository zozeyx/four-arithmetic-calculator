import sys

print("업데이트!")
print("Update!")
print("이제 한글버전과 영어버전이 생겼습니다! 원하는 버전 숫자를 입력해 엔터를 누르시면 됩니다!")
print("Now we have a Korean version and an English versions! Enter the desired version number and press Enter!")
print("만약 계산기를 나가고싶다면 '0'을 입력하시면 됩니다.")
print("If you want to turn off the calculator, you can enter '0'.")
print("0 나가기(exit)")
print("1 한글버전(Korean version)")
print("2 영어버전(English version)")

version = int(input("숫자입력 : "))

if version == 0:
        exit()
elif version == 1:
        print("사칙연산 계산기 입니다.")
        print("원하시는 계산식이 있다면 '숫자' + '부호' + '숫자'를 입력해주시길 바랍니다.")
        print("Ex) 8 + 9 를 입력하면 정답 : 8 + 9 = 17이 뜹니다.")
        data= input("수식을 입력하세요: ").split(' ')
        i = int(data[0])
        j = str(data[1])
        k = int(data[2])
        if j == '+':
                print('정답 : ',str(i),str(j),str(k), '=', i + k)
        elif j == '-':
                print('정답 : ',str(i),str(j),str(k),'=', i - k)
        elif j == 'x':
                print('정답 : ',str(i),str(j),str(k),'=', i * k)
        elif j == '%':
                print('정답 : ',str(i),str(j),str(k),'=', i / k)
        else:
                print("잘못 입력하셨습니다.")
elif version == 2:
        print("It's a four-pronged calculator.")
        print("If you have a desired formula, please enter 'number' + 'sign' + 'number'.")
        print("Ex) Enter 8 + 9 to get the correct answer: 8 + 9 = 17..")
        data= input("Please enter a formula: ").split(' ')
        i = int(data[0])
        j = str(data[1])
        k = int(data[2])
        if j == '+':
                print('Answer : ',str(i),str(j),str(k), '=', i + k)
        elif j == '-':
                print('Answer : ',str(i),str(j),str(k),'=', i - k)
        elif j == 'x':
                print('Answer : ',str(i),str(j),str(k),'=', i * k)
        elif j == '%':
                print('Answer : ',str(i),str(j),str(k),'=', i / k)
        else:
                print("You have entered the wrong one.")

