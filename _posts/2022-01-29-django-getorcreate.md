---
title:  "django get or create"
excerpt: "생성하거나, 조회하거나"
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2022-01-29
toc: true
toc_sticky: true
published: true
---

<br>

# get_or_create 사용법


<br>


ORM 을 이용하여 중복된 데이터를 만들지 않기 위해 사용하기 좋은 get_or_create 함수와 함수를 사용하지 않고 해당 기능을 구현하는 법을 알아보자

<br>

## get_or_create()

<br>

```python
object, created = Model.objects.get_or_create(pk=1)
```

<br>

일반적으로 위의 형태로 사용된다.

<br>

get_or_create() 는 튜플의 형태로 두 가지 값을 반환한다.

<br>

첫번째 변수 (object) 에는 본인이 원하는 조건에 해당되는 모델 인스턴스가 반환된다.

<br>

두번째 변수(created) 에는 get할 모델 객체가 존재 하지 않음으로 새로운 모델 인스턴스를 만들었다는 의미로서 boolean 값을 반환한다.

<br>

만약 새로운 인스턴스를 생성했다면 True, 

아니라면 False 를 반환한다.

<br>

## 사용 예제 

<br>



기본적인 사용법은 두번째 변수를 boolean flag로서 이용해 if문으로 분기를 나누어 사용하는 방식이다.

<br>

```python
def get_or_create_view(request):
    user_profile, flag = Profile.objects.get_or_create(author=request.user)
    
    if flag :
        user_profile.lang = '파이썬'
        user_profile.hobby = '블로깅'
        user_profile.save() # 새로운 데이터 객체 생성
    	
    else : 
        user_profile.hobby = '블로깅'
        user_profile.save()
```

<br>

만약 유저 프로필을 가져와서 취미를 수정하고 싶으나 주 사용 언어 필드가 not null 일 때를 가정하면 위와 같은 코드를 사용하면 된다.

<br>

새로운 인스턴스가 만들어졌다면 not null 필드인 값 까지 설정해서 저장을 해줘야하며, 만약 기존 객체를 인스턴스로 가져왔다면 not null 필드 값은 존재할 것이니 새로운 값만 수정해주면 된다.



<br>

## get_or_create 를 사용하지 않는 방법

<br>

장고의 get_or_create 를 사용하지 않고 python의 기본 예외처리 문법으로 비슷한 동작을 구현할 수 있다.

<br>

참고로 본인은 이 방법을 좀 더 직관적이라 생각해 좋아한다.

<br>

```python
try:
    user_profile =Profile.objects.get_or_create(author=request.user)
    user_profile.hobby = '블로깅'
    user_profile.save()
except Profile.DoesNotExist :
    user_profile = Profile.objects.create(author=request.user, hobby='블로깅',lang='python')
    user_profile.save() #
    
```

<br>

이 방법은 장고의 ORM 이 매칭되는 객체가 존재하지 않을 때 빈 쿼리셋을 반환하는 것이 아닌 `DoesNotExist` 에러를 발생 시키는 것을 이용하는 방식이다.


<br>
