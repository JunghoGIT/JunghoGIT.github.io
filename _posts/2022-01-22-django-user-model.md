---
title:  "django User Model"
excerpt: "장고 auth의 User 클래스를 사용해보자"
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2022-01-22
toc: true
toc_sticky: true
published: true
---

# django User Model


<br>


## django.contrib.auth



<br>


장고 auth 기능은 서비스에서 필요한 권한과 인증에 관한 대부분의 것들을 기본으로 제공한다.

덕분에 개발자는 해당 기능을 구현하는데 필요한 시간을 절약할 수 있다.

<br>


auth 안에는 view, form, model 과 그 외에도 우리가 개발 단계에서 직접 구현해야할 수 많은 것들을 제공하고 우리는 필요한 부분만 가져와서 우리 입맛에 맞게 수정하여 사용하면 된다.



<br>


## auth User model 기본 구조


<br>



auth에서는 User model을 기본으로 제공하여 회원 관리를 매우 편하게 할 수 있도록 도와준다.

그리고 해당 객체들을 통하여 auth의 다른 기능들을 손 쉽게 이용한다.

<br>


장고에서도 직접 회원 모델을 만들기보단 auth에서 제공하는 User 모델을 이용하여 기능을 구현하길 강력하게 권고한다.

<br>


기본적인 User모델의 상속 구조는 다음과 같다.

<br>


- models.Model
- class AbstractBaseUser : models.Model 상속
- class AbstractUser : AbstractBaseUser 상속
- class User : AbstractUser 상속

<br>


User 모델의 경우 auth의 기능들을 사용하기 위한 모든 기능과 필수 필드가 구현되어 있다고 보면 된다.

반대로 User모델 기준 부모 클래스로 갈수록 개발자가 만들어야 할 부분이 늘어남을 의미한다.


<br>





## User 모델 생성

<br>


이제 장고의 User 모델들을 이용하여 개발자의 입맛대로 User 모델을 만드는 법을 알아보자

크게 4가지의 방법이 있다.



<br>


### User 모델을 만드는 4가지 방법 

<br>




- **Proxy Model**
  - 기존 User 모델을 직접 상속한다.
  - Meta 클래스에서 proxy =True 속성을 추가한다.
  - DB 스키마에 영향을 주지 않는다.
  - 기존 User 모델에서 DB 스키마 외에 최소한의 변경사항만을 적용할 때 사용한다.
  - 프로젝트 중간에 모델을 추가할 때 사용하기 좋아보인다.
  - 모델 설계의 자유도가 가장 낮다.
  - 자주 사용하는 방식은 아니다

<br>


```python
from django.contrib.auth.models import User
from .managers import PersonManager

class Person(User):
    objects = PersonManager()

    class Meta:
        proxy = True

    def do_something(self):
        ...
```

<br>


- **One-to-One**
  - 새로운 모델을 추가하여 기존 User 모델과 1:1 관계로 연결시켜 사용자 정보를 저장한다.
  - 기존 User 모델과 관계됨으로서 auth 기능을 사용 할 수 있다.
  - 프록시 방식에 비해 필드에 대한 자유도가 매우 높다.

<br>


```python
from django.db import models
from django.contrib.auth.models import User
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20, blank=True)
    
    ...
```

<br>


- **AbstractBaseUser 모델 사용**
  - AbstractBaseUser 모델을 상속한 User 모델을 새로 정의하여 사용한다.
  - 프로젝트 시작 전 준비 단계에서 사용되어져야 한다.
  - 새로운 User 모델을 정의함에 따라 Settings.py 에 AUTH_USER_MODEL ='app이름.User' 설정 값을 추가해야 한다.
  - 가장 많은 구현을 필요로 한다. (자유도가 가장 좋다.)
  - 모든 기법 중 가장 적은 필드가 포함되어 있다.
    - 필수 필드로서 password 하나의 필드만 설정되어 있음

<br>


*AbstractBaseUser 방식은 설명을 위한 예시 코드가 너무 방대하여 생략 합니다. Do googling..!*

<br>




- **AbstractUser 모델 사용**
  - AbstractUser 모델을 상속한 User 모델을 새로 정의하여 사용한다.
  - 프로젝트 시작 전 준비 단계에서 사용되어져야 한다.
  - 새로운 User 모델을 정의함에 따라 Settings.py 에 AUTH_USER_MODEL ='app이름.User' 설정 값을 추가해야 한다.
  - 서비스 규모에 따라 달라지겠지만 가장 일반적인 사용법이다.

<br>


```python
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=20)

    def __str__(self):
        return self.nickname
```


<br>





## User 모델 포함 필드


<br>



- email
- username
  - Not Null
- password
  - Not Null
- first_name
- last_name
- groups
- user_permissions
- is_staff
- is_active
  - boolean타입으로 계정의 활성화 여부를 의미
  - 계정 삭제보단 cascade 옵션으로 인한 데이터 삭제를 방지하기 위해 해당 필드를 이용하는 것이 좋음
- is_superuser
- last_login
- date_joined


<br>
