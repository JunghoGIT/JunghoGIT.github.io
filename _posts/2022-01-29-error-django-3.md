---
title:  "django didn't return an HttpResponse object"
excerpt: "http response를 반환하지 않을 때 발생하는 에러"
categories:
 - Django
tags:
 - [Django,python,study,TIL,Error]
last_modified_at: 2022-01-29
toc: true
toc_sticky: true
published: true
---

# [Error] didn't return an HttpResponse object

<br>



## 에러 발생

<br>

개인 프로젝트를 하면서 특정 form 제출에 대한 유효성 검사를 테스트 하고 있었다.

<br>

나는 분명 내가 설계한대로 특정 조건에 대한 validator 를 만들었는데 그 조건에 해당 되는 form 을 post로 요청할 때마다 `didn't return an HttpResponse object` 에러가 발생했다.


<br>


## 에러 원인

<br>

다행히 어떤 조건에 저 에러가 발생하는지 분명했기 때문에 고려해야할 부분은 많지 않았다.

<br>

우선 첫번째로 내가 작성한 form 의 validator 코드를 확인해봤다. 

<br>

코드에도 딱히 문제는 없었고 다른 조건들에선 문제 없이 동작했기 때문에 금방 form의 문제가 아니란 것도 알 수 있었다.

<br>

이후엔 해당 요청을 처리하는 view를 확인했다.

<br>

에러메시지에 답이 있다고 했던가 에러 메시지 그대로 return 한 response가 없어서 그런 것이었다.

<br>

흔히 있는 실수지만 if문이 여러번 중첩되고 그 if문에서 분기가 나뉨에 따라 else 문을 적절한 순서에 배치하지 못한 탓이었다.

<br>

## 에러 해결

<br>



```python
def example(request):
    if request.method == 'POST':
        form = EXForm(request.POST)
        if form.is_valid():
            blahblah
          	return ...
        else : # 폼이 유효하지 않을 때에도 response를 확실히 해줘야 함
            return ...
```


<br>


form 을 사용한 view를 작성할 때에 위의 코드처럼 유효하지 않을 때에 대한 예외처리를 분명하게 해줘야 한다.

<br>

암튼 앞으로 해당 에러가 발생하면 무조건 특정 조건에 return 값이 없는지 확인해보자 !


<br>
