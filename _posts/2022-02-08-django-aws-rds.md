---
title:  "django AWS RDS(Mysql) 연동하기"
excerpt: "AWS rds 서비스를 사용해보자"
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2022-02-08
toc: true
toc_sticky: true
published: true
---

# django AWS RDS 연동하기 (Mysql)


<br>


장고의 데이터 베이스를 aws의 rds 서비스를 이용해 mysql DB와 연동해보자.


<br>


## AWS RDS 인스턴스 생성


<br>


우선 AWS 계정이 존재해야 한다.


<br>


AWS에서 RDS를 검색하여 해당 서비스로 이동한다.


<br>


![rds_1](\assets\images\django\rds_1.JPG)

<br>

데이터 베이스 생성 버튼을 클릭한다.

<br>

![rds_2](\assets\images\django\rds_2.JPG)

<br>

표준생성 옵션과 사용할 DB를 선택해준다.

<br>

**주의 ! 모든 DB가 프리티어가 적용되는 것이 아니다. Postgresql 의 경우 프리티어가 적용되지 않기 때문에 사용 요금이 청구된다. ** 

<br>

![rds_3](\assets\images\django\rds_3.JPG)

<br>

인스턴스 이름과 DB의 마스터 사용자에 대한 유저 정보를 설정한다.


<br>


![rds_4](\assets\images\django\rds_4.JPG)

<br>

연결 설정 부분에서 꼭 !! 퍼블릭 엑세스를 허용하자.

허용하지 않을 경우 VPC에서 인바운드를 허용하더라도 외부에서 접근이 불가능하다.

<br>

그 외 부분은 dafalut 설정으로 생성해도 큰 문제 없이 DB 인스턴스가 생성된다.

<br>

## python settings 설정


<br>


```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '인스턴스 명',
        'USER': '유저명',
        'PASSWORD' : '비밀번호',
        'HOST' : '엔드포인트',
        'PORT' : '3306',
    }
}

```
<br>


엔드포인트는 AWS에서 생성된 인스턴스의 상세페이지에서 연결 & 보안 탭에서 확인할 수 있다.




<br>




## 에러 해결 or 방지 세부 설정

<br>

위의 과정을 모두 마쳤다면 거의 대부분의 작업은 끝났지만 만약 runserver 하게 된다면 에러를 마주칠 것이다.


<br>






### Error loading MySQLdb module.

<br>

위 에러는 mysql 모듈이 설치되지 않아서 발생하는 에러이다.

<br>

postgresql 에서 psycopg2 패키지를 설치하여야 해당 DB를 사용할 수 있듯이 mysql도 별도의 패키지를 설치하여야 한다.

<br>

```python
pip install Mysqlclient
```



위 명령어로 해당 패키지를 설치해주자


<br>


### (2002, "Can't connect to server on '엔드포인트' (10060)")

<br>

위 에러는 해당 DB로 접근 실패했을 때 발생하는 에러이다.

<br>

원인은 두 가지이다. 

퍼블릭 엑세스를 허용하지 않았거나 vpc 인바운드 규칙을 설정하지 않았거나.

<br>

퍼블릭 엑세스의 경우 생성할 때 설정하지 못했다면 인스턴스 수정에 들어가서 해당 부분을 허용으로 체크해주면 된다.

<br>

인바운드 규칙의 경우 인스턴스의 보안그룹 상세페이지에서 수정이 가능하다.

<br>

아래의 사진과 같이 설정해주자.



![rds_5](\assets\images\django\rds_5.JPG)





### (1049, "Unknown database 'DB이름' ")

<br>

이 에러는 DB를 찾을 수 없어서 나타나는 에러이다.

<br>

사실상 DB 인스턴스는 만들었지만 스키마가 존재하지 않기 때문에 장고에서 접근할 DB를 찾지 못하는 것이다.

<br>

우선 편한 작업을 위해 mysql GUI 중 하나인 workbrench를 설치하자.

<br>

[https://dev.mysql.com/downloads/workbench/](https://dev.mysql.com/downloads/workbench/) 링크에서 설치 가능하다.

<br>

설치후 메인 홈 화면에서 My SQL Connetions 옆에 + 표시를 클릭하면 아래와 같은 창이 나온다.





![rds_6](\assets\images\django\rds_6.JPG)

<br>

커넥션 네임에는 인스턴스 명을 적어주자 (다른 이름도 가능)

<br>

그리고 인스턴스를 생성할 때 설정한 유저 정보를 기입후 OK를 해당 인스턴스와 연결된다.

<br>

연결 후에는 우리가 사용할 실제 DB를 안에 생성해주면 된다.

<br>

![rds_7](\assets\images\django\rds_7.JPG)

<br>

1번을 누르면 2번의 스키마를 생성하는 폼이 나오고 폼을 채운후 3번을 눌러 적용 시킨 후 4번의 스키마탭을 눌러 완성된 DB를 확인할 수 있다.

<br>

끝으로 마이그레이션을 해주면 된다 !