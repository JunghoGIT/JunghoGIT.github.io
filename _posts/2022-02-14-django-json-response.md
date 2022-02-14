---
title:  "django json Response"
excerpt: "json 형태의 data를 응답"
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2022-02-14
toc: true
toc_sticky: true
published: true
---

# django json으로 응답하는 방법


<br>


장고에서 api를 설계할 때 요청에 대해 json 으로 응답하는 방법은 대표적으로 2가지가 있다.

<br>

매우 간단하니 알아보자.


<br>


## JsonResponse


<br>


장고의 http 모듈안에 존재하는 JsonResponse를 사용해보자.

<br>



```python
from django.http import JsonResponse
from django.core import serializers
from .models import Post

def post_detail(request,pk):    
    post = Post.objects.get(pk=pk)
    json_post = serializers.serialize('json', post)
    
    return JsonResponse(json_post)
    
    
```


<br>


## HttpResponse

<br>

마찬가지로 장고의 http 모듈안에 존재하는 HttpResponse를 사용해보자.

<br>

```python
from django.http import HttpResponse
from django.core import serializers
from .models import Post

def post_detail(request,pk):    
    post = Post.objects.get(pk=pk)
    json_post = serializers.serialize('json', post)
    
    return HttpResponse(json_post,content_type="text/json-comment-filtered")
    
```

<br>

JsonResponse와 다른 점은 content_type 속성을 통해 json 형태로 보낼 것임을 설정하면 된다.

<br>



## 주의할 점

<br>

python의 딕셔너리를 이용해 일반적으로 json 형태로의 변환이 매우 수월하다.

<br>

하지만 장고에서 queryset은 딕셔너리 객체가 아니다.

<br>

위처럼 queryset을 응답하기 위해선 꼭 딕셔너리화 또는 json 직렬화 해주는 작업을 거쳐야 한다.

<br>

queryset을 json 형태로 변환하는 법은 이전 포스팅을 확인해보길 바란다.