---
title:  "연결리스트"
excerpt: "자료구조 학습"
categories:
 - DataStructure
tags:
 - [DataStructure,python,TIL]
last_modified_at: 2022-02-22
toc: true
toc_sticky: true
published: true
---


# 연결 리스트

<br>

연결 리스트 (Linked List) 자료 구조를 알아보자 !

<br>

## 구조

<br>

![What-are-linked-lists-in-python](\assets\images\자료구조\What-are-linked-lists-in-python.png)

<br>

- 노드 
  - 각 노드는 하나의 object
  - data, pointer 등의 데이터 저장 단위로 구성
- data
  - 노드에 저장되어 있는 값
- pointer
  - 다음 노드의 메모리 주소 
- head
  - 연결리스트의 시작점
- tail
  - 연결리스트의 끝
  - Pointer에 메모리 주소 값이 없음 (None)

<br>

## 장단점

<br>

- 장점
  - 메모리 공간을 미리 할당하지 않아도 됨
  - 삽입,삭제에 매우 유리
    - O(1) 의 시간 복잡도를 가진다.
- 단점
  - 조회에 불리
    - O(N)의 시간 복잡도를 가진다.
  - 중간 데이터 삭제시 앞 뒤 데이터를 재구성해줘야 함


<br>


## Python에서의 연결 리스트 

<br>

Python에서는 객체지향적으로 클래스를 이용하여 연결리스트 자료구조를 구현할 수 있다.

<br>

```python
class SLinkedList:

    class Node:
        def __init__(self, v, n = None):
            self.value = v
            self.next = n

    def __init__(self):
        self.head = None

    def printNode(self):
        if self.head is None:
            print("저장된 데이터가 없음")
            return
        else:
            print("<현재 리스트 구조>", end='\t')
            link = self.head

            while link :
                print(link.value, '->' , end = ' ')
                link = link.next
            print()

    def insertNode(self, v):
        if self.head is None:
            self.head = self.Node(v)
        else:

            self.head = self.Node(v, self.head)

    def deleteNode(self):
        if self.head is None:
            print("삭제할 노드가 없습니다.")
            return
        else:
            self.head = self.head.next

    def searchNode(self,v):
        if self.head is None:
            print("저장된 데이터가 없음")
            return
        else:
            link = self.head
            index  = 0
            while link:
                if v == link.value:
                    return index
                else:
                    link = link.next
                    index += 1

if __name__=="__main__":
    sl = SLinkedList()
    sl.insertNode('1st')
    sl.insertNode('2nd')
    sl.insertNode('3rd')

    print("<위치 탐색>")
    result = sl.searchNode('1st')
    print("1st의 위치 : {}".format(result))

    result = sl.searchNode('555')
    print("555의 위치 : {}".format(result))

```

<br>

코드 출처 : [wikidocs](https://wikidocs.net/34534)

<br>

## Python에서 리스트와 연결 리스트의 차이

<br>

사실상 python에서는 굳이 연결리스트를 구현할 필요는 없다.

<br>

python 리스트 object 자체가 동적 배열이며, 연결 리스트의 주요 기능들을 제공하기 때문이다.

<br>

기능적으로 부족함이 없기에 굳이 쓸 필요가 없다는 뜻이지 차이점이 없다는 뜻은 아니다.

<br>

차이점을 알아보자.

<br>

- Index

  - 연결리스트는 각 노드별로 메모리 주소가 연결되어 저장되지 않기 때문에 인덱싱이 불가능
  - 리스트의 경우 동적 배열의 형태가 기본이기 때문에 각 데이터는 연결된 메모리 주소에 저장됨에 따라 인덱싱이 가능하다.

- 시간 복잡도

  - 조회
    - 인덱스를 사용하는 리스트 조회의 경우 시간복잡도는 O(1)
    - 연결리스트의 경우 시간복잡도는 O(n)
  - 삽입, 삭제
    - 리스트의 경우 O(n)
    - 연결리스트의 경우 O(1)

  
<br>


