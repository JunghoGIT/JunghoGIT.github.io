---
title:  "데코레이터"
excerpt: "반복되는 코드를 줄여보자"
categories:
 - Python
tags:
 - [python,study,TIL]
last_modified_at: 2022-02-28
toc: true
toc_sticky: true
---

# 데코레이터


<br>


데코레이터란 python에서 기본적으로 제공하는 기능 중 하나이다.

<br>

일반적으로 반복되는 기능 또는 코드를 여러 함수에서 사용할 때에 반복되는 부분을 다른 함수에서 재사용할 수 있도록 꾸며주는 일을 한다.

<br>

## 사용 예시



만약에 수 십개의 함수가 동작하는 프로그램을 만든다고 가정해보자.

<br>

그리고 그 함수들은 모두 함수의 실행 시점부터 끝나는 시점까지의 시간을 측정하여 프로그램의 실행 소요 시간이 출력되어야 한다.

<br>

데코레이터를 사용하지 않는다면 다음과 같은 코드의 구조를 갖게 될 것이다.

<br>

```python
import time,math


def test():
    print('속도 측정 시작')
    start = time.time()
    print("함수 실행")
    math.factorial(100000)
    end = time.time()
    print(f"속도 측정 결과 {end-start}")

def test2():
    print('속도 측정 시작')
    start = time.time()
    print("함수 실행")
    math.factorial(200000)
    end = time.time()
    print(f"속도 측정 결과 {end-start}")    

    
.
.
# 중략
.
.
```


<br>


보다시피 모든 함수에 중복으로 존재하는 코드가 존재한다.

<br>

물론 지금 예시에서는 몇 개 안 된다고 생각할 수도 있지만, 수 십 수 백 그 이상일 때는 정말 개발자스럽지 못한 코드인 것이다.

<br>

또한 속도 측정은 함수 실행의 앞과 뒤에서 기능을 실행해야 유의미 하기 때문에 해당 부분을 별도의 함수로 만들어도 한계가 분명하다.

<br>

이럴 때 데코레이터를 사용하면 된다.

<br>

```python
import time, math

def timer_decorator(func):
    def decorator():
        print('속도 측정 시작')
        start = time.time()
        func()
        end = time.time()
        print(f"속도 측정 결과 {end-start}")
    return decorator

@timer_decorator
def test():
    print("함수 실행")
    math.factorial(100000)

@timer_decorator
def test2():
    print("함수 실행")
    math.factorial(200000)

.
.
# 중략
.
.
    
test()

```

<br>

위와 같이 데코레이터 기능을 통해 반복되는 부분을 재사용함으로서 코드를 훨씬 간단히 줄이고 좀 더 pythonic한 코드를 만들 수 있다.


<br>


## 클래스에서의 사용

<br>

데코레이터는 함수 뿐만 아니라 클래스에서도 사용 가능하다.

<br>

생성자와 \__call__  함수를 정의해 줌으로서 동일한 기능을 구현할 수 있다.


<br>


```python
import time, math

class TimerDeco:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print('속도 측정 시작')
        start = time.time()
        self.func()
        end = time.time()
        print(f"속도 측정 결과 {end - start}")

class Test:

    @TimerDeco
    def test():
        print("함수 실행")
        math.factorial(100000)

    @TimerDeco
    def test_2():
        print("함수 실행")
        math.factorial(200000)


t = Test
t.test()
t.test_2()

```

<br>