---
title:  "django-debug-toolbar"
excerpt: "개발단계에서 도움을 주는 유틸"
categories:
 - Django
tags:
 - [Django,study,TIL,python]
last_modified_at: 2021-12-29
toc: true
toc_sticky: true
---

# django-debug-toolbar



장고의 강력한 기능인 ORM 덕분에 우리는 SQL 없이 객체와 DB를 맵핑하여 손 쉽게 데이터 처리를 할 수 있다.

사실 SQL을 직접 사용하지 않을 뿐이지 결국 ORM은 RDBMS에 사용자의 요청에 따른 SQL을 만들어 보낸다.



여기서 문제가 하나 발생하는데 사용자가 직접 만든 SQL이 아니기 때문에 해당 SQL의 세부 내역에 대해서 확인하기 어렵다는 것이다.



이때 `django-debug-toolbar` 를 추가하여 응답과 요청에 대한 다양한 디버깅 정보를 확인 할 수 있다.



## 설치



### 1. 패키지 설치



우선 pip 명령어로 django-debug-toolbar 를 설치해준다.



```bash
pip install django-debug-toolbar
```



### 2. 설정전 환경



우선 project의 settings.py 에서 `INSTALLED_APPS ` 과 `TEMPLATES ` 항목이 다음과 같은 코드가 존재하는지 확인해보자. 

없다면 추가해준다.



```python
INSTALLED_APPS = [
    # ...
    "django.contrib.staticfiles",
    # ...
]

STATIC_URL = "static/"

# ...
# ...
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        # ...
    }
]
```



### 3. INSTALLED_APPS 추가



settings.py 에서 `INSTALLED_APPS ` 항목에 debug_toolbar 를 추가해주자.



```python
INSTALLED_APPS = [
    # ...
    "debug_toolbar",
    # ...
]

```



### 4. urls.py 에 url 맵핑



프로젝트의 urls.py의 urlpatterns 에 path를 추가한다.



```python
from django.urls import include, path

urlpatterns = [
    # ...
    path('__debug__/', include('debug_toolbar.urls')),
]
```





### 5. Middleware 추가



다시 settings.py 로 돌아가 `MIDDLEWARE` 항목에 다음과 같이 미들웨어를 추가해준다.



```python
MIDDLEWARE = [
    # ...
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # ...
]
```





### 6. INTERNAL_IPS 설정



앱의 모든 사용자가 디버깅에 관한 정보들을 알면 보안상의 큰 위험이 노출되니 IP를 지정하여 관리자만 사용할 수 있도록 한다.

settings.py 에 다음과 같은 코드를 추가해준다.



```python
INTERNAL_IPS = ['127.0.0.1']
```





## 적용 확인



이제 runserver 하여 로컬 페이지로 접속하면 아래와 같이 우측에 toolbar가 적용된 모습을 볼 수 있다.



 ![debug_toolbar](\assets\images\django\debug_toolbar.JPG)



해당 페이지에서 사용되는 정적 파일이나 페이지의 요청 응답 과정에서 사용된 SQL 까지 확인 할 수 있다.



주의 할 점은 너무 많은 정보가 노출되니 DEBUG 가 TRUD 일때만 사용해야 한다.

서비스 전 개발과정에서 유용하게 쓰이는 도구 중 하나로서 잘 사용하자 !