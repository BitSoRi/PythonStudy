# Ch.3
## 3-1 if

#### Q1 조건문1
홍길동씨는 5,000원의 돈을 가지고 있고 카드는 없다고 한다. 이러한 홍길동씨의 상태는 아래와 같이 표현할 수 있을 것이다.
```python
>>> money = 5000
>>> card = False
```
홍길동씨는 택시를 타고 목적지까지 가려고 한다. 목적지까지 가기 위해서는 카드를 소유하고 있거나 4,000원 이상의 현금을 가지고 있어야 한다고 한다. 홍길동씨는 택시를 탈 수 있는지를 판별할 수 있는 조건식을 작성하고 그 결과를 출력하시오.

#### A1
```
money = 5000
card = False

if money >= 5000 or card:
    print('taxi')
else:
    print('walk')
```


#### Q2 조건문2
홍길동씨의 행운권 번호는 23번 이라고 한다. 다음은 행운권 당첨번호 리스트이다.
```
>>> luchy_list = [1, 9, 23, 46]
```
홍길동씨가 당첨되었다면 "야호"라는 문자열을 출력하는 프로그램을 작성하시오.

```
lucky_list = [1, 9, 23, 46]

if 23 in lucky_list:
    print('야호')
else:
    print('fail')
```


#### Q3 홀수 짝수 판별
주어진 수가 짝수인지 홀수인지 판별하는 프로그램을 작성하시오.

#### A3
```
x = 3

if x%2 == 0:
    print('even')
else:
    print('odd')
```


#### Q4 문자열 분석
다음 문자열을 분석하여 나이가 30미만이고 키가 175 이상인 경우에는 YES를 출력하고 아닌 경우에는 NO를 출력하는 프로그램을 작성하시오.
```
나이 : 30, 키 : 180
```

#### A4
```
age = 30
height = 180

if age < 30 and height >= 175:
    print('yes')
else:
    print('no')
```


#### Q5 조건문3
다음 코드의 결과값은 무엇일까?
```
>>> a = "Life is too short, you need python"
>>> if 'wife' in a:
...     print('wife')
... elif 'python' in a and 'you' not in a:
...     print('python')
... elif 'shirt' not in a:
...     print('shirt')
... elif 'need' in a:
...     print('need')
... else:
...     print('none')
```

#### A5
```
shirt
```



## 3 - 2 while
#### Q1 1부터 100까지 더하기
1부터 100까지의 자연수를 모두 더하고 그 결과를 출력하시오.

#### A1
```
n = 1
sum_n = 0

while n <= 100:
    sum_n = sum_n + n
    n += 1
```


#### Q2 3의 배수의 합
1부터 1000까지의 자연수 중 3의 배수의 합을 구하시오.

#### A2
```
n = 1
sum_n = 0
while n <= 1000:
    if n % 3 = 0:
        sum_n = sum_n + n

    n += 1
```


#### Q3 50점 이상의 총합
다음은 A학급 학생의 점수를 나타내는 리스트이다. 다음 리스트에서 50점 이상의 점수들의 총합을 구하시오.
```
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
```

#### A3
```
a = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum_a = 0

while a:
    temp = a.pop()
    if temp >= 50:
        sum_a = sum_a + temp
print(sum_a)
```


#### Q4 별 표시하기1
while문을 이용하여 아래와 같이 별(```*```)을 표시하는 프로그램을 작성해 보자.
```
*
**
***
****
```

#### A4
```
i = 1
while i < 5:
    print('*' * i)
    i += 1
```


#### Q5 별 표시하기 2
while문을 이용하여 아래와 같이 별(```*```)을 표시하는 프로그램을 작성해 보자.
```
*******
 ***** 
  ***
   *
```

#### A5
```
i = 4
while i > 0:
    print("{0:^7}".format('*' * (2 * i - 1)))
    i = i - 1
```



## 3 - 3 for
#### Q1 1부터 100까지 출력
1부터 100까지의 숫자를 for문을 이용하여 출력하시오.

#### A1
```
sum = 0
for i in range(101):
    sum = sum + i
```


#### Q2 5의 배수의 총합
for문을 이용하여 1부터 100까지의 자연수 중 5의 배수에 해당되는 자연수들의 총합을 구하시오.

#### A2
```
sum = 0
for i in range(1001):
    if i % 5 == 0:
        sum = sum + i
```


#### Q3 학급의 평균 점수
for문을 이용하여 A 학급의 평균 점수를 구해보자.
```
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
```

#### A3
```
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for i in a:
    sum = sum + i
mean = sum / len(a)
```


#### Q4 혈액형
다음은 학생들의 혈액형 (A, B, AB, O)에 대한 데이터이다.
```
['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
```
for 문을 이용하여 각 혈액형 별 학생수의 합계를 구하시오.

#### A4
```
blood_type = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
ct_a = ct_b = ct_o = ct_ab = 0
for i in blood_type:
    if i == 'A':
        ct_a += 1
    elif i == 'B':
        ct_b += 1
    elif i == 'O':
        ct_o += 1
    elif i == 'AB':
        ct_ab += 1
    else:
        print('not human')
```


#### Q5 리스트 내포1
리스트 중에서 홀수에만 2를 곱하여 저장하는 다음과 같은 코드가 있다.
```
numbers = [1, 2, 3, 4, 5]

result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n * 2)
```
위 코드를 리스트 내포(list comprehension)를 이용하여 표현하시오.

#### A5
```
numbers = [1, 2, 3, 4, 5]
result = [i * 2 for i in numbers if i % 2 != 0]
```


#### Q6 리스트 내포2
리스트 내포를 이용하여 다음 문장에서 모음('aeiou')을 제거하시오.
```
Life if too short, you need python
```

#### A6
```
vowels = ['a', 'e', 'i', 'o', 'u']
quote = 'Life is too short, you need python'
result = [i for i in quote if i not in vowels]
```
