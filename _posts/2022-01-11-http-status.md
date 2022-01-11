---
title:  "HTTP 상태코드"
excerpt: "상태코드를 통한 http 통신 상태 확인"
categories:
 - Web
tags:
 - [web,Network,study,TIL]
last_modified_at: 2022-01-11
toc: true
toc_sticky: true
---

# HTTP 상태코드

<br>

클라이언트가 보낸 요청의 처리 상태를 응답에서 알려주는 기능을 의미한다.

<br>

가장 쉬운 예로 404 error가 상태코드 중 하나이다.

<br>

상태코드의 백의 자리 만으로 대략적인 상태를 유추할 수 있다.


<br>


## 1xx (infomational) 

<br>

요청이 수신되어 처리 중을 의미함

거의 볼 수 없다.

<br>

## 2xx(Successful) 

<br>

요청 정상 처리를 의미함

<br>

- 200 OK
- 201 Created
  - 리소스 생성시 주로 사용
- 202 Accepted
  - 배치 처리 같은 곳에서 사용
  - 요청이 접수되었으나 완료되지 않았음을 의미
- 204 No Content
  - 본문에 보낼 데이터가 없음을 의미함


<br>


## 3xx(Redirection)

<br>

요청을 완료하려면 추가 행동이 필요

<br>

- 300 Multiple Choices
- 301 Moved Permanently
  - 영구 리다이렉션(기존 URL 사용 불가능을 의미)
  - 리다이렉트시 요청 메소드가 GET으로 변함
  - 본문이 제거 될 수 있음
- 302 Found
  - 일시적인 리다이렉션
  - 리다이렉트시 요청 메소드가 GET으로 변함
  - 본문이 제거 될 수 있음
- 303 See Other
  - 일시적인 리다이렉션
  - 리다이렉트시 요청 메소드가 GET으로 변함
- 304 Not Modified
  - 캐시를 목적으로 사용
  - 캐시를 재사용하라는 응답을 준다
- 307 Temporary Redirect
  - 일시적인 리다이렉션
  - 요청 메소드와 본문이 유지됨
- 308 Permanent Redirect
  - 영구 리다이렉션(기존 URL 사용 불가능을 의미)
  - 요청 메소드와 본문이 유지됨


<br>


## 4xx(Client Error)

<br>

클라이언트 오류, 잘못된 문법 등으로 서버가 요청을 수행 할 수 없음을 의미함

<br>

- 400 Bad Reqeust

  - 요청 구문, 메세지 오류등
  - 클라이언트가 요청을 수정해서 보내줘야함

- 401 Unauthorized

  - 인증 되지 않음

- 403 Forbidden

  - 접근 권한 없음

- 404 Not Found

  - 리소스가 없음
  - 권한에 따라 리소스를 숨기고 싶을 때도 사용

  
<br>


## 5xx(Server Error)

<br>

서버 오류, 서버가 정상 요청을 처리하지 못함

<br>

- 500 Internal Sever Error
  - 서버 에러
- 503 Service Unavaliable
  - 일시적인 서버 사용 불가 

<br>

