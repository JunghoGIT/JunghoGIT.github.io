---
title:  "[Error] serializers 'objects is not iterable'"
excerpt: "직렬화 실패 에러"
categories:
 - Django
tags:
 - [Django,python,study,TIL,Error]
last_modified_at: 2021-02-05
toc: true
toc_sticky: true
---

# [Error]  serializers 'objects is not iterable' 

<br>

## 에러 발생

<br>

DRF 를 사용하지 않고 스크립트에서 장고 서버 api를 get으로 호출하면 모델 객체를 응답하도록 api를 만들었다.

<br>

이전에도 사용했었던 로직에서 모델 객체만 바뀌었기 때문에 당연히 될 줄 알았으나 요청을 보내면 500 상태 코드가 나오며 아무런 값도 반환하지 않았다.

<br>

## 에러 원인

<br>

장고 serializers 는 반복 가능한 객체 즉 `iterable objects` 를 default로 동작하기 때문이었다.

<br>

```python
object_test = serializers.serialize('json',Test.objects.get(pk=1))
```

<br>

장고 ORM에서 get을 사용했을 땐 단 하나의 객체만 반환하기 때문에 'not iterable' 하다.

<br>

## 에러 해결


<br>


1. filter 사용 

```python
object_test = serializers.serialize('json',Test.objects.filter(pk=1))
```

<br>

2. 리스트로 전달

<br>

```python
object_test = serializers.serialize('json',[Test.objects.get(pk=1),])
```

<br>

ORM에서 get 과 filter의 차이를 이해하고, python 에서 itreable 객체에 대한 이해가 있으면 어렵지 않게 해결 가능한 에러다.