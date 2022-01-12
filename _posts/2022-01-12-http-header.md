---
title:  "HTTP 헤더"
excerpt: "header"
categories:
 - Web
tags:
 - [web,Network,study,TIL]
last_modified_at: 2022-01-12
toc: true
toc_sticky: true
---

# HTTP 헤더

<br>


HTTP 메세지에서 다양한 정보를 담고 있는 헤더 부분에 대해서 알아보자.

<br>

## 표현 헤더(Representation Header)

<br>

HTTP 메시지의 헤더 부분에는 표현헤더가 존재하며, 바디에 있는 메시지는 표현 메시지라고도 표현이 가능하다.

<br>

- Content Type : 표현 데이터의 형식
  - 미디어 타입, 문자 인코딩 등을 포함
- Content-Encoding : 표현 데이터의 압축 방식
  - 표현 데이터를 압축하기 위해 사용 ex.gzip
- Content -Language : 표현 데이터의 자연 언어
  - ko, en, en-US 등의 자연어를 명시한다.
- Content-Length : 표현 데이터의 길이
  - 표현데이터의 바이트 단위로 길이를 표현한다.
  - 전송 코딩을 사용할 때는 사용 금지


<br>


## 협상 헤더 (콘텐츠 네고시에이션)

<br>

클라이언트가 선호하는 표현을 요청한다.

클라이언트 기준이기 때문에 요청시에만 사용 가능하다.

<br>

- Accept : 클라이언트가 선호하는 미디어 타입 전달
- Accept-Charset : 클라이언트가 선호하는 문자 인코딩
- Accept-Encoding : 클라이언트가 선호하는 압축 인코딩
- Accept-Language : 클라이언트가 선호하는 자연 언어

<br>

q=0~1 의 값을 부여함으로서 우선 순위를 설정한다.


<br>


## 일반 정보 헤더

<br>

- From
  - 유저 에이전트의 이메일 정보
  - 검색 엔진 같은 곳에서 주로 사용한다.
  - 요청에서 사용 됨
  - 일반적으론 잘 사용하지 않음
- Referer
  - 현재 요청된 페이지 이전의 페이지 주소
  - 요청에서 사용됨
  - 유입 경로 분석에 잘 쓰임
- User_Agent
  - 클라이언트의 애플리케이션 정보
  - 통계 정보에 자주 쓰임
- Server
  - 요청을 처리하는 Origin 서버의 소프트웨어 정보
  - 응답에서 사용
- Date
  - 날짜
  - 응답에서 사용

<br>

## 특별 정보 헤더

<br>

- Host (\* **필수**)
  - 요청한 호스트 정보
  - 요청에서 사용
  - 하나의 서버가 여러 도메인을 처리해야 할 때
- Location 
  - 3xx 응답의 경우 페이지 리다이렉션 할 때 사용할 주소
  - 201 응답의 경우 생성된 리소스 URI
- Allow
  - 허용 가능한 HTTP 메소드 명시
  - 자주 사용 안 함
- Retry-After
  - 유저가 다음 요청까지 기다려야 하는 시간
  - 자주 사용 안 함



<br>

## 인증 헤더

<br>

- Authorization 
  - 클라이언트 인증 정보를 서버에 전달
- WWW-Authenticate
  - 리소스 접근시 필요한 인증방법 정의
  - 401 응답과 함께 사용함

<br>

## 쿠키

<br>

무상태 특성 때문에 모든 요청에 정보를 넘기는 문제를 해결하기 위해 생겨난 개념

<br>

쿠키에 대한 부분은 현재 글에서 정리하기 보단 다른 글에서 자세히 다뤄볼 예정이다. 



<br>

- Cookie

- Set-Cookie

  - 쿠키를 설정하는 헤더

  - 생명주기 설정 가능

    

    



