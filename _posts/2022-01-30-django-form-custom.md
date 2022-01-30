---
title:  "django form에서 외부 값 참조"
excerpt: "validator custom"
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2022-01-30
toc: true
toc_sticky: true
published: true
---

<br>

# form에서 유효성 검사를 위해 외부 값 참조하기

<br>

개인 프로젝트 도중 form 의 유효성 검사를 위해 validator 에서 form 을 보내는 유저의 정보가 필요한 경우가 발생했다.

<br>

문제는 어떤 유저가 보낼지 모르기 때문에 User 모델을 가져와서 사용하는 것 자체가 의미가 없었다.

<br>

구글링도 하고 공식 문서를 찾아보던 중 답을 찾았다.


<br>


##  1. form 수정

<br>

우선 모델폼을 수정해보자.

<br>

Order form 모델은 장고 auth user model 을 foreign key 로 갖는 user 필드를 갖고 있다.

> 프로젝트에서 실제 사용한 코드는 너무 방대하여 포스팅을 위해 일부 생략함

<br>

```python
from .models import Order
from django import forms
from django.contrib.auth import get_user_model



class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [            
            'order_price',
            'amount',
        ]

    def __init__(self, user, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_amount = self.cleaned_data['amount']
        cleaned_order_price = self.cleaned_data['order_price']
        cleaned_user = get_user_model().objects.get(pk = self.user.pk)
        user_money = cleaned_user.money
        deposit = round(cleaned_amount*cleaned_order_price,2)

        if cleaned_position == 'buy':
            if deposit >= user_money:
                raise forms.ValidationError("구매에 필요한 돈이 보유한 돈 보다 많습니다.")
            else :
                return self.cleaned_data



```

<br>

위의 코드처럼 생성자를 오버라이딩 하여 인스턴스 변수를 만들 수 있도록 코드를 수정해주자.

상속받은 부모 클래스(form.modelform) 생성자 super함수를 통해 불러온다.

 <br>

이렇게 하면 view에서 form 인스턴스가 생성 될 때에 user 인스턴스 변수도 생성됨에 따라 내부에 정의한 validator 에서 해당 변수를 이용해 유효성 검사를 정의할 수 있다.


<br>


## 2. view 수정

<br>

view에서는 form 객체를 생성하는 부분에서 인수로 원하는 값을 주면 된다.

<br>

```python
.
.
.

def orderview(request):
    order_form = OrderForm(request.user,request.POST)
    .
    .
    .
    return redirect(order)
.
.
.

```


<br>


## 요약


<br>


1. 원하는 인스턴스 변수가 생성되도록 생성자를 재정의
2. 인스턴스 객체를 만들 때 인스턴스 변수가 생성되도록 인수를 전달

<br>

매우 간단하다.

<br>

이걸 공부하면서 느낀 점은 프레임워크의 내장 기능을 잘 이용하는 것도 좋은 개발이지만, 그것보다 근본적으로 언어를 제대로 이해한다면 프레임워크을 더 다양하게 수정 가능하다는 것이다.

<br>

단순하지만 간지가 나는 코드를 짜고 싶다.