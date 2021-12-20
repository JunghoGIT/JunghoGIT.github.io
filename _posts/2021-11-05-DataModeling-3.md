---
title:  "데이터 모델링 3"
excerpt: "정규화와 반정규화"
categories:
 - SQL
tags:
 - [data,SQL,study,TIL]
last_modified_at: 2021-11-05
toc: true
toc_sticky: true
---

# 정규화와 반정규화



`정규화`와 `반정규화`는 데이터 모델링 과정에서 꼭 필요한 단계이다.

좋은 데이터 베이스란 중복된 데이터가 없어야 하며 메모리는 최소화 하고 연산 속도는 빨라야 한다.

앞서 비즈니스 프로세스를 파악해 entity,속성,관계,식별자를 정의 했다면, 이젠 정규화와 반정규화를 통해 데이터 베이스를 좀 더 체계적으로 만들어 볼 차례이다.



![정규화반정규화1](\assets\images\정규화반정규화1.jpg)

위에 그림과 같이 정규화와 반정규화는 실행함에 따라 몇 몇 단점들이 발생되는데 이를 서로의 장점으로 보완하는 구조이다.



일관성과 무결성을 우선으로 한다면 정규화에 좀 더 비중을 두면 되는 것이고, 데이터베이스의 성능과 단순화를 목적에 둔다면 반정규화에 비중을 두고 데이터 베이스를 설계하면 된다.





## 정규화 



**정규화**는 중복된 데이터를 허용하지 않음으로서 무결성을 유지하고 DB의 저장용량을 최적화 하는 것을 목표로 가진다.

하나의 종속성이 하나의 릴레이션에 표현될 수 있도록 분해해 가는 과정이라 할 수 있다.

이상( Anomaly) 현상을 방지하는 효과를 기대할 수 있다.



### 정규화의 원칙



- 데이터의 중복이 감소 되어야 한다.
- 정보가 사라지지 않아야함 (정보의 무손실)
- 독립된 관계성은 독립된 릴레이션으로 분리해서 표현해야함 (분리의 원칙)
- 같은 의미의 정보를 유지하면서 더 바람직한 구조로 변환해야 함



### 정규화의 단계



정규화에는 여러 단계가 있으며 순서와 조건들이 존재한다.

정규화의 단계는 다음과 같으며 일반적인 경우 제3정규형까지만 한다.



1. 비정규형
2. 제1정규형 : 원자값이 아닌 도메인 분해
3. 제2정규형 : 부분 함수 종속 제거
4. 제3정규형 : 이행 함수 종속 제거
5. BCNF(3.5정규형) : 결정자가 후보키가 아닌 함수 종속 제거
6.  제4정규형 : 다중치 종속제거
7.  제5정규형 : 후보키를 통하지 않은 조인 종속 제거



### 제1 정규형



제1 정규형에 대해서 가장 많이 찾아볼 수 있는 설명은 `'제1 정규형 과정을 통해 원자값이 아닌 도메인을 분해하여 어떤 릴레이션 R에 속한 모든 도메인이 원자값으로만 되어 있도록 설계'`라는 텍스트이다.

하지만 원자값이란 말이 이해하기 어려운데 다행히 이에 대해 [설명한 영상](https://www.youtube.com/watch?v=RXQ1kZ_JHqg)이 있다. 

이 영상을 보면 크리스토퍼 J. 데이트는 원자값이란 표현에 애매모호함에 새로운 표현으로 정의를 내렸는데 다음과 같다.



> 크로스토퍼 J. 데이트의 1정규형 저의
>
> 1. 열에는 위-아래의 순서가 없다.
> 2. 행에는 좌-우의 순서가 없다.
> 3. 중복되는 열이 없다.
> 4. 모든 열과 행의 중복지점에는 해당되는 분야에서 한 개의 값을 가진다.
> 5. 모든 행은 규칙적이다.



4번 정의가 원자값의 표현으로 부족한 1정규형의 설명을 이해하기 쉽도록 다르게 표현한 것이다.



간단히 말하자면 하나의 속성에는 하나의 값만 갖도록 한다는 것이다.



예를 들어 

| 이름   | 연락처                          |
| ------ | ------------------------------- |
| 윤정호 | 010-1234-5678<br />031-123-5678 |



위의 테이블이 있다고 쳤을 때 하나의 속성에 휴대폰번호와 집전화 두가지를 모두 갖고 있기 때문에 제 1정규형에 위배되는 테이블이다.



| 이름   | 집전화       | 휴대폰        |
| ------ | ------------ | ------------- |
| 윤정호 | 031-123-5678 | 010-1234-5678 |



이런식으로 하나의 속성에 하나의 값만 갖도록 테이블에 칼럼을 만들어준다거나 테이블을 분리함으로서 제1 정규형을 만족시키는 테이블을 만들 수 있다.



### 제2 정규형



제2 정규형은 **부분 함수 종속이 없으며 완전 함수적 종속을 충족**시키는 정규형이다.



제2 정규형은 우선 기본키가 2개 이상인 **복합키**일 경우에만 시행된다.



"부분 함수 종속"이라는 의미는 밑의 그림과 같다.



![2정규화](\assets\images\2정규화.jpg)

C속성은 기본키 A,B 복합 속성으로 이루어진 기본키에 완전 함수적 종속 관계이지만 D,E 속성은 기본키 B에만 종속 관계를 갖고 있기 때문에 이 테이블은 완전 함수적 종속 관계라고 할 수 없다.

이때는 2개의 릴레이션(테이블)로 분리해줘야 한다.

[기본키 A - 기본키 B - C] 의 형태를 가진 테이블과 [기본키 B - D - E] 형태의 테이블로 나누어준다면 제2 정규형을 만족할 수 있게 된다.



### 제3 정규형



제3 정규형의 타겟은 **이행적 함수 종속**이다.

제3 정규형은 제1 정규형과 제2 정규형을 모두 만족 할때에 시행한다.

우선 이행적 함수 종속이 무엇인지 이해가 필요하다.

 

| 회원ID(기본키) | 이름   | 통신사 | 통신사 고객센터 번호 |
| -------------- | ------ | ------ | -------------------- |
| yoonjungho     | 윤정호 | KT     | 123                  |



억지스러운 테이블이지만 위 테이블을 예로 들자면 제1 정규형과 제 2정규형을 만족하고 모든 속성은 기본키에 종속 관계를 가진다.

하지만 통신사 속성와 통신사 고객센터 번호는 족송 관계일 수 있다.

이런 상황을 이행적 함수 종속 관계라고 한다.

위의 경우는 간단하게

| 통신사 | 통신사 고객센터 번호 |
| ------ | -------------------- |
| KT     | 123                  |
| SKT    | 124                  |
| LG     | 125                  |

이런식으로 별도의 테이블을 만들어줌으로서 제 3 정규형을 만족 시킬 수 있다.



### BCNF



**BCNF**는 제3 정규화를 진행한 테이블에 대해 모든 결정자가 후보키가 되도록 테이블을 분해하는 것이다.



제 3.5정규형이라고도 불리며,  BCNF를 만족한다면 제 3정규형을 만족한다고 볼 수 있지만 역의 경우는 아닐 수도 있다.



쉽게 말해 어떤 A속성이 B속성의 결정자가 되는 속성이지만 후보키가 될 수 없을 때 A속성과 B속성을 따로 분리하여 테이블을 만드는 것을 의미한다.





## 반정규화



`반정규화`란 보통 정규화 이후에 발생하는 속도 저하의 문제를 해결하기 위해 하는 최적화 기법이다.

보통 하나 이상의 테이블에 데이터를 중복으로 배치하여 시스템의 성능 향상, 개발 및 운영의 편의성등을 추구한다. 

즉 의도적으로 정규화 원칙을 위배한다고 볼 수 있다.

하지만 반정규화를 한다고 무조건 적으로 성능이 향상 되는 것은 아니다 모든 것은 과하면 독이 되듯이 과한 반정규화는 오히려 성능 저하를 초래할 수 있다.



반정규화시 조인 비용이 줄어들기 때문에 빠른 데이터 조회가 가능해지고 쿼리문이 비교적 심플 해지는 장점이 있다.

단점으로는 데이터 갱신이나 삽입 비용이 높아지고 데이터 간의 일관성과 무결성이 깨질 수 있는 위험이 있다.

또한 중복 데이터가 발생하면서 필요한 메모리의 양이 많아지게 된다.

그러므로 `데이터의 일관성,무결성`과 `데이터베이스의 성능과 단순화` 두 가지 장점 중에 어느 것을 우선으로 할지 생각하여야 한다.





### 반정규화 방법



반정규화 방법에는 크게 4가지가 있다.



- **테이블 병합** : 잦은 join 사용으로 나오는 단점을 해소함으로서 성능 향상을 추구한다.



- **테이블 분할** : 테이블을 수평 또는 수직으로 분할 한다.



- **테이블 추가** :  작업의 효율성을 향상 시키기 위해 테이블을 추가한다.



- **칼럼 추가** : Join의 사용을 줄인다거나 자주 쓰는 계산 값을 추가한다.

  



### 테이블 병합



테이블 병합 방식은 비즈니스 로직 상 Join되는 경우가 많아 통합하는 것이 성능 측면에서 유리할 경우에 고려된다.



테이블 병합의 방법으론 3가지 정도가 있다.



- **1:1 관계 테이블 병합**
- **1:N 관계 테이블 병합**
- **super sub type 테이블 병합**
  - OneToOne type : 슈퍼타입과 서브타입을 개별 테이블로 도출한다. 관리가 어려운 단점이 있다
  - Plus type : 슈퍼타입과 서브타입 테이블로 도출한다. 조인이 발생하며 관리가 어렵다.
  - Single type : 슈퍼타입과 서브타입을 하나의 테이블로 도출한다. 조인성능이 좋고 관리도 용이 but 입출력 성능 이 안 좋다.



 ### 테이블 분할



테이블 분할은 2가지 방식이 있다.



- **수직 분할** : 칼럼 단위로 테이블을 1:1 분리한다.
- **수평 분할**: row(행) 단위로 테이블을 분리한다.



### 테이블 추가



- **중복 테이블 추가**
  - 타 업무 또는 타 서버에 있는 테이블과 동일한 구조의 테이블을 추가한다. 
  - 원격 Join 방지
- **통계 테이블 추가** 
  - 통계값을 미리 계산해서 저장하는 테이블 추가
- **이력 테이블 추가**
  - 마스터 테이블에 존재하는 row를 트랜재션 발생 시점에 따라 복사해두는 테이블 추가
- **부분 테이블 추가**
  - 자주 조회되는 칼럼들만 별도로 모아놓는 테이블 추가



### 칼럼 추가



- **중복 칼럼 추가**
  - Join 프로세스를 줄이기 위해 중복 칼럼 추가
  - SELECT 비용은 감소하나 Update 비용은 증가
- **파생 칼럼 추가**
  - 계산을 통해 얻어지는 결과 값을 테이블에 칼럼으로 저장
- **이력 테이블 칼럼 추가**
  - 이력 테이블에 기능성 칼럼추가 (최신 여부, 시작일/종료일 등)


