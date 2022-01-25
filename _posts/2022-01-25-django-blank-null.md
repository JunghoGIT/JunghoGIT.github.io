---
title:  "django null과 blank"
excerpt: "모델 필드 속성 공부"
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2022-01-25
toc: true
toc_sticky: true
published: true
---

# django 모델 필드의 null 과 blank 속성

<br>



장고의 모든 모델 필드에는 ` null`과 `blank` 설정이 포함되어 있다.

모든 필드의 default 는 null과 blank 모두 False 이다.

<br>

```python
class Test(models.Model):
    test = models.IntegerField(blank=True,null=True)
```

<br>

소문자로 사용해야함에 주의하자.

<br>

두 속성 모두 해당 모델 필드(칼럼)의 빈 값을 허용하냐에 대한 설정이다.

<br>

동일한 기능을 하는 것 같지만 사실은 큰 차이가 존재한다.

<br>

## 차이


<br>


- null : DB에서 해당 칼럼에 null 값을 허용할 것인지를 의미한다.
- blank : is_valid 가 호출될 때에 유효성을 검사하는 기준으로 사용된다.


<br>


기본적으로 유효성 검사 후에 DB에 저장되는 점을 생각하여 blank 설정을 애용하는 것이 나아보인다.

<br>

그리고 또한 자주 사용하는 문자열 필드인 CharField와 TextField 에서 null = True 를 설정할 경우 DB 내에 None과 공백 두가지 값을 중복하여 갖게 될 수 있다.

그러므로 blank=True 만을 사용함으로서 빈공백으로 저장되는 방식을 장고에서는 권한다.


<br>
  