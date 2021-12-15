---
title:  "Django 프로젝트 만들기"
excerpt: "Django 프로젝트와 앱 생성"
categories:
 - Djagno
tags:
 - [Django,python,study,TIL]
last_modified_at: 2021-12-12
toc: true
toc_sticky: true
---

# Django 프로젝트 생성



python 의 강력한 프레임워크인 django 를 이용하면 아주 쉽고 편하게 웹사이트를 만들 수 있다.

초기 환경설정부터 서버 구동까지의 과정을 해당 문서에서 다뤄보겠다.

이 문서는 window 환경을 기준으로 작성되었습니다.




## 환경설정



우선 작업할 로컬 디렉토리에 가상환경을 만들어보자.



가상환경을 만드는 방법은 [https://junghogit.github.io/python/python_virtualenv/](https://junghogit.github.io/python/python_virtualenv/)에서 확인해보자.



## Django 설치



우선 터미널에서 가상환경에 진입한다.



```bash
(venv) C:\users > pip install django 

```



위의 명령어를 통해 해당 가상환경에 django를 설치해준다.



## 프로젝트 생성



가상환경을 설치한 디렉토리 위치로 진입한다.



```bash
(venv) C:\users > django-admin startproject jumpdjango
```



위의 명령어를 입력하여 프로젝트를 생성한다.



```bash
(venv) C:\users > cd jumpdjango
(venv) C:\users\jumpdjango > tree /f

C:.
│  manage.py
│
└─jumpdjango
        asgi.py
        settings.py
        urls.py
        wsgi.py
        __init__.py


```



해당 프로젝트가 잘 설치되었는지 확인한다.



설치된 각 파일에 대한 기능과 사용법에 대해서는 이 글에서는 다루지 않고 웹 사이트를 만들면서 포스팅 해보겠다.





## 앱 생성



django project(하나의 웹 사이트) 는 다수의 app으로 이루어진다.

app은 웹 사이트에서 다양한 기능을 구현한다.

django에서 기본적으로 제공하는 관리자 앱, 인증 앱, 로그인 앱 등과 개발자가 직접 만든 앱을 말한다.



```bash
(venv) C:\users\jumpdjango > python manage.py startapp community
(venv) C:\users\jumpdjango > tree /f

C:.
│  manage.py
│
├─community
│  │  admin.py
│  │  apps.py
│  │  models.py
│  │  tests.py
│  │  views.py
│  │  __init__.py
│  │
│  └─migrations
│          __init__.py
│
└─jumpdjango
    │  asgi.py
    │  settings.py
    │  urls.py
    │  wsgi.py
    │  __init__.py
    │
    └─__pycache__
            settings.cpython-39.pyc
            __init__.cpython-39.pyc

```



community 라는 이름의 app 을 만들어봤다.



## 서버 구동



이제 기본적인 준비가 끝났으니 로컬 서버를 구동하고 웹 사이트에 접속해보자.



```bash
(venv) C:\users\jumpdjango > python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
December 08, 2021 - 15:59:20
Django version 4.0, using settings 'jumpdjango.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

```



django 는 default로 8000 포트를 사용한다.



해당 주소로 들어가서 확인해보자.



![django기본화면](\assets\images\django기본화면.JPG)



위의 이미지를 볼 수 있다면 성공이다.



서버는 ctrl + C 를 입력하여 종료할 수 있다.