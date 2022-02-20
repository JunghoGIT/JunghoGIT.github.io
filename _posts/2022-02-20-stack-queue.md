---
title:  "스택과 큐"
excerpt: "자료구조 학습"
categories:
 - DataStructure
tags:
 - [DataStructure,python,TIL]
last_modified_at: 2022-02-20
toc: true
toc_sticky: true
published: true
---

# 스택과 큐

<br>

자료구조 중 가장 기본적인 자료구조인 스택과 큐를 알아보자.

<br>

## 스택

<br>

스택이란 Last In First Out(LIFO) 즉, 먼저 넣은 데이터가 나중에 반환되도록 설계한 메모리 구조이다.

<br>

간단한 비유로는 탑을 쌓아올리는 것이라고 생각하면 된다.

<br>

스택에서 데이터 입력은 'Push', 출력은 'Pop' 이라고 부른다.

<br>

![stack](\assets\images\자료구조\stack.png)

<br>

### 스택의 활용


<br>


- 브라우저 방문기록 
- 실행 취소 : ctrl + z 로 실행 취소 하는 것처럼 가장 최근의 이벤트부터 취소되어야 할 때
- 재귀함수 처리 프로세스


<br>


### python에서의 스택


<br>


python에서 스택은 리스트를 사용함으로서 별도의 구현 없이 동일한 기능을 사용할 수 있다.

<br>

- Push : append()
- Pop : pop()

<br>



## 큐

<br>

큐란 First In First Out(FIFO) 즉, 먼저 넣은 데이터가 먼저 반환되도록 설계한 메모리 구조이다.

<br>

간단한 비유로는 줄을 서는 것과 비슷하다고 생각하면 된다.

<br>

큐에서 데이터 입력은 'Push', 출력은 'Pop' 이라고 부른다.

<br>

![queue-data-structure-queue-picture-2-mROyS1mul](\assets\images\자료구조\queue-data-structure-queue-picture-2-mROyS1mul.jpg)

### 큐의 활용

<br>

- 우선순위가 같은 작업의 스케줄링
- 캐시 구현

<br>

### python 에서의 큐


<br>


python에서 큐는 리스트를 사용함으로서 별도의 구현 없이 동일한 기능을 사용할 수 있다.

<br>

- Push : append()
- Pop : pop(0)



