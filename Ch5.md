# Ch 5

## Ch 5-4. 예외 처리

#### Q1 예외 처리
다음 코드의 실행결과를 예측하고 그 이유에 대해서 설명하시오.
```python
result = 0
try:
    [1, 2, 3][3]
    "a" + 1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4

print(result)
```

#### A1
가장 먼저 나온 IndexError (```[1, 2, 3]``` 에 ```[3]``` 이 존재 하지 않음) 를 실행하면 ```result``` 가 3이 되고 마지막에 ```finally```를 실행하면 총 7이 된다.


## Ch 5-5. 내장함수

#### Q1 내장함수
다음 결과를 예측하시오.
1)
```python
>>> all([1, 2, abs(-3) - 3])
```
2)
```python
>>> chr(ord('a')) == 'a'
```

#### A1
1번의 경우 ```abs(-3)```은 3이 되고 ```abs(-3) - 3```은 0이 되므로 ```FALSE```가 나온다.
2번의 경우 ```chr```과 ```ord```는 반대연산을 해주는 함수이므로 결국 동일하게 된다.

#### Q2 filter와 lambda
filter와 lambda를 이용하여 ```[1, -2, 3, -5, 8, -3]```라는 리스트에서 음수를 모두 제거하시오.

#### A2
```python
list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3]))
```

#### Q3 16진수를 10진수로 변환
234라는 10진수의 16진수는 다음과 같이 구할 수 있다.
```python
>>> hex(234)
'0xea'
```
이번에는 반대로 '0xea'라는 16진수 문자열을 10진수로 변경해 보시오. (힌트. 내장함수 int를 활용해보자.)

#### A3
```python
int('0xea', 16)
```

#### Q4 map과 lambda
map과 lambda를 이용하여 [1, 2, 3, 4]라는 리스트의 각 요소값에 3이 곱해진 [3, 6, 9, 12]라는 리스트를 만드시오.

#### A4
```python
list(map(lambda x: x * 3, [1, 2, 3, 4]))
```

#### Q5 최대값과 최소값
다음 리스트의 최대값과 최소값의 합을 구하시오.
```python
[-8, 2, 7, 5, -3, 5, 0, 1]
```

#### A5
```python
x = [-8, 2, 7, 5, -3, 5, 0, 1]
max(x) + min(x)
```

#### Q6 소수점 반올림
17/3의 결과는 다음과 같다.
```python
>>> 17/3
5.666666666666667
```
위와 같은 결과값 5.666666666666667을 소수점 4자리까지만 반올림하여 표시하시오.

#### A6
```python
round(17 / 3, 4)
```


## Ch 5-6. 외장함수

#### Q1 sys.argv
다음과 같이 실행할 때 입력 값을 모두 더하여 출력하는 스크립트 (```C:\doit\myargv.py```)를 작성하시오.
(힌트. 외장함수 sys.argv를 이용해 보자)
```
c:\> cd doit
c:\doit> python myargv.py 1 2 3 4 5 6 7 8 9 10
55
```

#### A1
```python
import sys
a = map(int, sys.argv[1:])
print(sum(a))
```

#### Q2 os
os 모듈을 이용하여 다음과 같이 동작하도록 코드를 작성해 보자.
1. ```C:\doit``` 이라는 디렉토리로 이동한다.
2. dir 명령을 실행하고 그 결과를 변수에 담는다.
3. dir 명령의 결과를 출력한다.

#### A2
```python
import os
os.chdir("C:\doit")
result = os.popen("dir")
print(result)
```

#### Q3 glob
glob 모듈을 이용하여 ```C:\doit``` 디렉토리의 파일중 확장자가 py인 파일만 출력하는 프로그램을 작성하시오.

#### A3
```python
import glob
glob.glob("C:\doit\*.py")
```

#### Q4 time
time 모듈을 이용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력하시오.
```python
YYYY/MM/DD HH:mm:ss (YYYY:년도, MM:월, DD:일, HH:24시간 기준시간, mm:분, ss:초)
```
출력 예
```
2018/04/03 17:20:32
```

#### A4
```python
import time
time.strftime('%Y/%m/%d %H:%M:%S, time.localtime(time.time()))
```

#### Q5 random
random 모듈을 이용하여 로또번호 (1~45 사이의 숫자 6개)를 생성하시오. (단, 중복된 숫자가 있으면 안됨)

#### A5
```python
import random
lotto_set = range(1,46)
for i in range(6):
    lotto = random.randint(0, len(lotto_set))
    data.pop(lotto_set[lotto])
```
