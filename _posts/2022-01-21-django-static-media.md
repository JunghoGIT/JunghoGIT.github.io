---
title:  "django static과 media"
excerpt: "장고 정적파일 관리"
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2022-01-21
toc: true
toc_sticky: true
published: true
---

# django에서 static과 media


<br>



장고에서는 static과 media, 2가지 종류의 정적파일이 존재한다.

해당 정적 파일들은 웹 서비스에 사용하기 위해 미리 준비해둔 파일이라고 정의 할 수 있다.

<br>

스타일마다 차이가 있겠지만 개발 시작 단계에서 settings.py 를 통해 해당 정적파일들에 대한 설정을 미리 한 후에 개발을 시작하는 것이 수월하다.


<br>


우선 static에 대해서 알아보자

<br>

## static file



<br>

### 장고에서 static file 이란 ?

<br>

장고에서 static file 이란 다음을 의미한다.

- css, js, image...
- 개발 리소스로서의 정적인 파일
- 수시로 변경되지 않으며 미리 준비되어 고정되어 있는 파일

<br>

### 설정



장고에서는 static file 설정을 위해 크게 3가지의 항목을 사용한다.

각 항목 별로 사용법을 알아보자.


<br>


- **STATICFILES_DIRS**
  - 개발 단계에서 사용하는 정적 파일이 위치한 경로를 지정
  - 만약 여러 앱에서 서로 다른 경로를 사용한다면 리스트나 튜플의 형태로 다수의 경로 지정해준다.

<br>

```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
#최상위 경로에 static 디렉토리를 만들었을 경우
```

<br>

- **STATIC_URL**
  - 웹 페이지에서 사용할 정적 파일의 최상위 경로이다.
  - 물리적인 파일의 경로가 아닌 웹페이지에서 사용할 수 있는 주소의 최상위를 지정해주는 것이다.
  - static 템플릿 태그에서 참조되어 진다.

<br>

```python
STATIC_URL = 'static/'
```

<br>



- **STATIC_ROOT**
  - `python manage.py collectstatic` 명령어를 통해 프로젝트 내의 모든 static file을 저장할 경로를 의미한다.
  - 배포시에만 사용한다고 생각하면 된다.
  - **STATICFILES_DIRS** 과 동일한 경로로 지정하면 안 된다.

<br>

```python
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# 한 곳에 모으는 것이기 때문에 문자열로 값을 줘야한다.
```


<br>


## media file

<br>



### 장고에서 media file 이란?


<br>


- media file은 유저가 웹에서 업로드한 정적 파일을 의미한다.
- FileFiled, ImageFiled 를 통해 저장된 모든 파일


<br>


### 설정



<br>



크게 2가지의 설정이 존재한다.


<br>


- **MEDIA_ROOT**

  - 업로드 된 미디어 파일이 저장될 공간을 지정하는 항목

  - STATIC_ROOT와는 다른 경로여야 한다.

  - image나 file 필드에 upload_to 를 설정을 통해 저장되는 경로의 최상위 경로이다.

    - 즉 경로 지정시 생략해야한다.

    

<br>

```python
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```


<br>


- **MEDIA_URL**
  - STATIC_URL 과 마찬가지로 최상위 경로 URL을 지정한다.
  - STATIC_URL 과 동일할 수 없다.

<br>

### urls.py 설정

<br>

media file은 static file과 다르게  urlpatterns 에 설정 항목을 넘겨줘야 정상적으로 동작한다.

<br>

```python
if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)

```


<br>


## 주의사항


<br>


장고는 웹 서버가 아닌 웹 어플리케이션 서버이다. 

실제로 클라이언트에게 정적 파일을 제공하는 것은 웹 서버(아파치,엔진엑스)의 업무이다.

그러나 우린 효율적인 개발을 위해 개발 단계에서만 몇몇 설정으로 정적 파일을 제공할 수 있도록 하는 것 뿐이다.

<br>

DEBUG = False , 즉 배포 단계에서는 보통 AWS나 azure 같은 클라우드 서비스를 통해 별도의 서버에 정적파일들을 저장하여 관리한다.

<br>