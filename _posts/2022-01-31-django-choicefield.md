---
title:  "django Choice Field 만들기"
excerpt: "선택 목록 만들기"
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2022-01-31
toc: true
toc_sticky: true
published: true
---

# django choice field 만들기 

<br>

form을 만들다보면 유저가 마음대로 값을 입력하는 것이 아닌 개발자가 원하는 값 중에서 선택하도록 만들 상황이 있다.

<br>

다양한 방법이 있지만 내가 애용하는 간단한 방법을 소개해보겠다.

<br>

## form 


<br>


```python
class OrderForm(forms.ModelForm):
    position_choice =[
        ('buy','매수'),
        ('sell','매도'),
    ]
    position = forms.ChoiceField(widget=forms.Select, choices=position_choice)

    class Meta:
        model = Order
        fields = [
            'position',
            'order_price',
            'amount',
        ]
```

<br>

1. 폼 객체 안에 두 개의 값으로 이루어진 튜플을 요소로 갖는 리스트를 만들어준다.
   - 튜플에서 두개의 값 중 첫 번째 값은 실제 DB에 저장되어지는 값을 의미한다.
   - 두 번째 값은 클라이언트에서 유저에게 보여지는 값을 의미한다.
2. `forms.ChoiceField` 로 필드를 만들어준다.
   - widget : for<br>m 의 input type 을 설정한다.
   - choices : 위에 만들어둔 리스트를 줌으로서 위젯에서 쓰일 선택 목록을 준다.
3. fields에 만든 ChoiceField 이름을 추가한다.


<br>






