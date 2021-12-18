---
title:  "[Error] Related Field got invalid lookup: icontains"
excerpt: "Foreignkey 관련 에러"
categories:
 - Djagno
tags:
 - [Django,python,study,TIL,Error]
last_modified_at: 2021-12-18
toc: true
toc_sticky: true
---


# [error]  Related Field got invalid lookup: icontains





django 에서 admin 페이지에  모델 검색기능을 추가하는 과정에서 발생한 에러이다.



두 모델의 구조는 다음과 같았다.



```python
from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return "질문"+str(self.id)+" "+str(self.question)+" 의 답변"

```



Answer 모델의 question 필드가 Question의 subject 를 외래키로 받는다.



그리고 검색 기능을 추가한 admin.py 코드는 다음과 같았다.



```python
from django.contrib import admin
from.models import Question,Answer

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['question']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
```



Question 모델의 경우 검색이 정상적으로 동작하였지만 Answer 모델은 검색 했을 때 

Related Field got invalid lookup: icontains 에러가 발생했다.



## 원인



원인은 간단했다.

외래키를 사용했을 경우 검색 필드가 값을 가져오기 위해서 

Answer 모델의 question 필드 -> Question 모델에서 해당 question 의 subject필드 

로 찾아가야 하는데 question 이라고만 값을 주니 길을 잃어버린 것이다.



## 해결



외래키에 대한 정보를 살짝 알려주면 에러가 해결되고 길을 잘 찾아간다.





```python
class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['question__subject']

```



필드명 뒤에 연결된 모델의 필드명을 알려주면 해결된다.



에러 해결 완료~!