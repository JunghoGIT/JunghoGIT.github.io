---
title:  "django postgreSQL 연동"
excerpt: "장고 DB를 설정해보자"
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2022-01-21
toc: true
toc_sticky: true
published: true
---

# django에서 postgreSQL 사용하기


<br>


## postgreSQL 설치

<br>





우선 공식 사이트 링크 [https://www.postgresql.org/download/](https://www.postgresql.org/download/) 에서 각자 OS에 맞춰 다운로드 후 설치하면 된다.

<br>

근데 나의 경우엔 에러가 발생했다.

그것도 읽을 수도 없는 에러..

<br>

![postgresql_error](\assets\images\django\postgresql_error.JPG)

<br>

참나 이건 뭐 읽을 수도 없다.

<br>

그래서 구 버전도 설치해봤으나 동일한 오류 발생..



빠르게 구글링을 해서 동일한 에러가 발생한 경우를 찾아봤는데 대부분 에러의 원인을 해결하기보단 다른 경로에서 다운로드 받는 방법을 선택했다.

<br>

약간은 구버전이긴 하나 아래의 경로에서 다운로드 받아 설치하면 정상적으로 진행된다.

[https://get.enterprisedb.com/postgresql/postgresql-11.2-1-windows-x64.exe](https://get.enterprisedb.com/postgresql/postgresql-11.2-1-windows-x64.exe)

<br>

설치는 비밀번호 설정 외에는 별다른 액션 없이 next만 눌러서 설치해도 충분하다.

<br>

## DB설정


<br>


DB설정 및 관리는 **PgAdmin4** 를 통해 GUI 환경에서도 가능하지만 CLI 환경에서 진행해보겠다.


<br>


### 1. 관리자 계정 접속

<br>

설치가 정상적으로 완료됐다면 SQLshell (psql) 또한 설치됐을거다.

해당 쉘을 실행하여 'postgres 사용자의 암호 :' 가 나올 때까지 Enter를 누르자.

그리고 설치할 당시 설정했던 암호를 입력하면 postgres=# 로 커맨드 라인이 변경된다.

<br>

```bash
Server [localhost]:
Database [postgres]:
Port [5432]:
Username [postgres]:
postgres 사용자의 암호:
psql (11.2)
도움말을 보려면 "help"를 입력하십시오.

postgres=#
```

<br>

### 2. DB 생성

<br>

```bash
CREATE DATABASE <DB이름>;
```

<br>

명령어를 통해 DB를 생성한다.

세미클론을 사용해야 한다.

<br>

### 3. user 생성

<br>

```bash
CREATE USER <아이디> WITH PASSWORD '<비밀번호>' ;
```

<br>

아이디와 비밀번호를 지정해주자.

비밀번호의 경우 작은 따옴표로 감싸줘야한다.

<br>

### 4. 인코딩, isolation, timezone 설정

<br>

```bash
ALTER ROLE <아이디> SET client_encoding TO 'utf8';
ALTER ROLE <아이디> SET default_transaction_isolation TO 'read committed';
ALTER ROLE <아이디> SET TIME ZONE 'Asia/Seoul';
```

<br>

### 5. 데이터베이스 권한 부여



<br>

```bash
GRANT ALL PRIVILEGES ON DATABASE <DB이름> To <아이디>;
```

<br>

### 6. DB 확인

<br>

\\list 명령어를 통해 생성된 DB 목록을 확인해보자.

<br>



## 장고 설정

<br>

### settings.py

<br>

이제 장고에서 설정을 변경해보자.

<br>

장고의 settings.py로 진입합니다.

<br>

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': BASE_DIR / '<DB이름>',
        'USER': '<아이디>',
        'PASSWORD' : '<비밀번호>',
        'HOST' : 'localhost',
        'PORT' : ' '
    }
}
```

<br>

### psycopg2 

<br>

```bash
pip install psycopg2
```

<br>

psycopg2 모듈을 설치해야 장고 환경에서 postgresql 을 사용할 수 있다.

<br>

### migrate

<br>

이제 해당 장고 환경에서 마이그레이션을 해줄 차례다.

<br>

```bash
python manage.py makemigrations
python manage.py migrate
```
<br>


설정에 특별한 문제가 없다면 정상적으로 DB에 마이그레이션 파일대로 테이블이 생성 된다.

