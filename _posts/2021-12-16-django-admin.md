---
title:  "Django 관리자"
excerpt: "admin 페이지를 둘러보자"
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2021-12-16
toc: true
toc_sticky: true
---

# django 관리자

> ***이 글은 박응용 님의 wikidocs 의 [점프 투 장고](https://wikidocs.net/70718) 교재를 학습하며 작성한 글 입니다.***



django 는 관리자(admin) 기능을 기본으로 포함하고 있다.

해당 기능을 통해 우리의 app을 다양한 방법으로 관리 할 수 있다.



## 슈퍼유저 생성



우선 관리자화면에 접속할 수 있는 슈퍼유저를 생성해보자



```bash
(venv) C:>python manage.py createsuperuser
Username: admin
Email address: wjdgh8926@naver.com
Password:
Password (again):
Superuser created successfully.

```



**python manage.py createsuperuser** 명령어를 통해 계정을 생성할 수 있다.

비밀번호는 자동으로 가려져서 입력이 안 되는 것처럼 보이는 것 뿐이니 나의 손가락을 믿고 비밀번호를 잘 입력해해보자.



## 관리자 페이지



이제 관리자 페이지를 이용해보자

과거 프로젝트 디렉토리의 urls.py 에서 봤듯이 admin url은 기본적으로 맵핑이 되어있다.



서버를 구동한 후 http://localhost:8000/admin/ 주소로 들어가보자.



로그인 화면이 나오는데 방금 만든 슈퍼유저 계정으로 로그인 한다면 관리자 페이지를 볼 수 있다.



 

## 모델 관리



관리자 페이지에서 전에 만들었던 모델을 추가해보자.



app디렉토리내부에 admin.py 에서 하단 코드를 추가해보자.





```python
from django.contrib import admin
from.models import Question,Answer

admin.site.register(Question)
admin.site.register(Answer)
```



코드를 입력한 후 관리자 페이지를 확인해면 해당 app에 대한 모델 메뉴가 생성이 되었다.

이 화면에서 각 모델들을 CRUD 할 수 있다.





## 모델 검색 기능 추가



지금이야 모델(데이터)가 현저히 적지만 많다면 하나하나 찾는 것이 힘들 것이다.



관리자 페이지에서 질문 모델을 검색할 수 있는 기능을 추가해보자.



admin.py 코드에 해당 내용을 추가해보자.



```python
from django.contrib import admin
from.models import Question,Answer

def QuestionAdmin(admin.ModelAdmin):
    search_fileds = ['subject']

admin.site.register(Question)
admin.site.register(Answer)
```



짜잔 검색기능이 추가 된 것을 알 수 있다.