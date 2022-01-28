---
title:  "django User모델 참조하는 방법"
excerpt: "장고의 User모델"
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2022-01-28
toc: true
toc_sticky: true
published: true
---

# django User 모델을 참조하는 방법

<br>

장고에서 User 모델을 참조하는 방법을 알아보자.

<br>

일반적으로 3가지 방식이 존재한다.

<br>

## User 모델 직접 호출

<br>



클래스 자체를 import 하여 사용하는 방식이다.

가장 권장하지 않는 방법이다.

<br>

User 모델 폼을 만드는 것을 가정해보자.

<br>

```python
from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model= User
        fields = [
            'username',        
        ]

```

<br>

이렇게 사용해도 기능하는 데에는 아무 문제는 없으나 코드를 유지보수 하는 데 불편함이 있다.

서비스 중 모델이 변경되었을 때 일일이 코드를 변경해야함으로 유연성이 매우 떨어진다.


<br>


## get_user_model 사용


<br>


장고 auth에서 기본으로 제공하는 `get_user_model()` 을 사용할 수 있다.


<br>


 ```python
 from django.contirb.auth import get_user_model
 
 class SignupForm(UserCreationForm):
     class Meta:
         model= get_user_model()
         fields = [
             'username',        
         ]
 
 ```

<br>

객체 인스턴스를 반환한다. 

앱이 로드 되는 순간에 실행되므로 반드시 유효한 모델 객체를 반환한다는 보장이 안 된다.

<br>

난 개인적으로 User 모델을 직접 사용하는 것보단 좀 더 나은 방식이라고 판단한다.

<br>

## AUTH_USER_MODEL


<br>


장고의 settings 의 설정을 참고하여 사용하는 방식이다.

<br>

```python
from django.conf import settings

class SignupForm(UserCreationForm):
    class Meta:
        model= settings.AUTH_USER_MODEL
        fields = [
            'username',        
        ]

```

<br>

문자열을 반환한다.

가장 안정적인 방식이다.

외래키 설정할 때에는 특히 해당 방법을 사용하기를 권한다.

<br>

## 번외 request로 모델 인스턴스 참조


<br>


장고는 기본적으로 로그인 세션이 유지될 경우 request에 user 정보가 항상 유지된다.

<br>

```python
from django.contirb.auth import get_user_model

def test(request):
    user = get_user_model().objects.exclude(pk =request.user.pk )
    pass
```

<br>

