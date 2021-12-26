---
title:  "MTV 디자인패턴"
excerpt: "장고의 디자인패턴"
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2021-12-26
toc: true
toc_sticky: true
---

# 디자인 패턴



디자인패턴이란 객체지향 프로그래밍을 설계할 때 자주 사용하는 설계 형태를 정형화하고 설계 지식을 검증화, 추상화하여 일반화한 패턴이다.



구조적인 문제를 해결할 수 있는 방안을 제시해준다.



## MVC 패턴



웹을 설계할 때 가장 흔하게 쓰이는 패턴 중 하나이다.



### 장점 

- 유연성이 높다.
- 유지보수가 쉽다.
- 업무 분담이 수월하다.

### 단점

- 모델과 뷰의 의존성을 완벽히 분리 할 수 없다.



### 구성 요소



- **Model** 
  - 로직을 통해 사용자의 요청에 따라 정보(데이터)를 처리하는 부분이다.
  - DB에 직접적으로 접근하고 데이터를 CRUD 한다.
- **View**
  - 사용자들이 실제로 볼 수 있는 화면
  - Controller 에서 받은 데이터를 웹 브라우져에 렌더링 되도록 변환한다.
  - 시각적인 HTML 페이지 그 자체를 의미하기도 한다.
- **Controller** 
  - Model 과 View 의 징검다리 역할을 한다.
  - 적절한 로직으로 Model에 원하는 데이터를 요청하고, Model 의 응답을 로직에 맞춰 view에 전달해준다.



## 과정



1. 유저가 브라우저를 통해 요청을 보낸다.
2. View에서 해당 요청을 Controller 에게 전달한다.
3. Controller는 해당 요청을 로직에 따라 Model 데이터 처리 요청을 한다.
4. Model 은 데이터 처리 결과를 반납한다.
5. Controller는 응답 데이터를 View에게 전달한다.
6. View는 전달 받은 데이터로 HTML 을 구성하여 사용자에게 응답한다.





## MTV 패턴



장고는 기존 MVC 패턴과 비슷하지만 장고만의 특징을 가진 MTV 패턴을 가진다.

MTV 패턴의 각 요소별 명칭은 MVC 패턴에 대응되지만 내부동작 원리에는 차이가 있다.



### 구성 요소



- **Model**
  - DB에 저장되는 데이터를 의미한다.
  - 장고는 Model을 통해 객체로서 데이터를 관리하며 하나의 클래스가 하나의 테이블이다.
  - 객체로서 데이터를 관리하기 때문에 SQL을 필요로 하지 않는다.
  - SQL은 ORM 기능을 통해 query set 이라는 python code로 대신한다.
- **Template**
  - MVC 패턴의 View에 대응한다.
  - 사용자들에게 보여지는 화면을 의미한다.
  - view에서 context와 함께 렌더링한 html 파일이 template이다.
  - 장고만의 탬플릿 태그를 통해 html 파일에서 데이터를 활용할 수 있다.
- **View**
  - MVC 패턴의 Controller에 대응한다.
  - 요청에 따라 결과를 템플릿으로 렌더링해준다.
  - 로직을 구성하는 부분이다
- URL 설계
  - 장고에서는 urls.py 에서 url과 view를 맵핑해준다.





### 과정





![MTV_1](\assets\images\django\MTV_1.jpg)



1. 클라이언트가 요청을 보낸다.
2. urls.py 에서 URL을 분석하여 맵핑을 통해 처리할 view에 요청을 보낸다.
3. View는 받은 요청에서 Data가 필요하다면 Model에 요청을 보낸다.
4. Model은 해당 요청을 처리하기 위해 DB와 ORM 방식으로 질의하여 데이터를 받아온다.
   - 이후 데이터 요청 처리 결과를 view에게 반환한다.
5. View 는 자신의 로직을 처리하고 Template에 context로 데이터를 전달
   - Template 은 받은 데이터로 HTML 파일을 생성
6. 렌더링이 완료된 template을 사용자에게 응답