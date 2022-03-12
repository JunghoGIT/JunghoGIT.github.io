---
title:  "django 정참조와 역참조"
excerpt: "관계된 데이터에 접근하는 법"
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2022-03-13
toc: true
toc_sticky: true
published: true
---

# django 정참조와 역참조

<br>

django ORM 을 사용하다 보면 관계되어 있는 객체에 접근해야 될 때가 있다.

<br>

이럴 때 정참조이냐 역참조이냐에 따라 데이터에 접근하는 방식이 다르다.

<br>

단순히 접근법에 대한 차이가 아니라 쿼리 비용에 대한 문제로까지 확장되는 개념이다.

<br>

이번 글에선 단순히 개념적인 부분만 정리해보자.

<br>

## 개념

<br>

아래와 같은 모델이 존재한다고 가정해보자.

<br>

```python
class Person(models.Model)
	name = models.CharField(max_length=10)
    
class Dog(models.Model)
	owner = models.ForeignKey(Person)
    name = models.CharField(max_length=20)
    
```

<br>

사람과 개는 1:N 관계이다.

<br>

그리고 개 모델은 주인에 대한 속성을 포함하고 있다.

<br>

이때 개 -> 사람으로 참조하는 것을 `정참조` 반대의 경우를 `역참조` 라고한다.

<br>

## 코드

<br>

### 정참조

<br>

정참조를 쉽게 설명하자면 Foreign Key 속성이 있는 객체에서 없는 개체를 참조하거나 One to One 관계에서 참조할 때를 정참조라고 한다.

<br>

```python
dog = Dog.objects.get(pk=1)

dog.owner.name
```

<br>

정참조의 경우는 위의 코드처럼 아주 간단하게 참조 할 수 있다.

<br>

### 역참조

<br>

역참조는 Foreign Key 속성이 없는 객체에서 관계된 모델을 참조하는 경우이다.

<br>

```python
person = Person.objects.get(name='윤정호')

person.dog.name # X
person_dogs = person.dog_set.all()

```
<br>

위의 코드처럼 set manager를 사용하여 참조하는 방법이 있다.

<br>

다른 방법으론 related_name 을 사용하는 방법이 있다.

<br>

```python
class Person(models.Model)
	name = models.CharField(max_length=10)
    
class Dog(models.Model)
	owner = models.ForeignKey(Person, related_name='dogs')
    name = models.CharField(max_length=20)
```

<br>

Foreign Key 속성에 해당 related_name 설정을 추가해주자.

<br>

```python
person = Person.objects.get(name='윤정호')

person_dogs = person.dogs.all()
```

<br>

위 코드처럼 사용 가능하다.

<br>

사실 related_name을 사용하는 이유는 set manager를 대신하기 위함은 아니다.

<br>

여러 속성에서 같은 모델을 Foriegn Key로 가지고 있을 경우 역참조할 때에 django는 어떤 속성에 대한 참조인지 찾을 수 없는 에러가 발생한다.

<br>

이때 related_name 설정을 통해 각 필드의 이름을 구분하여 참조할 수 있도록 도와주는 기능을 하는 것이다.