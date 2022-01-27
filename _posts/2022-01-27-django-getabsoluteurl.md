---
title:  "django get_absolute_url"
excerpt: "장고 reverse"
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2022-01-27
toc: true
toc_sticky: true
published: true
---

# django get_absolute_url

<br>



장고에서 URL reverse 기능을 제대로 사용할 수 있는 get_absolute_url 기능을 알아보자.

<br>

## 기능

<br>

보통 view나 template 안에서 모델 인스턴스를 통해 특정 페이지로 리다이렉트 하기 위해 사용된다.

<br>

### 작동 원리

<br>

1. 외부에서 URL Reverse로 모델 인스턴스를 전달한다.
2. 모델 인스턴스를 받게 되면 URL Reverse(reverse())에 정의된 대로 해당 모델 클래스에 선언된 get_absolute_url 을 참고한다.
3. get_absolute_url 함수가 실행되며 내부에서 정의된 path name 을 통해 정해둔 url 맵핑을 참고하여 해당 페이지로 이동한다.




<br>




## 사용법


<br>


### models.py

<br>

```python
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return reverse("appname:post_detail", args=[self.pk])

```

<br>

적용하고 싶은 모델 내부에 인스턴스 함수로서 만들어준다.

<br>

### view에서 redirect를 통해 사용하는 경우

<br>

```python

def testview(request):
    post=Post.objects.get(pk=1)
    return redirect(post)

```

<br>

위 코드처럼 모델의 인스턴스를 전달하게 되면 자동으로 get_absolute_url 함수를 호출하여 원하는 페이지로 이동할 수 있다.


<br>



### template 에서 사용

<br>

```html
<a href="{{ post.get_absolute_url }}">포스트 디테일</a>
```

<br>

template에서도 편하게 해당 모델의 인스턴스를 이용하여 직접 get_absolute_url에 접근하는 방식으로 사용 가능하다.



