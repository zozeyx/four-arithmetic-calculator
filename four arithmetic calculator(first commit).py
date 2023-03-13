import sys

print("사칙연산 계산기 입니다.")
print("원하시는 계산식이 있다면 '숫자' + '부호' + '숫자'를 입력해주시길 바랍니다.")
print("Ex) 8 + 9 를 입력하면 정답 : 8 + 9 = 17이 뜹니다.")
print("만약 계산기를 끝내고 싶다면 숫자 '나가기'를 입력해주시길 바랍니다.")
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

    