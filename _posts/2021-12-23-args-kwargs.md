---
title:  "*args와 **kwargs"
excerpt: "함수의 인자 설정"
categories:
 - Python
tags:
 - [python,study,TIL]
last_modified_at: 2021-12-23
toc: true
toc_sticky: true
---

# *args 와 **kwargs





python 코드를 보다보면 함수의 매개변수로 def something(*args, **kwargs) : 이런식으로 선언 되 있는 것을 종종 볼 수 있다.



간단하게 정리하자면 **함수를 설정할 당시 인자로 받을 인수를 정확히 특정할 수 없을 때 모든 인수를 받겠다는 의미**로 사용된다.



해당 매개 변수의 의미에 대해서 알아보자.



## asterisk('*')



사실 args 나 kwargs 는 관례적으로 쓰는 매개변수명일 뿐이고 아무런 의미는 없다.

*yoon, **jungho 라고 해도 원하는 기능을 구현하는 것엔 아무런 영향이 없다.

하지만 완전한 private 프로젝트가 아니라면 관례에 맞춰서 작성해주자.



암튼 중요한 것은 매개변수명이 아니라 그 앞에 붙는 아스타리스크이다. 

아스타리스크의 개수에 맞춰서 인자가 설정되고 기능하게 된다.



코드를 통해 알아보자.



## *args



*args 는  'argument' 의 약어로 인수를 의미한다.



모든 인수를 **튜플**의 형태로 받아온다.

실제 python 코드를 통해 실습해보자.



```python
def sum(a,b):
    return a+b

a = sum(3,4)
print(a)
```

> 7



국민 함수인 sum 함수를 만들어서 설명해보겠다.

위 코드대로 하면 당연히 잘 작동한다.

하지만 만약 설정한 인자보다 많거나 적은 인수를 넘긴다면 ?



```python
def sum(a,b):
    return a+b

a = sum(3,4,5)
print(a)
```

> TypeError: sum() takes 2 positional arguments but 3 were given



너무나도 당연하게 에러가 발생한다.

그렇다고 인자가 3개인 또는 모든 인자의 기본값을 설정하여 함수를 만드는 것도 현명하지 못한 코딩이다.

이럴 때 *args 를 통한 함수를 구성하여 깔끔하게 해결 가능하다.



```python
def sum(*args):
    print(type(args))
    temp = 0
    for x in args:
        temp+=x
    return temp

a = sum(3,4,5)
print(a)
```

><class 'tuple'>
>12



type 함수를 통해 알 수 있듯이 우선 모든 인수는 args 라는 이름의 튜플의 요소로서 전달된다.

그릐고 for문을 통해 해당 튜플의 요소를 변수에 더하는 방식으로 덧셈 함수를 구현하였다.

이렇듯 *args 를 통해 모든 인수를 하나의 튜플에 저장하여 인수의 개수에 상관 없이 사용가능하다.





### 튜플을 인수로 사용하는 예





근데 여기서 하나 의문은 만약 인수로 애초에 튜플을 넘긴다면 어떻게 될까 ?





```python
def sum(*args):
    print(type(args))
    temp = 0
    for x in args:
        temp+=x
    return temp

temp = (3,4,5)
a = sum(temp)
print(a)

```

> TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'



에러가 발생한다. 



어떻게 된 일인지 확인해보자.



```python
def sum(*args):
    print(args)
   # temp = 0
    #for x in args:
       # temp+=x
   # return temp

temp = (3,4,5)
a = sum(temp)
print(a)
```

>((3, 4, 5),)
>
>None



보다시피 튜플의 요소로 인수 튜플 각 요소가 아닌 튜플이 통째로 들어가게 된다.



즉 *args 는 **튜플로 인수를 묶는다.**

그렇다면 어떻게 풀까



```python
def sum(*args):
    print(type(args))
    temp = 0
    for x in args:
        temp+=x
    return temp

temp = (3,4,5)
a = sum(*temp)
print(a)

```



위 처럼 인수 앞에 아스타리스크를 써주면 튜플이 풀린 상태로 함수에 전달된다.



즉 정리해보자면 

- 인자(매개변수) 앞에 아스타리스크 : **튜플로 묶는다.**
- 인수 앞에 아스타리크스크 : **리스트 or 튜플을 푼다.**





## **kwargs



이번엔 아스타리스크 두 개를 사용한 kwargs 를 알아보자.

keyword argument 의 약자이다.



args가 **튜플**을 사용하였다면 kwargs 는 **딕셔너리**를 사용한다.



```python
def sum(**kwargs):
    temp = 0
    print(type(kwargs))
    print(kwargs)
    for k,v in kwargs.items():
        print(k,v)
        temp+=v
    print("모든 value의 합은 : {}".format(temp))


sum(a=123,b=100,c=200)

```

><class 'dict'>
>{'a': 123, 'b': 100, 'c': 200}
>a 123
>b 100
>c 200
>모든 value의 합은 : 423



**kwargs 도 마찬가지로 딕셔너리를 인수로 사용할 때 아스타리스크 두 개를 붙여서 풀어서 사용 가능하다.



끝.