---
title:  "python colon과 type hint"
excerpt: "pythonic한 코드"
categories:
 - Python
tags:
 - [python,study,TIL]
last_modified_at: 2022-03-25
toc: true
toc_sticky: true
---

# python 에서의 콜론(colon, ' : ')

<br>

Python에서 콜론은 일반적으로 3가지의 경우에 쓰이게 된다.

<br>

python을 조금이라도 해본 사람은 2가지 사용법은 알지만 3.6 버전에 추가된 사용방법은 알지 못 하는 경우가 있을 것이다.

<br>

나도 나름 python을 많이 사용했지만 최근에 알게된 콜론 사용처가 있어 간단하게 정리해본다.

<br>



## 콜론이 쓰이는 곳



<br>

- 클래스, 함수나 반복문, 조건문의 마지막에 사용

```python
def colon():
    pass
class COLON():
    pass
if colon:
    pass
for i in colon:
    pass
```

<br>

- 딕셔너리의 key value를 구분 짓기위해 사용

```python
colon_dic = {
    'colon' : colon
}
```

<br>

- 자료형에 대한 변수 주석


<br>


## 콜론을 이용한 type hint

<br>

사실 기존 2가지 사용처는 워낙 기본적인 부분이라 의식하지 않고 사용하지만 3.6 버전에 추가된 변수 주석같은 경우는 흔하게 접하는 방식은 아니다.

<br>

python은 `동적 타입 언어`로서 C나 Java와 다르게 변수를 선언할 때 자료형을 명시적으로 선언해줄 필요가 없다.

이는 Duck Typing이라는 추론 방법으로 python이 자체적으로 자료형을 정의하는 방식이다.

<br>

개발자는 개발할 때에 크게 자료형을 의식하지 않고 코드를 짤 수 있다는 장점이 있지만, 코드가 복잡해지거나 협업이 필요할 때에 자료형이 명시되지 않다면 개발 과정에서 장애가 발생할 확률이 꽤 있다.

<br>

아마도 python 측에선 이런 특성을 조금이라도 개선하기 위해 콜론을 이용한 변수 주석 문법을 만들어주지 않았을까 추측해본다.

<br>

코드를 통해 알아보자.

<br>

```python
name : str = '윤정호'
age : int = 28
num_list : List[int] =  [i for i in range(10)]
```

<br>

위와 같이 `(변수명) : (자료형) = 값` 의 형태로 사용된다.

<br>

이 뿐만 아니라 함수에서 각 인자의 자료형에 대한 힌트를 줄 때도 많이 사용되어 진다.

<br>

```python
def exam(a, b:int) -> int:
    return a+b
```

<br>

인자 뿐만아니라 화살표 문법을 통해 return 값에 대한 자료형 힌트도 줄 수 있다.

<br>

주의할 점을 말 그대로 힌트이다. 

<br>

특정 자료형에 대하여 힌트를 줌으로서 유지 보수 능력을 키우고, 에러를 방지하는 목적일 뿐이지 자료형에 제약을 주는 기능은 하지 않는다.

<br>