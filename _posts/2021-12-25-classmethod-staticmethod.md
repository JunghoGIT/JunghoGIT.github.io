---
title:  "classmethod와 staticmethod"
excerpt: "정적메소드와 인스턴스 변수"
categories:
 - Python
tags:
 - [python,study,TIL]
last_modified_at: 2021-12-25
toc: true
toc_sticky: true
---

# classmethod & staticmethod



클래스 선언 부에서 확인할 수 있는 `@classmethod`와 `@staticmethod`에 대해서 알아보자.

두 데코레이터 모두 정적 메소드를 의미하며, 정적 메소드란 인스턴스를 생성하지 않고 호출 할 수 있는 메소드를 의미한다.



우선 본격적인 학습 전에 클래스의 변수에 대해 짧은 코드로 확인해보자.



```python
class class1 :
    temp = 10 # 클래스 변수
    def __init__ (self, A, B): # 생성자 
        self.A=A # 인스턴스 변수
        self.B=B # 인스턴스 변수
```





## 클래스 변수





클래스 메소드를 확인하기 전에 모든 직원에게 똑같이 시급을 주는 이상한 술집의 직원을 객체화 해보자.



```python
#work.py

class employee:
    def __init__(self,name,time,hourlywage):
        self.name=name
        self.time=time
        self.hourlywage=hourlywage

    def wage(self):
        wage=self.time * self.hourlywage
        print(f"{self.name}님의 이번 달 근무 시간은 {self.time}시간이며, 예상 급여는 {wage}원 입니다.")
```



생성자를 통해 이름, 한 달 간 근무시간, 시급을 멤버 변수로 갖는 인스턴스를 생성할 수 있다.



wage 함수를 통해 인스턴스별 한달 예상 급여를 알 수 있다.



```python
import work

employee1 = work.employee('윤정호',145,8600)
employee2 = work.employee('드와이트',123,8600)
employee3 = work.employee('마이클',110,8600)

employee1.wage()
employee2.wage()
employee3.wage()
```

> 윤정호님의 이번 달 근무 시간은 145시간이며, 예상 급여는 1247000원 입니다.
> 드와이트님의 이번 달 근무 시간은 123시간이며, 예상 급여는 1057800원 입니다.
> 마이클님의 이번 달 근무 시간은 110시간이며, 예상 급여는 946000원 입니다.



여기서 만약 가게가 잘 돼서 시급이 400원 오른 9000원 으로 변경 되었다고 생각해보자.

그렇다면 객체를 생성하는 코드를 전부 변경해주어야한다.

```python
.
.
employee1 = work.employee('윤정호',145,9000)
employee2 = work.employee('드와이트',123,9000)
employee3 = work.employee('마이클',110,9000)
.
.
```



지금이야 직원이 3명이지만 해당 객체가 많아질수록 효율성은 떨어지게 된다.

이럴 땐 클래스 변수를 사용하면 해결된다.



```python
#work.py

class employee:
    hourlywage=8600
    
    def __init__(self,name,time):
        self.name=name
        self.time=time
        #self.hourlywage=hourlywage

    def wage(self):
        wage=self.time * self.hourlywage
        print(f"{self.name}님의 이번 달 근무 시간은 {self.time}시간이며, 예상 급여는 {wage}원 입니다.")
```

```python
import work

employee1 = work.employee('윤정호',145)
employee2 = work.employee('드와이트',123)
employee3 = work.employee('마이클',110)

employee1.wage()
employee2.wage()
employee3.wage()

print("-------임금 인상-------")
work.employee.hourlywage = 9000

employee1.wage()
employee2.wage()
employee3.wage()
```

> 윤정호님의 이번 달 근무 시간은 145시간이며, 예상 급여는 1247000원 입니다.
> 드와이트님의 이번 달 근무 시간은 123시간이며, 예상 급여는 1057800원 입니다.
> 마이클님의 이번 달 근무 시간은 110시간이며, 예상 급여는 946000원 입니다.
> -------임금 인상------
> 윤정호님의 이번 달 근무 시간은 145시간이며, 예상 급여는 1305000원 입니다.
> 드와이트님의 이번 달 근무 시간은 123시간이며, 예상 급여는 1107000원 입니다.
> 마이클님의 이번 달 근무 시간은 110시간이며, 예상 급여는 990000원 입니다.



이상태에서 시급에 변수에 대해서 클래스가 아니라 인스턴스로 접근하면 어떻게 될까 ?







```python
.
.
.# 윗 부분 생략
print("-------임금 인상-------")
work.employee.hourlywage = 9000

employee1.hourlywage= 10000

employee1.wage()
employee2.wage()
employee3.wage()
```

>-------임금 인상-------
>윤정호님의 이번 달 근무 시간은 145시간이며, 예상 급여는 1450000원 입니다.
>드와이트님의 이번 달 근무 시간은 123시간이며, 예상 급여는 1107000원 입니다.
>마이클님의 이번 달 근무 시간은 110시간이며, 예상 급여는 990000원 입니다.

생성자를 통해 인스턴스 변수를 초기화 해준 적이 없음에도 인스턴스 변수가 생성되어 클래스 변수가 아닌 인스턴스 변수로 함수가 동작한다.

이런 경우를 위해 클래스 메소드를 사용할 수 있다.



## @classmethod



@classmethod 데코레이터를 통해 클래스 함수를 지정해줄 수 있다.

인자로 'cls' 가 필수로 존재하며, 이는 클래스 그 자체를 의미한다.



```python
class employee:
.
.#(중략)
.

    @classmethod
    def set_hourlywage(cls,N):
        cls.hourlywage=N
.
```



set_hourlywage 함수를 추가해줬다.

이제 해당 함수를 사용해보자.



```python
.
.
.# 윗 부분 생략
print("-------임금 인상-------")
work.employee.hourlywage = 9000

employee1.set_hourlywage(10000)

employee1.wage()
employee2.wage()
employee3.wage()
```

>-------임금 인상-------
>윤정호님의 이번 달 근무 시간은 145시간이며, 예상 급여는 1450000원 입니다.
>드와이트님의 이번 달 근무 시간은 123시간이며, 예상 급여는 1230000원 입니다.
>마이클님의 이번 달 근무 시간은 110시간이며, 예상 급여는 1100000원 입니다.



짜잔~! 클래스에 직접 접근하지 않고 인스턴스를 통해 접근했음에도 클래스 메소드를 통해 클래스 변수의 값을 변경하였다.

사실 이 부분만으론 굳이 왜 이렇게 하지 싶은 의문이 들 수 밖에 없다.

그 의문은 언젠간 작성할 캡슐화(은닉화)을 통해 해결할 수 있다.



## @staticmethod



이번엔 staticmethod에 대해서 알아보자.



`@staticmethod`는 첫 번째 매개변수가 필요하지 않도록 하는 데코레이터이다.

클래스 메소드는 cls를 매개변수로 필요했고 인스턴스 메소드는 self를 필요로 한 것과 차이가 난다.



코드를 통해 알아보자



```python
# work.py
class employee:
    .
    .
    .#   (중략)
	@staticmethod
    def clac(self,x,y):
        return x*y

if __name__ == '__main__' :    
	a = employee.clac(2,4)
    print(a)   
```

> TypeError: clac() missing 1 required positional argument: 'y'



에러 코드를 통해 볼 수 있듯이 @staticmethod 는 self를 하나의 인자로서 인수를 요구한다.

self = 2, x=4 가 되므로 y 인자에 어떤 인수도 들어가지 않게 된다.

@staticmethod 데코레이터를 사용할 땐 절대 self나 cls를 인자로 가질 수 없다.



@statiemethod 는 내 짧은 식견으론 클래스를 객체화가 아닌 모듈화를 하여 사용할 때 말고는 크게 사용할 일은 없을 것 같다.

