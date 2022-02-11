---
title:  "django Queryset json 직렬화"
excerpt: "DRF를 사용하지 않고 직렬화를 해보자"
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2022-02-11
toc: true
toc_sticky: true
published: true
---


# django Queryset을 json 으로


<br>


장고에서 일반적으로 ORM을 통해 데이터를 조회하게 되면 Queryset objects 형태로 데이터를 반환한다.


<br>



일반적인 queryset 형태는 전처리 없이 json 직렬화가 되지 않는다.

<br>


queryset을 json 형태로 변환하는 방법을 알아보자.

<br>


# 사용자 정의 함수 사용


<br>



json이란 사실상 문자열로만 이루어진 딕셔너리의 형태라고 생각하면 이해하기 쉽다.

<br>


물론 정확한 예시는 아니다.

<br>


json과 딕셔너리는 몇가지 차이가 존재하지만 해당 부분은 다른 글에서 다뤄보겠다.

<br>


우선 간단한 모델을 정의해보자.


<br>



```python
class Post(models.Model):
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    category = models.CharField(max_length=20)
    title = models.TextField(max_length=40)
    content = models.TextField(max_length=300)
```


<br>



그리고 해당 모델 쿼리셋을 딕셔너리 형태로 변환할 함수 (serializer)를 정의해보자.


<br>



``` python
import json

def post_serializer(post_queryset):
    
    dic = {}
    dic['author'] = post_queryset.author
    dic['category'] = post_queryset.category
    dic['title'] = post_queryset.title
    dic['content'] = post_queryset.content
    json_dic = json.dumps(dic)
    
    return json_dic
    
```

<br>


해당 함수는 다음과 같이 사용한다,

<br>


```python

post =Post.objects.get(pk=1)

json_post = post_serializer(post)
```



<br>




## django serializer 사용



<br>


일반적인 경우에 가장 흔하게 사용할 수 있는 방법이다.


<br>



```python
from django.core import serializers

post_list = Post.objects.filter(pk = 1)
json_post = serializers.serialize('json', post_list)
```

<br>


아주 간단하게 json화 할 수 있다.

<br>


주의할 점은 장고의 기본 serializer는 iterable 한 객체만을 받는다.

<br>


get을 사용하면 iterable한 객체를 반환하지 않기 때문에 사용할 수 없다.


<br>



## values 함수 사용

<br>


ORM 에서 values 함수를 사용하게 되면 queryset이 아닌 딕셔너리 형태로 해당 객체를 반환한다.

<br>


```python
post = Post.objects.get(pk=2).values()

json_post = json.dumps(post)
```

<br>
