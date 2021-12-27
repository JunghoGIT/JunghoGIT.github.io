---
title:  "Template 상속"
excerpt: "template 상속을 통해 base.html을 만들어보자."
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2021-12-20
toc: true
toc_sticky: true
---

# Template 상속



웹페이지를 만들다보면 페이지 별로 중복되는 부분이 존재할 수 있다.

그럴 때 모든 템플릿 코드를 수정하는 번거로움이 없이 중복되는 템플릿 하나를 만들어 상속시켜 줌으로서 효율적인 템플릿 구조를 만들 수 있다.





## 부모 템플릿



부모 템플릿이 될 base.html 을 만들어보자.

{% raw %}``{% block content %}`` 와 ``{% endlock %}`` {% endraw %}탬플릿 태그를 이용하게 간단하게 만들 수 있다.



```html
{% raw %}
{% load static %}
<!doctype html>
<html lang="ko">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" type="text/css" href="{% static 'bootstrap.min.css' %}">
    <!-- pybo CSS -->
    <link rel="stylesheet" type="text/css" href="{% static 'style.css' %}">
    <title>Hello, Jungho!</title>
</head>
<body>
<!-- 기본 템플릿 안에 삽입될 내용 Start -->
{% block content %}
{% endblock %}
<!-- 기본 템플릿 안에 삽입될 내용 End -->
</body>
</html>
{% endraw %}
```



자식 탬플릿이 작성되고 적용 시킬 부분을 {% raw %}``{% block content %}`` 와 ``{% endlock %}`` {% endraw %} 탬플릿 태그로 구분한다.





## 자식 템플릿



부모 템플릿인 'base.html'을 상속받는 자식 템플릿을 작성해보자.



```html

{% raw %}
{% extends 'base.html' %} <!-- base.html 템플릿 상속-->

{% block content %}

<!-- 코드 작성 -->

{% endblock %}
{% endraw %}

```



아주 간단하다.

요약하자면



1. 부모 템플릿에서 상속받은 자식만의 코드가 구현 될 부분을 {% raw %}`{% block content %}` 와 `{% endlock %}`{% endraw %} 코드로 만들어준다.
2. 자식 템플릿에서 `{% extends '부모템플릿' %}` 을 통해 부모 템플릿을 지정해주고  {% raw %}`{% block content %}` 와 `{% endlock %}`{% endraw %} 안에 코드를 작성한다.



very easy !