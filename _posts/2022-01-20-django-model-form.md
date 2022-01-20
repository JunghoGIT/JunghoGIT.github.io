---
title:  "django model form"
excerpt: "모델 폼을 이용하여 form 생성 "
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2022-01-20
toc: true
toc_sticky: true
published: true
---

# Django Model Form

<br>

## Form

<br>

- 장고에서 form은 매우 중요한 역할
- 본인 생각이지만 장고의 디자인 패턴은 MTV+F(폼)+S(시리얼라이저) 라고 생각한다.

<br>

### form 의 기능

<br>

- html form 생성 
  - html 에서 form 태그 없이 장고의 탬플릿 태그로 django form 을 이용해 html form 을 만들 수 있다.
- 유효성 검사
  - 폼에 입력된 값에 대해서 유효성을 검사할 수 있다.
  - 유효성 검사 기준을 정의할 수 있다.
  - 유효성에 만족하는 값을 사전타입으로 제공한다.

<br>

## model form 구현


<br>


### 모델 생성

<br>

모델 폼은 모델을 기반으로 폼을 생성하기 때문에 모델이 필수로 필요하다.

<br>

```python
#models.py

from django.db import models
from django.urls import reverse

class Note(models.Model):
    title = models.TextField(max_length=20)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note:note_detail', args=[self.pk])
    
```

<br>

### model form 생성

<br>

만들어둔 모델을 기반으로 폼을 만들어보자.

<br>

```python
from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model= Note
        fields =[
            'title','content',
        ]
```

<br>

일반 폼에서는 메타 클래스를 지정 안 해줘도 되지만 모델 폼에서는 메타클래스를 통해 해당 모델과 

입력할 필드를 지정해줘야 한다.

<br>

필드는 '\__all__' 로 지정해주면 전체 필드를 폼으로 만들겠다는 뜻이다.

하지만 일반적인 경우 유저필드처럼 개인이 변경하거나 생성하면 안되는 폼이 있다보니 개발단계에서 적절하게 설정해야한다.

<br>

또한 일반 폼에서는 개별 필드별로 폼 타입을 폼 클래스를 통해 설정해줘야 한다.

모델 폼에서는 지정된 모델의 필드 타입에 따라 폼 타입이 설정된다.

<br>

### views 함수 생성


<br>


```python
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            # 유저 정보를 받는 경우
            # note = form.save(commit=False)
            # note.author = request.user / 로그인 되어 있을 경우 리퀘스트 유저정보 이용
            # note.save()
            return redirect(note) 
    else :
        form = NoteForm
    return render(request, 'note/note_create.html',{
        'form' : form
    })
```

<br>

view 함수를 만들어 준다.

<br>

폼의 경우 post 방식으로 request가 오는 특성을 이용해 함수의 분기를 나눠준다.

만약 폼이 작성되어 정상적으로 submit 됐을 경우 if 문안에서 request의 post를 인수로 Note폼 클래스를 저장해준다.


그리고 유효성 검사 후 통과한다면 폼을 모델 객체로 해서 저장한다.

<br>

그 외의 경우라면 GET 방식이기 때문에 그냥 form 형식만을 전달하여 탬플릿으로 보낸다.

<br>

### template 생성



```html
{% raw %}
<div style="margin-left: 5rem">
    <form action="" method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="저장">
    </form>
</div>
{% endraw %}

```

<br>

form.as_p 를 통해 아주 쉽고 간단하게 html 폼을 만들 수 있다.

csrf_token 은 장고에서 폼을 사용할 때 필수적으로 사용해야 한다. 

사용하지 않는다면 오류가 발생한다. (settings 에서 설정을 변경할 수 있으나 보안을 위해 사용해야함)

항상 폼 태그 직후에 작성해주면 된다.

<br>

as_p 외에도 as_table, as_ul 등의 옵션을 사용가능하다.

부트스트랩 폼도 당연히 사용 가능 !









