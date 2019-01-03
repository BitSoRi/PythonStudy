# Ch. 4 
## 4 - 1 함수

#### Q1 홀수 짝수 판별
주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성하시오.

#### A1
```python
def is_odd(x):
    if x % 2 == 0:
        print('even number')
    elif x % 2 != 0:
        print('odd number')
```

#### Q2 평균값 계산
입력으로 들어오는 모든 수의 평균값을 계산해 주는 함수를 작성해 보자. (단, 입력으로 들어오는 수의 갯수는 정해져 있지 않다.)

#### A2
```python
def total_average(*ag):
    total_sum = 0
    x_count = 0
    for i in ag:
        total_sum = total_sum + i
        x_count += 1
    total_avg = total_sum / x_count
    return(total_avg)    
```

## 4 - 2 사용자 입력과 출력

#### Q1 두 수의 합은?
다음은 두 개의 숫자를 입력받아 더하여 리턴해 주는 프로그램이다.
```python
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)
```
이 프로그램을 수행 해 보자.
```
첫번째 숫자를 입력하세요 : 3
두번째 숫자를 입력하세요 : 6
두 수의 합은 36 입니다
```
3과 6을 입력했을 때 9가 아닌 36이라는 결과가 리턴되었다. 이 프로그램의 오류를 수정하시오.

#### A1
```python
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" % total)
```

#### Q2 숫자의 총합
사용자로부터 다음과 같은 숫자들의 입력을 받아 입력받은 숫자들의 총합을 구하는 프로그램을 작성하시오. (단, 숫자들은 콤마로 구분하여 입력한다.)
```
65, 45, 2, 3, 45, 8
```

#### A3
```python
number_input = input()
number_set = number_input.split(',')
total_sum = 0
for i in number_set:
    total_sum = total_sum + int(i)
print(total_sum)
```

#### Q3 문자영 출력
다음 중 출력결과가 다른 것 한개를 고르시오.
1. ```print("you" "need" "python")```
2. ```print("you"+"need"+"python")```
3. ```print("you", "need", "python")```
4. ```print("".join(["you", "need", "python"]))```

#### A3
```python
print('you' 'need' 'python')
print('you'+'need'+'python')
print('you', 'need', 'python')
print(''.join(['you', 'need', 'python']))
```

#### Q4 한줄 구구단
사용자로부터 2~9 까지의 숫자중 하나를 입력받아 해당 숫자의 구구단을 한줄로 출력하는 프로그램을 작성하시오.
실행 예
```
구구단을 출력할 숫자를 입력하세요(2~9): 2
2 4 6 8 10 12 14 16 18
```

#### A4
```python
def times_table(x):
    for i in range(9):
        print(x * (i + 1), end = ' ')
```


## 4 - 3 파일 읽고 쓰기

#### Q1 파일 읽고 출력하기
다음은 "test.txt"라는 파일에 "Life is too shorot" 라는 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
```python
f1 = open("test.txt", 'w')
f1.wirte("Life is too short")

f2 = open("test.txt", 'r')
print(f2.read())
```
이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다. 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정하시오.

#### A1
```python
f1 = open('test.txt', 'w')
f1.write('Life is too short')
f1.close()

f2 = open('test.txt', 'r')
print(f2.read())
f2.close()
```

#### Q2 파일저장
사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성하시오. (단, 프로그램을 다시 실행하더라도 기존 작성한 내용을 유지하고 새로 입력한 내용이 추가되어야 한ㄷ.)

다음은 실행 예제이다.
```
저장할 내용을 입력하세요:
```
실행 할 때마다 사용자가 입력한 내용이 test.txt 파일에 추가 되어야 한다.

#### A2
```python
new_contents = input()
add_file = open('test.txt', 'a')
add_file.write(new_contents)
add_file.close()

```

#### Q3 역순 저장
다음과 같은 내용의 파일 abc.txt가 있다.
*abc.txt*
```
AAA
BBB
CCC
DDD
EEE
```
이 파일의 내용을 다음과 같이 역순으로 바꾸어 저장하시오.
```
EEE
DDD
CCC
BBB
AAA
```

#### A3
```python
abc = open('abc.txt', 'r')
abc_lines = abc.readlines()
new_abc = open('abc.txt', 'w')
for i in range(len(abc_lines) - 1, -1, -1):
    new_abc.write(abc_lines[i].replace('\n', ''))
    if i == 0:
        break
    new_abc.write('\n')
new_abc.close()
```

#### Q4 파일 수정
다음과 같은 내용을 지닌 파일 test.txt 가 있다.
*test.txt*
```
Life is too short
you need java
```
이 파일의 내용중 java라는 문자열을 python으로 바꾸어서 저장하시오.

#### A4
```python
jav_to_py = open('test.txt', 'r')
jtp_lines = jav_to_py.readlines()
jav_to_py.close()
with open('test.txt', 'w') as new_jtp:
    for i in jtp_lines:
        new_jtp.write(i.replace('java', 'python'))
```

#### Q5 평균값 구하기
다음과 같이 총 10줄로 이루어진 sample.txt 파일이 있다.
*sample.txt*
```
70
60
55
75
95
90
80
80
85
100
```
sample.txt 파일의 숫자값을 모두 읽어 총합과 평균값을 구한 후 평균값을 result.txt라는 파일에 쓰는 프로그램을 작성해 보자.

#### A5
```python
with open('sample.txt', 'r') as data_file:
    data = data_file.readlines()
for i in range(len(data)):
    data[i] = int(data[i].replace('\n', ''))
with open('result.txt', 'w') as result_file:
    result_data = sum(data) / len(data)
    result_file.write(str(result_data))
```
