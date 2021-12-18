---
title:  "Django Model 기본 사용법"
excerpt: "Model CRUD"
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2021-12-16
toc: true
toc_sticky: true
---

# 모델 사용하기

> ***이 글은 박응용 님의 wikidocs 의 [점프 투 장고](https://wikidocs.net/70718) 교재를 학습하며 작성한 글 입니다.***



## 데이터 생성



django shell 을 통해 모델을 사용해보자.



```bash
(venv) C:>python manage.py shell
Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>

```



shell 명령어를 통해 django shell로 진입할 수 있다.



```bash
>>> from community.models import Question, Answer
>>> from django.utils import timezone
>>> q = Question(subject='첫 커뮤니티 제작한 기분은 ?', content='윤정호님의 기분이 궁금해영', create_date=timezone.now())
>>> q.save()
>>> q.id
1

```



그리고 위의 shell에서 python 코드를 작성하듯이 명령어를 입력해주면 된다.

django 내에선 SQL문을 거의 안 쓴다고 보면 된다. 

DB에 직접적으로 접근하지 않으며 모델 객체로 ORM 방식을 이용하여 DB와 데이터를 주고 받는다.



위 코드에서도 SQL문 하나 없이 모델 객체만을 사용하여 데이터를 생성할 수 있다.

 

```bash
>>> q = Question(subject='장고를 어떻게 평가하나용?',content='윤정호님의 장고에 대한 생각이 궁금합니다.' ,create_date=timezone.now())
>>> q.save()
>>> q.id
2

```

하나의 데이터를 더 만들어보았다.



## 데이터 조회



각 데이터 모델은 데이터 모델명.objects.all()명령어를 통해 해당 모델이 포함하고 있는 전체 객체(데이터)를 확인할 수 있다.



```bash
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>, <Question: Question object (2)>]>

```



인덱스 넘버와 함께 객체에 대한 정보가 출력된다.

인덱스 넘버가 아니라 특정 칼럼에 대한 정보로 데이터를 확인하고 싶다면

 model.py 에서 \__str__ 함수를 통해 설정할 수 있다.



```python
class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject
```

```bash
>>> from community.models import Question,Answer
>>> Question.objects.all()
<QuerySet [<Question: 첫 커뮤니티 제작한 기분은 ?>, <Question: 장고를 어떻게 평가하나용?>]>
>>>

```

shell 을 재시작 후에 다시 확인해보면 설정한 칼럼명 기준으로 출력되는 것을 확인할 수 있다.



**모델에 함수가 추가되었을 때는 migrate 명령이 필요 없다 **



```bash
>>> Question.objects.filter(id=1)
<QuerySet [<Question: 첫 커뮤니티 제작한 기분은 ?>]>
>>> Question.objects.get(id=1)
<Question: 첫 커뮤니티 제작한 기분은 ?>
>>> Question.objects.filter(subject__contains='장고')
<QuerySet [<Question: 장고를 어떻게 평가하나용?>]>

```



그리고 filter와 get 함수를 통해 조회가 가능하다.

여기서 중요한 점은 한 개의 데이터만 조회할 때만 get함수가 사용 가능하다.



filter 에 대한 공식문서는 아래 링크에서 확인해보자.

[https://docs.djangoproject.com/en/3.0/topics/db/queries/](https://docs.djangoproject.com/en/3.0/topics/db/queries/)



연결된 모델끼리의 조회의 경우

부모객체변수.자식모델명_set.all() 함수를 통해 외래키로 연결된 모든 것들을 조회할 수 있다.



## 데이터 수정



이제 데이터를 수정해보자. 데이터 수정또한 간단하다.



```bash
>>> q= Question.objects.get(id=1)
>>> q
<Question: 첫 커뮤니티 제작한 기분은 ?>

>>> q.subject = '오늘 기분 어떠십니까'
>>> q
<Question: 오늘 기분 어떠십니까>

>>> q.save()
>>> Question.objects.all()
<QuerySet [<Question: 오늘 기분 어떠십니까>, <Question: 장고를 어떻게 평가하나용?>]>




```



위처럼 객체를 변수에 저장하여 값을 변경할 수 있다.

q 에는 정보가 복사 되는 구조가 아니라 해당 데이터에 접근하는 포인터가 되는 거라고 이해하면 편하다.



## 데이터 삭제



데이터 삭제 또한 마찬가지로 변수에 조작하길 원하는 객체를 불러와 저장하고 해당 변수를 통해 조작하면 된다.



```bash
>>> q = Question.objects.get(id=2)
>>> q
<Question: 장고를 어떻게 평가하나용?>

>>> q.delete()
(1, {'community.Question': 1})

>>> Question.objects.all()
<QuerySet [<Question: 오늘 기분 어떠십니까>]>
>>>

```

위 코드로 간단하게 데이터를 지우고 지워진 데이터를 확인할 수 있다.