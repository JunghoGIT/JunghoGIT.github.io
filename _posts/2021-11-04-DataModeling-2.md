---
title:  "데이터 모델링 2"
excerpt: "Entity와 스키마"
categories:
 - SQL
tags:
 - [data,SQL,study,TIL]
last_modified_at: 2021-11-04
toc: true
toc_sticky: true
---

# 데이터 모델링 2

<br>
<br>

## 3층 스키마


<br>


### 3층 스키마란

<br>

- 사용자, 설계자, 개발자가 데이터베이스를 보는 관점에 따라 데이터베이스를 기술하고 이들간의 관계를 정의한 ANSI표준이다.

- 3층 스키마는 데이터의 `독립성`을 확보하기 위한 방법이다.
- 데이터 베이스의 독립성을 확보함으로써 데이터 복잡도 감소, 데이터 중복 제거, 사용자 요구사항 변경에 따른 대응력 향상, 관리 및 유지보수 비용 절감등의 장점을 챙길 수 있다.
- 각 계층은 view라고도 한다.



### 3층 스키마의 구조
<br>




- **외부 스키마**
  - 응용 프로그램이 접근하는 데이터베이스를 정의한다.
  - 사용자 관점, 뷰를 표현한다.
  - 업무상 관련 있는 데이터만 접근한다.
  - 관련된 데이터베이스의 일부만 표시한다.
  - 하나의 데이터베이스에 대해 서로 다른 관점을 허용한다.
- **개념 스키마**
  - 설계자 관점, 사용자 전체 집단의 데이터베이스 구조이다.
  - 기관이나 조직체의 관점에서 데이터베이스 구조를 정의한다.
  - 통합 데이터베이스 구조이다.
  - 전체 데이터베이스 내의 모든 데이터에 관한 규칙과 의미를 묘사한다.
- **내부 스키마**
  - 데이터 베이스의 물리적 저장구조이다.
  - 데이터의 저장 구조, 레코드의 구조, 필드의 정의, 인덱스와 해시를 생성한다.
  - 운영체제와 하드웨어에 종속적이다.
  - 개발자 관점의 스키마이다.



**3층 스키마의 독립성**

- 논리적 독립성
  - 개념 스키마가 변경되더라도 외부 스키마가 영향을 받지 않는 것
- 물리적 독립성
  - 내부 스키마가 변경되더라도 개념 스키마가 영향을 받지 않는 것



## Entity

<br>

엔티티는 업무에서 관리해야 하는 데이터 집합을 의미하며, 저장되고 관리되어야 하는 데이터이다.

실제 데이터베이스에서 테이블로 표현된다.

고객의 비즈니스 프로세스에서 관리되어야 하는 정보를 추출한다.



### Entity의 특징
<br>


- **식별자**
  - 엔티티는 유일한 식별자가 있어야한다. (primary key)
- **인스턴스 집합**
  - 2개 이상의 인스턴스가 있어야한다.
- **속성**
  - 엔티티는 반드시 속성을 가지고 있다.
- **관계**
  - 엔티티는 다른 엔티티와 최소한 한 개 이상 관계가 있어야한다.
- **업무**
  - 엔티티는 업무에서 관리 되어야 하는 집합이다.



### Entity의 종류
<br>


엔티티의 종류는 유형과 무형에 따른 종류, 발생하는 시점에 따른 종류 두가지 방식으로 분류 할 수 있다.

엔티티를 유형과 무형으로 분류하는 기준은 물리적 형태의 존재여부이다.



**유형과 무형에 따른 엔터티 종류**

| 종류        | 설명                                                         |
| ----------- | ------------------------------------------------------------ |
| 유형 엔티티 | -업무에서 도출되며 지속적으로 사용되는 엔티티이다.<br />-ex)고객명단,사원명단 |
| 개념 엔티티 | -물리적 형태가 없으며 개념적으로 사용된다.<br />-ex)금융 상품,거래소 종목 |
| 사건 엔티티 | -비즈니스 프로세스를 실행하면서 생성되는 엔티티이다.<br />-ex)주문,체결 |

**발생 시점에 따른 엔티티 종류**

| 종류        | 설명                                                         |
| ----------- | ------------------------------------------------------------ |
| 기본 엔티티 | -키엔티티라고 불리며 독립적으로 생성되는 엔티티이다.         |
| 중심 엔티티 | -기본 엔티티와 행위 엔티티 간의 중간에 있다.<br />- 기본 엔티티로 인해 발생되고 행위 엔티티를 생성하는 엔티티이다. |
| 행위 엔티티 | - 2개 이상의 엔티티로부터 발생된다.                          |





## 속성

<br>



- 속성은 업무에서 필요한 정보인 엔티티가 가지는 항목이다.

- 이는 데이터베이스에서 칼럼을 의미한다.

- 속성은 더 이상 분리되지 않는 단위로 업무에 필요한 데이터를 저장할 수 있다.

- 하나의 값만 가진다.

- 주식별자에게 함수적으로 종속된다. 기본키가 변경되면 속성의 값도 변경된다는 의미이다.

  



### 속성의 종류

<br>

**분해 여부에 따른 속성의 종류**



| 종류        | 설명                                                         |
| ----------- | ------------------------------------------------------------ |
| 단일 속성   | 하나의 의미로 구성된 것으로 이름,id같은 것을 의미한다.       |
| 복합 속성   | 여러 개의 의미가 있는 것으로 주소 같은 것을 의미한다.        |
| 다중값 속성 | 속성에 여러개의 값을 가질 수 있는 것으로 예를 들어 상품 리스트가 있다. |



**특성에 따른 속성의 종류**

<br>

| 종류      | 설명                                                         |
| --------- | ------------------------------------------------------------ |
| 기본 속성 | 비즈니스 프로세스에서 도출되는 본래의 속성이다.              |
| 설계 속성 | 데이터 모델링 과정에서 발생되는 속성이며  상품 코드처럼 유일한 값을 부여한다. |
| 파생 속성 | 합계나 평균처럼 다른 속성에 의해서 만들어지는 속성이다.      |



## 관계
<br>


관계는 엔터티간의 관련성을 의미하며 존재 관계와 행위 관계로 분류된다.



### 관계의 종류
<br>
​	

- **존재 관계** 
  - 존재 관계는 엔터티 간의 상태를 의미한다.
  - 부모와 자식처럼 존재에 영향을 미치는 관계를 의미한다고 보면 된다.
- **행위 관계** 
  - 행위 관계는 엔티티 간에 어떤 행위가 있느 것으로, 계좌를 사용해서 주문을 발주하는 관계가 만들어진다.





### 식별관계와 비식별 관계

<br>

- **식별 관계**
  \- 실선으로 표현
  \- strong entity의 기본키를 다른 엔티티(weak entity)의 기본키의 하나로 공유하는 것
  \- strong entity의 기본키 값이 변경되면, (기본키를 공유받은) 식별 관계에 있는 엔티티의 값도 변경됨
  \- 강한 개체(strong entity)는 독립적으로 존재할 수 있음
  \- 강한 개체는 다른 엔티티와 관계를 가질 때 다른 엔티티에게 기본키를 공유함
  \- 강한 개체는 식별 관계로 표현됨
- **비식별 관계**
  \- 점선으로 표현
  \- strong entity의 기본키를 다른 엔티티의 기본키가 아닌 일반 칼럼으로 관계를 가지는 것



## 엔티티 식별자

<br>

식별자 라는 것은 엔티티를 대표할 수 있는 유일성을 만족하는 속성이며, id, 계좌번호, 주민등로번호 같은 유일한 존재로서 무언가를 대표하는 것이다.





### 주식별자(기본키)
<br>


데이터베이스에서 primary key가 되는 녀석이다.



4가지 특성이 있다.



- 최소성 
- 대표성
- 유일성
- 불변성 
  - 변경은 가능하나 가급적 변경되지 않아야한다. 완전 불가능은 아니다.



데이터베이스에서 키는 다섯 종류가 있다.



- 기본키 : 후보키 중에서 엔티티를 대표할 수 있는 키이다.
- 후보키 : 후보키는 유일성과 최소성을 만족하는 키이다.
- 슈퍼키 : 슈퍼키는 유일성은 만족하지만 최소성은 만족하지 않는 키이다.
- 대체키 : 후보키 중에서 기본키가 되지 못하고 남은 키이다.
- 외래키 : 하나 혹은 다수의 다른 테이블의 기본 키 필드를 가리키는 것으로 참조 무결성을 확인하기 위해서 사용된다.



### 식별자의 분류
<br>


**대표성 여부에 따른 식별자의 종류**



- **주식별자** : 유일성과 최소성을 만족하면서 엔티티를 대표하는 식별자. 참조 관계로 연결될 수 있다.
- **보조 식별자** : 유일성과 최소성은 만족하지만 대표성을 만족하지 못하는 식별자이다. (후보키)



**생성 여부에 따른 식별자의 종류**



- **내부 식별자** : 내부 식별자는 엔터티 내부에서 스스로 생성되는 식별자이다.
- **외부 식별자** : 다른 엔터티와의 관계로 인하여 만들어지는 식별자이다. (외래키)



**속성의 수에 따른 식별자의 종류**



- **단일 식별자** : 하나의 속성으로 구성된다.
- **복합 식별자** : 두 개 이상의 속성으로 구성된다.



**대체 여부에 따른 식별자의 종류**



- **본질 식별자** : 비즈니스 프로세스에서 만들어지는 식별자이다.
- **인조 식별자 **: 인위적으로 만들어지는 식별자이다. 주로 주식별자가 없거나 주식별자가 너무 많은 경우 사용 된다. 
