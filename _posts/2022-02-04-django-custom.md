---
title:  "django allauth custom"
excerpt: "소셜 로그인을 내 입맛대로 !"
categories:
 - Django
tags:
 - [Django,python,study,TIL,allauth]
last_modified_at: 2022-02-04
toc: true
toc_sticky: true
published: true
---

# django allauth 커스텀하여 사용하기

<br>

django allauth 라이브러리를 통해 우리는 손 쉽게 소셜 로그인을 구현할 수 있다.

<br>

하지만 allauth의 view 로직이나 template 구조는 실제 서비스에서 사용하기에는 allauth만의 형식이 너무 강하다.

<br>

나의 서비스에 맞게 allauth를 커스텀하여 사용해보자.

<br>

너무 좋은 듀토리얼 글이 많기에 본 글에서는 allauth로 소셜 로그인을 구현하는 부분은 생략하여 작성하겠다.


<br>


## Template 커스텀


<br>


allauth를 통해 로그인을 구현하게 되면 해당 url 맵핑에 따라 allauth의 view가 실행되어 allauth내부의 template을 렌더링한다.

<br>

그리고 그 template의 UI는 아주아주 구리다.

사용할 수 없는 수준이다.

<br>

이 template을 수정하는 방법은 크게 두 가지이다.

<br>

1. allauth login view의 template_name 속성 변경
2. django에서 template를 찾는 원리를 이용하는 방법

<br>

이번 글에서는 2번에 해당하는 방식을 통해 커스텀 된 template을 사용하겠다.



<br>

### 1. settings 의 TEMPLATES DIRS 설정

<br>

```python
# settings.py

.
.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'config','templates'),
            os.path.join(BASE_DIR,'config','templates','allauth'),
        ],
        ,
        ,
        
        

```

<br>

우선 장고에서 template를 조회하는 우선 순위를 결정하는 DIRS를 설정해주자.

<br>

해당 설정을 통해 view가 특정 template를 렌더링 할 때에 장고는 설정된 DIRS에서 최우선으로 template을 찾는다.

<br>

### 2. allauth source code

<br>

allauth는 장고로 만들어진 라이브러리이다.

<br>

장고와 동일한 MTV 구조를 가지고 있기 때문에 소스 코드에서 template 디렉토리에 여러 template이 저장되어 있는 것을 확인할 수 있다.

<br>

소스 코드는 가상환경 내부의 라이브러리 폴더나 깃헙 소스 코드에서 확인할 수 있다.

<br>

내가 커스텀하여 사용하고 싶은 html 파일을 복사하여 allauth의 디렉토리 구조와 동일하게 나의 프로젝트 templates 디렉토리에 저장해주자.

<br>

즉 allauth/templates/socialaccount/login.html 파일을 수정하고 싶다면

<settings에 설정한 template경로>/socialaccount/login.html 이런식으로 저장해줘야한다.

<br>

대략적인 원리는 allauth의 view가 login.html 을 렌더링 할 때에 우리가 설정해놓은 폴더에서 우선으로 찾아서 렌더링 해주는 점을 사용하는 것이다.

<br>

그리고 allauth의 view에서 template를 렌더링 할 때에 '경로/템플릿' 포맷으로 경로를 포함한 일반적인 방식으로 사용하기 때문에 allauth의 디렉터리 구조를 지켜서 가져와야 한다.

<br>

## 원하는 View만 사용하기


<br>


설계에 따라 allauth의 url 맵핑이나 view의 로직을 사용하고 싶지 않을 때가 있다.

<br>

예를 들면 로그인페이지 template -> 소셜로그인 template -> 소셜 웹사이트 -> 로그인 의 프로세스가 아니라 로그인 페이지를 건너뛰고바로 소셜로그인을 한다거나, 원하는 특정 url에 특정 로그인 view를 맵핑해주고 싶을 때가 그러하다.

<br>

우선 이글은 socialaccount 로그인 template을 반환하는 view를 사용하는 법을 기준으로 작성합니다.

<br>

다른 경우도 원리는 똑같다.

<br>

나의 경우엔 장고에서 loginrequired 데코레이터를 통해 리다이렉트 했을 경우 곧 바로 소셜 계정 로그인 페이지로 이동하도록 만들고 싶었다.

<br>

하지만 아무리봐도 allauth의 view에는 'socialacccounts/login.html' 을 렌더링 해주는 부분을 찾을 수 없었다.

<br>

내가 해당 페이지를 렌더링 해줬을 땐 페이지의 로그인 기능이 정상적으로 작동하지 않았다..

<br>

결국 소스 코드의 30% 가까이를 읽고나서야 찾을 수 있었다.

<br>

### 1. view 찾기



<br>

나는 노하우가 없어서 힘들게 찾았으나 이글을 읽는 사람들은 그럴 일이 없길 바란다.

<br>

기본적인 view는 allauth/views.py 나 allauth/account 또는 socialaccount/views.py 에 모두 정리되어 있다.

<br>

그리고 소셜 로그인 페이지를 렌더링하는 view는 

<br>

allauth/socialaccount/providers/소셜서비스명/views.py 에 정리되어 있다.

<br>

구글의 경우 코드는 다음과 같다.

<br>

```python
import requests

from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import GoogleProvider


class GoogleOAuth2Adapter(OAuth2Adapter):
    provider_id = GoogleProvider.id
    access_token_url = "https://accounts.google.com/o/oauth2/token"
    authorize_url = "https://accounts.google.com/o/oauth2/auth"
    profile_url = "https://www.googleapis.com/oauth2/v1/userinfo"

    def complete_login(self, request, app, token, **kwargs):
        resp = requests.get(
            self.profile_url,
            params={"access_token": token.token, "alt": "json"},
        )
        resp.raise_for_status()
        extra_data = resp.json()
        login = self.get_provider().sociallogin_from_response(request, extra_data)
        return login


oauth2_login = OAuth2LoginView.adapter_view(GoogleOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(GoogleOAuth2Adapter)
```

<br>

그리고 소셜 로그인 페이지를 반환하는 뷰는 하단에 'oauth2_login' 객체이다.

<br>

### 2. url 설정

<br>

```python
from allauth.socialaccount.providers.google.views import oauth2_login
from django.urls import path, include


app_name = 'accounts'

urlpatterns = [
    path('login/', oauth2_login, name='login'),
    path('logout/', views.logout, name='logout')

]
```

<br>



찾는 것이 어렵지 view를 찾기만 하면 아주 쉽게 사용할 수 있다.