---
title:  "DRF FBV 방식으로 API View 만들기"
excerpt: "함수 기반 뷰를 사용해보자"
categories:
 - DRF
tags:
 - [DRF,Django,python,study,TIL]
last_modified_at: 2022-02-19
toc: true
toc_sticky: true
published: true
---

# DRF  함수 기반 뷰 방식으로 API View 만들기 


<br>


## DRF에서 API view 를 만드는 방법

<br>

DRF를 이용하여 API 를 설계하는 방법에는 django와 마찬가지로 FBV, CBV 두 가지로 나뉜다.

<br>

- FBV - 함수 기반 뷰
  - @api_vew  : 자유도가 가장 높다
- CBV - 클래스 기반 뷰
  - APIView : @api_view 와 거의 동일하다고 보면 된다.
  - generics View : 다양한 CRUD 조합 별로 클래스가 구성되어 있다.
  - ViewSet : 자유도는 비교적 낮은 편이지만 개발에 필요한 코드는 가장 적다. 
    - router를 이용하여 URI 설계가 가능하다.

<br>

## @api_view 데코레이터를 이용한 FBV 방식 API 설계

<br>

이번 글에서는 가장 자유도가 높은 api_view 데코레이터를 이용한 방식을 사용해보겠다.

<br>

### 기본적인 코드 작성법

<br>

아무런 퍼포먼스 없이 하나의 리소스 만을 CRUD 하는 로직을 기준으로 코드를 작성해봤다.

<br>

```python
@api_view(['GET', 'POST'])
def memo(request):

    if request.method == 'GET':
        memo = Memo.objects.all()
        serializer = MemoSerializer(memo, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    elif request.method == 'POST':
        memo = MemoSerializer(data=request.data)
        if memo.is_valid():
            memo.save()
            return Response(status=status.HTTP_201_CREATED)
        else: 
    	return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def memo_detail(request,pk):
    memo = Memo.objects.get(id=pk)
    if request.method == 'GET':
        serializer = MemoSerializer(memo)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = MemoSerializer(memo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        memo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

```

<br>

코드를 대충 보면 알겠지만 django에서 form으로 데이터를 처리하는 것과 거의 동일하다.

<br>

### 특징 

<br>

- @api_view() 데코레이터
  - api view 데코레이터를 사용함으로서 request method에 대한 제약을 둘 수 있다.
  - 그 외에도 DRF의 여러 API view와 관계된 기능들을 사용할 수 있도록 한다.
- Serializer
  - Form 과 매우 유사한 기능을 하는 Serializer를 사용한다.
  - 일반적으로 Form은 HTML 상에서 form 태그에서 받은 data를 사용하지만 Serializer는 request에 전달 된 json 데이터를 사용한다.
- Response
  - DRF의 Response를 사용함으로서 HTTP 상태 코드와 data를 전달할 수 있다.
  - 데이터는 직렬화되어 있는 형태여야 한다.

<br>

### 함께 사용 가능한 데코레이터

<br>

- @renderer_classes(...)

  - 렌더러 설정

- @parser_classes(...)

  - 파서 설정

- @authentication_classes(...)

  - 인증 방식 설정

- @throttle_classes(...)

  - 호출 횟수 설정

- @permission_classes(...)

  - 권한 설정

  