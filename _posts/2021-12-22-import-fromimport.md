---
title:  "import 와 from import"
excerpt: "효율적으로 패키지 사용하기"
categories:
 - Python
tags:
 - [python,study,TIL]
last_modified_at: 2021-12-22
toc: true
toc_sticky: true
---

# import 와 from import의 차이



프로그래밍을 하다보면 다양한 라이브러리, 패키지, 모듈을 사용하게 된다.

이 때 import ... 과 from ... import ... 두 가지 방법을 보통 사용하는데 두 가지 사용법의 차이를 간단하게 알아보자.



import 할 모듈은 다음과 같이 만들었다.



```python
#test_module.py
class Hello:
    def __init__(self,name):
        self.name = name

    def hello(self):
        print("hello {} !!".format(self.name))


def world():
    print("hello world")

feeling = "tired"
```



## 클래스 사용





### import ...



```python
#main.py

import test_module

A=test_module.Hello("jungho")
A.hello()
```

> hello jungho !!



### from ... import ...



```python
from test_module import Hello

A=Hello("jungho")
A.hello()
```

> hello jungho !!



from 을 통해 import 하는 경우 모듈에서 직접 실행하는 것과 동일하게 클래스 사용이 가능하다.

import만을 한 경우 코드에서 한 번 더 모듈을 호출하여 접근하여야 한다.



## 함수와 변수



### import ...

```python
import test_module

world()
print(feeling)
```

> NameError: name 'world' is not defined





### from ... import ...



```python
from test_module import *

world()
print(feeling)
```

> hello world
>
> tired



결과를 통해 알 수 있듯이 import는 내부 함수나 변수에 직접 접근이 불가능하다.



## 결론



`import...` 는 모듈을 사용하기 위한 준비 단계 정도라고 보면 된다. 

모듈 내의 요소들을 사용하기 위해선 실행 코드 내부에서 정확히 호출 해줘야 한다.

하지만 `from ... import ...` 을 통해 모듈을 가져온다면 직접 실행하는 것과 마찬가지로 메인 코드로 모듈을 가져온다.