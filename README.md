# Four-arithmetic-calculator
Four arithmetic calculator(사칙연산 계산기) with python

파이썬을 이용한 사칙연산 계산기

## Update !!
Now you can write the Korean and English versions separately on the calculator!       
(It is available in the four arithmetical calculator second commit file.)

# Functions available on the calculator
* Plus
* Subtract
* multiply
* divide

Other features will be added..

\*And if you enter a character other than a number, the function to display an error message will be added later.\*

### Code
To briefly explain the code,
```python
date = input().split(' ')
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
```
Put the value entered in 'date' into a variable, and the result value depends on which variable is responsible for the symbol.

```python
print("1 한글버전(Korean version)")
print("2 영어버전(English version)")

version = int(input("version : "))
...
if version == 1:
...
elif version == 2:
...
```
Due to this code, it is divided into Korean and English versions.
```python
if version == 1:
...
	else:
     print("잘못 입력하셨습니다.")
if version == 2:
...
	else:
		print("You have entered the wrong one.")
```
This code is output when inputted incorrectly.
