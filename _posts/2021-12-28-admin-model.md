---
title:  "admin 페이지에서의 model"
excerpt: "model 페이지를 디자인하고 관리해보자."
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2021-12-28
toc: true
toc_sticky: true
---

# 관리자 페이지에서 model 관리하기



장고의 기본 app인 admin을 이용하면 model을 쉽게 관리 할 수 있다.



기본적인 CRUD 기능을 제공하며 그 외에도 admin.py 를 통해 다양한 기능을 추가 할 수 있다.





## model 생성





설명을 위해 간단한 모델을 하나 만들어주자.



```python
# models.py

# ...
# ...

class Person(models.Model):
    name =models.CharField(max_length=10)
    age = models.IntegerField()
    address = models.TextField()
    school = models.TextField()

```

```bash
python manage.py makemigrations

python manage.py migrate
```



## 관리자 페이지에 모델 admin 추가



모델을 생성한 후에 관리자 페이지에 접속하여도 모델 목록은 볼 수 없다.

admin.py 에 모델 admin을 추가해줘야 한다.



방법은 여러가지가 있지만 나는 코드의 확장성이 좋은 데코레이터+클래스 방식으로 추가해보겠다.



```python
#admin.py

from django.contrib import admin
from .models import Person



@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass

```



이제 관리자 페이지를 보면 좌측에 해당 모델에 대한 메뉴가 생겼다.



## 데이터 생성



관리자 페이지에서 해당 모델의 옆에 추가 버튼을 눌러서 간단하게 데이터를 생성할 수 있다.

데이터를 생성해서 저장하게 되면 바로 DB에 저장이 된다.



## 데이터 리스트 변경



좌측 메뉴에서 모델을 클릭하면 해당 모델에 대한 데이터 목록이 출력된다.



![admin_model_1](C:\Users\jungho\Desktop\github rapository\JunghoGIT.github.io-master\JunghoGIT.github.io\assets\images\django\admin_model_1.JPG)



그런데 보는 것과 같이 모델명 + object + (index) 로 리스트가 출력된다.

안에 내용에 대해서 확인이 어려우니 바꿔보자



### def \__str__(self):



간단하게 \__str__ 을 이용하여 변경 할 수 있다.



```python
# models.py

#...
#...
#...

class Person(models.Model):
    name =models.CharField(max_length=10)
    age = models.IntegerField()
    address = models.TextField()
    school = models.TextField()
    
    def __str__(self):
        return self.name

```



위으 코드처럼 객체가 호출 됐을 때 반환하는 이름을 변경해주면 된다.



이젠 원하는대로 이름으로 데이터 리스트가 출력되지만 만족할 수 없다.

다른 데이터 속성들도 한 화면에서 확인하고 싶다.



이땐 admin.py 에서 `list_display` 속성을 이용해서 변경해줄 수 있다.



### list_display



```python
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name','age','address','school']
```



리스트형식으로 해당 모델 필드명을 요소로 넣어주면 된다.



이제 확인해보면 설정한대로 출력된다.



### list_display_links



지금은 Name 필드에만 데이터 수정 페이지로의 링크가 활성화 되어있는데 해당 옵션은

list_distplay_links 속성으로 설정해줄 수 있다.



```python
#admin.py

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name','age','address','school']
    list_display_links = ['name','age']
```



결과를 확인해보자 .



![admin_model_2](C:\Users\jungho\Desktop\github rapository\JunghoGIT.github.io-master\JunghoGIT.github.io\assets\images\django\admin_model_2.JPG)





## 검색 기능 구현







이번엔 해당 페이지에서 검색기능을 구현해보자.

지금이야 데이터가 적어서 필요성을 못 느끼지만 실제 서비스에선 엄청난 데이터가 생길 것이다.



```python
#admin.py

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name','age','address','school']
    list_display_links = ['name','age']
    search_fields = ['name']
```



다음과 같이 `search_fields` 속성을 추가해주는 것 만으로 검색 기능을 구현할 수 있다.

리스트에 넣어준 모델의 필드명에 대해서만 검색을 한다.



## 새로운 필드 추가 



기존 모델에는 존재하지 않지만 admin 클래스 안에서 코드를 작성하여 가상의 필드를 추가할 수 있다.



이름의 길이 필드를 한번 만들어보자.



```python
# admin.py

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name','name_length','age','address','school']
    list_display_links = ['name','age']
    search_fields = ['name']

    def name_length(self,Person):
        return len(Person.name)
```



해당 코드처럼 함수에 인자로 해당 모델명을 설정해주면 된다.

그리고 list_display 의 요소로 해당 함수명을 입력해주면 데이터 별로 return 값이 출력된다.