---
title:  "django model field"
excerpt: "장고에서 지원하는 모델필드"
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2022-01-05
toc: true
toc_sticky: true
published: true
---

# 장고 기본 지원 모델 필드


<br>

django 에서 model 클래스(테이블)를 정의할 때 각 각의 필드(속성)에 대하여 정의하고 다양한 옵션들을 이용해 제약 조건을 설정해 줄 수 있다.

<br>

이렇게 정의된 model 클래스는 ORM통해 migrate 될 때 DB에서 지원하는 필드들을 반영하여 테이블로 생성된다.


<br>


다양한 기본 지원 필드들을 살펴보자.

<br>

자세한 정보는 장고 공식 문서 [https://docs.djangoproject.com/en/4.0/ref/models/fields/](https://docs.djangoproject.com/en/4.0/ref/models/fields/) 를 통해 확인 할 수 있다.

<br>

> 지금 보고 있는 이 문서는 계속 업데이트 될 예정입니다.
>
> 주인장 윤


<br>


## primary key

<br>
<br>

기본키 속성을 의미한다.

<br>

미 설정시 장고 내부에서 id 값으로 데이터 생성순으로 고유한 인덱스 넘버를 기본키로서 부여한다.

<br>

- AutoField
  - 추가 예정
- BigAutoField
  - 추가 예정


<br>


## 문자열

<br>

문자열이 저장될 수 있는 속성을 의미한다.

<br>

- CharField
  - 최대 길이 정의가 필요한 타입
  - TextFiled에 비해 최적화에 용이
  - `max_length` 옵션 사용
- TextField
  - 최대 길의 지정 없이 사용 (사용은 가능하나, 일반적인 경우 이러하다.)
- SlugField
  - 문자열을 유효한 URL 로 만들기 위한 데이터를 저장
  - 모든 영문자를 소문자로, 공백은 하이픈(-) 으로 변경된다.

<br>



## 날짜와 시간

<br>


날짜와 시간 타입 또는 정보를 저장한다.


<br>


- DateField
  - 날짜를 저장한다.
- TimeField
  - 시간을 저장한다.
- DatdTimeField
  - 날짜와 시간을 저장한다.
  - `auto_now` 와 `auth_now_add` 옵션을 주로 사용한다.
- DurationField
  - 기간을 저장한다.
  - 공식문서에 따르면 postgreSQL DB 외에 다른 DB에선 DateTimeField 와의 연산이 불가능 하다고 한다.

<br>

## 참/ 거짓

<br>

True 또는 False 여부를 저장한다.

<br>



- BooleanField
  - 추가 예정
- NullbooleanField
  - Null 을 허용한다.

<br>



## 숫자

<br>

숫자를 저장한다.

<br>

- IntegerField
  - ...
- SmallIntegerField
  - ...
- PositiveIntegerField
  - ...
- PositiveSmallIntegerField
  - ...
- BigIntgerField
  - ...
- DecimalField
  - ...
- FloatField
  - ...

<br>

## 파일


<br>


파일을 저장한다.


<br>


- BinaryField

  - raw binary 데이터를 저장
  - 바이트만을 할당한다.
  - 매우 제한적이며 사용도가 매우 낮다.

- FileField

  - 파일을 저장한다.
  - upload_to 설정 사용 가능

- FilePathField

  - 파일 시스템에서 특정한 디렉토리에 파일 이름으로 제한
  - path 인수를 필수로 지정해줘야함

- ImageField

  - upload_to 설정 사용 가능

  - height_field, width_field 설정을 통해 이미지의 크기를 자동으로 채울 수 있다.

  - pillow 라이브러리를 필수로 요구한다.

    
<br>


## 그 외 특수 필드


<br>


- EmailField 
  - 유효한 이메일 주소인지 체크하는 CharField 이다.
  - EmailValidator 를 사용한다.
- URLField
  - URL을 위한 CharField 이다.
- UUIDField
  - Universally Unique IDentifiers 를 저장하기 위한 필드
  - 기본키로 설정할 때 주로 사용됨
- GenericlPAddressField
  - IP 를 저장하는 필드

<br>

## 관계형 필드

<br>

RDBMS 에서 매우 중요한 부분인 만큼 해당 필드들에 대한 세부 사항은 다른 문서에서 다뤄보겠다.

<br>

- ForiegnKey
- ManyToManyField
- OneToOneField


<br>


