---
title:  "django Lazy Loading"
excerpt: "게으른 것인가 효율적인 것인가"
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2022-03-24
toc: true
toc_sticky: true
published: true
---

# django Lazy Loading

<br>

장고 ORM의 핵심 특성 중 하나인 `Lazy Loading`에 대해서 알아보자.

<br>

## Lazy Loading 이란

<br>

Lazy Loading 이란 간단하게 말해서 django ORM이 맵핑된 데이터에 접근 할 때에 쿼리를 정말 필요한 때에 필요한 만큼만 호출하는 특징을 의미한다.

<br>

간단한 코드로 살펴보자

<br>

```python
def exam_view(request):
    users = User.objects.all() # 1
    
    first_user = users[0] # 2
    
    user_list = list(users) # 3
    
    
```

<br>

위와 같은 View가 있다고 가정해보자.

<br>

- 1번에서는 모든 유저 정보를 가져 오기 위한 준비만 할 뿐 어떤 쿼리도 실행되지 않는다.

<br>

- 2번에서는 `LIMIT 1` 쿼리를 통해 맵핑된 데이터에서 하나의 row만을 가져온다,

<br>

- 3번에서는 list 객체를 만들기 위해서 맵핑된 모든 데이터의 row를 가져온다.

<br>

1번에서 Lazy Loading의 첫 번째 특성인 필요한 순간에 쿼리가 호출되는 특징을 알 수 있으며,

<br>

2번에서 Lazy Loading의 두 번째 특성인 필요한 만큼만 쿼리가 호출되는 특징을 알 수 있다.

<br>

불필요한 쿼리 비용이 낭비되는 것을 방지하기 위해 만든 특성이지만 이 때문에 일반적인 SQL과 다르게 오히려 쿼리가 재사용되지 않을 수도 있다.

<br>

이런 단점을 QuerySet  캐싱을 통해 해결 할 수 있다.

<br>

이번 글에선 간단하게 Lazy Loading에 대한 부분만 다뤄보고 다음 글에서 캐싱을 통해 쿼리를 어떻게 효율적으로 사용하며, 관리할 수 있는지 작성해보겠다.