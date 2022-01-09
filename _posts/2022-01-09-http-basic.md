---
title:  "HTTP 개요"
excerpt: "HTTP란?"
categories:
 - Web
tags:
 - [web,Network,study,TIL]
last_modified_at: 2022-01-09
toc: true
toc_sticky: true
---

# HTTP 

<br>


HTTP란 Hyper Text Transfer Protocol 의 약자로서 클라이언트와 서버 사이에 이루어지는 요청/응답 프로토콜이다.

<br>

지금의 web 서비스라고 하면 거의 전부라 할 정도로 HTTP로 모든 것을 처리할 수 있다.

<br>

웹페이지를 구성하는 HTML 부터 각종 파일들, API를 통한 json, xml 형식까지 거의 모든 형태의 데이터를 전송 가능하다.


<br>


## 기반 프로토콜

<br>

HTTP는 버전 별로 다른 프로토콜이 사용된다.

<br>

- TCP : HTTP/1.1 , HTTP/2
  - 현재 1.1을 가장 주로 사용하고 있다.
- UDP : HTTP/3
  - 최근 급 부상하여 사용도가 올라가고 있다.


<br>


## Stateful, Stateless

<br>

- Stateful 은 상태유지, Stateless 는 무상태를 의미한다.

<br>

### stateful 

<br>

- 상태유지란 한 클라이언트에 대해서 특정 서버가 해당 클라이언트의 상태를 유지함을 의미한다.
  - 데이터 A의 1번글을 원한다 쳤을 때, 데이터 A를 달라는 요청 이후엔 1번글만 요청해도 서버는 클라이언트가 A 데이터를 원한다는 상태를 유지하고 있기 때문에 A의 1번글을 전달한다.
- 항상 같은 서버가 유지되어야 하는 불편함이 있다.
- 중간에 서버가 장애가 났을 때 새로운 서버를 사용함에 따라 기존의 상태는 무용지물이 된다.


<br>


### stateless

<br>

- 무상태란 서버가 클라이언트에 대한 상태를 보관하지 않고 각각의 요청에 맞는 응답만 해주는 것을 의미한다.
- 스케일 아웃(수평확장) 에 매우 유리하다.
  - 서비스의 트래픽이 몰렸을 때 복잡한 로직 없이 단순히 서버를 늘리는 것만으로 해결이 가능하다.
- 비용적으로나 유지보수 측면에서 stateful 보다 우수하다고 할 수 있다.
- 하지만 모든 것을 stateless로 설계 할 순 없다.
- 최소한의 stateful 안에서 최대한 stateless로 설계한다.
  - 로그인등은 쿠키와 세션등을 사용하여 처리


<br>


## 비연결성

<br>

- 만약 모든 클라이언트와 서버의 연결이 계속 유지된다면 서버의 자원이 낭비되게 된다. 그렇기에 HTTP는 기본적으로 연결을 유지하지 않는 비연결성을 갖는다.


<br>


### 특징과 장점 

<br>

- 일반적으로 초 단위 이하의 빠른 속도로 응답한다.
- 수천명이 서비스를 사용해도 동시에 처리하는 요청은 수십개 이하이다.
- 서버 자원을 효율적으로 사용 가능하다.

<br>

### 한계점

<br>

- 연결이 유지되지 않는 만큼 클라이언트의 요청에 따라 TCP/IP 매번 새로 해야한다.
  - 3 way handshake 시간 소모
- 연결 할 때마다 페이지의 수 많은 리소스들이 함께 다운로드 됨
  - HTTP 지속연결 (Persistent Connections)로 문제 해결
  - HTTP/2 , HTTP/3 에서 더욱 최적화됨
  - 

<br>

## HTTP 메시지

<br>

기본 구조는 다음과 같다.


<br>


![html구조](\assets\images\html\html구조.png)



출처:[https://deepwelloper.tistory.com/98](https://deepwelloper.tistory.com/98)


<br>


### 요청메시지

<br>

HTTP 요청 메시지의 구조는 다음 예시를 통해 살펴보자.


<br>


| HTTP 요청메시지                                  | HTTP 메시지 구조 |
| ------------------------------------------------ | ---------------- |
| GET/search?q=jungho&amp;hl=ko HTTP/1.1           | start-line       |
| Host:www.google.com                              | header           |
| 공백                                             | empty-line       |
| <요청메시지에선 body가 있을 수도 없을 수도 있음> | message body     |


<br>


- start-line
  - HTTP 메소드 (GET,POST...)
  - 요청대상 
    - ('/') 로 시작하는 절대경로
    - 쿼리
  - HTTP 버전
- Header
  - 전송에 필요한 모든 부가정보 포함


<br>


### 응답 메시지

<br>

타입에 따라 내용은 달라 질 수 있지만 대략적인 구조는 다음의 예와 같다.

<br>

| HTTP 응답메시지                                              | HTTP 메시지 구조 |
| ------------------------------------------------------------ | ---------------- |
| HTTP/1.1 200 OK                                              | start-line       |
| Content-Type:text/html;charset=UTF-8<br />Content-Length:3423 | header           |
| 공백                                                         | empty-line       |
| html 태그~(Content-Type:text/html 이기 때문에)               | message body     |


<br>


- start-line
  - HTTP 버전
  - HTTP 상태코드 (성공 실패 여부 등)
  - 이유 문구 : 사람이 이해할 수 있는 짧은 코드 설명
- Header
  - 전송에 필요한 모든 부가정보 포함
  - 많은 표준 헤더 존재
- Body
  - 실제 전송할 데이터가 저장됨
  - HTML, 문서, 이미지, json 등 byte로 표현할 수 있는 모든 데이터 전송 가능

<br>