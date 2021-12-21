---
title:  "[Error] Answer matching query does not exist."
excerpt: "쿼리 매칭 실패 에러"
categories:
 - Django
tags:
 - [Django,python,study,TIL,Error]
last_modified_at: 2021-12-21
toc: true
toc_sticky: true
---

#  [Error] Answer matching query does not exist.



## 에러 발생



점프 투 장고를 학습하던 도중 교재와 다르게 질문 상세 페이지 하단에 질문에 맞는 답변도 출력을 하고 싶었다.



그래서 탬플릿과 뷰 코드를 수정하였다.

```python
# views.py
def detail(request, question_id):

    if Answer.objects.get(id=question_id) :
        answer = Answer.objects.get(id=question_id)
        question = Question.objects.get(id=question_id)
        context = {'question': question, 'answer': answer}
        return render(request, 'community/question_detail.html', context)
    else:
        question = Question.objects.get(id=question_id)
        context = {'question': question}
        return render(request, 'community/question_detail.html', context)
```



```html
{% raw %}
<!-- question_detail.html -->

<p style="font-size:50px"> 질문 </p>
<h1>{{ question.subject }}</h1>

<div>
    {{ question.content }}
</div>
<br>
<div>{{question.create_date}}</div>
<br> --------------------------<br>
{% if answer %}
<p style="font-size:50px"> 답변 </p>
<div>{{answer.content}} </div>
<br>
<div>{{answer.create_date}} </div>
{% else %}
<br>답변이 존재하지 않습니다.<br>
{% endif %}
{% endraw %}
```



탬플릿 태그를 이용해서 HTML 에 Answer에가 존재 하지 않을 때의 조건을 고려했다.

질문 모델의 id와 대응되는 답변이 존재한다면 정상적으로 출력이 됐지만 문제는 질문만 있고 대응되는 답변이 없을 땐 에러가 발생했다.



![queryset_error_1](C:\Users\jungho\Desktop\github rapository\JunghoGIT.github.io-master\JunghoGIT.github.io\assets\images\jumptodjango\queryset_error_1.JPG)



## 에러 원인



에러 원인을 찾기 위해 django shell 에서 queryset 을 사용해봤다.



```bash
>>> from community.models  import Answer
>>> Answer.objects.get(id=3)

Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\jungho\Desktop\github rapository\jumptodjango\venv\lib\site-packages\django\db\models\manager.py", line 85, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Users\jungho\Desktop\github rapository\jumptodjango\venv\lib\site-packages\django\db\models\query.py", line 439, in get
    raise self.model.DoesNotExist(
community.models.Answer.DoesNotExist: Answer matching query does not exist.
```



결과를 보니 에러의 원인은 queryset 을 사용해서 데이터를 가져올 때 매칭되는 데이터가 없다면 None이나 False를 반환하는 것이 아니라 Error를 발생시켯다.



## 에러 해결



원인은 존재 하지 않는 데이터에 대한 질의가 에러를 발생시키니 존재하는 값에 대해서만 조회를 하게 만들면 된다.



간단하게 if문에서 인자로 받은 question_id 가 Answer 에도 존재하는지를 확인하면 된다 생각했는데 이게 생각보다 간단하지 않았다.



django 에서는 ORM 을 사용하기 때문에 모델의 필드 값을 queryset 객체의 형태로 가져온다.



```bash
{% raw %}
>>> Answer.objects.values('question_id')
<QuerySet [{'question_id': 1}, {'question_id': 3}]>

>>> Answer.objects.values_list('question_id')
<QuerySet [(1,), (3,)]>
{% endraw %}

```



values 와 values_list 모두 queryset 객체의 리스트 형태로 반환을 했는데 문제는 안에 요소들이 전처리 없이는 비교가 불가능한 상태였다.



value_list 의 경우 튜플 요소가 (1,) 처럼 None 값까지 포함하고 있어서 비교가 쉽지 않다.

그래서 values 를 통해 queryset을 가져오고 list로 변환한 후 딕셔너리의 키를 이용해 값을 가져오는 방식을 선택했다.



```python
# views.py

def detail(request, question_id):

    templist = list(Answer.objects.all().values('id'))
    temp_answer_id = []
    for i in range(0,len(templist)):
        temp_answer_id.append(templist[i]['id'])

    if question_id in temp_answer_id :
        answer = Answer.objects.get(id=question_id)
        question = Question.objects.get(id=question_id)
        context = {'question': question, 'answer': answer}
        return render(request, 'community/question_detail.html', context)
    else:
        question = Question.objects.get(id=question_id)
        context = {'question': question}
        return render(request, 'community/question_detail.html', context)
```



간단하게 성공했다. (사실 해결하는데 1시간 정도 걸림 ㅜ )



queryset은 SQL을 대신하는 좋은 기능이지만 고려해야할 부분이 많다는 것을 깨달았다.



끝.

