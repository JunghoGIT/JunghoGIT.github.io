---
title:  "DML 1"
excerpt: "INSERT,UPDATE,DELETE"
categories:
 - SQL
tags:
 - [DATA,SQL,study,TIL]
last_modified_at: 2021-11-09
toc: true
toc_sticky: true
---


# DML (INSERT, UPDATE, DELETE)



DDL을 통해 테이블의 구조를 만들었으니 이제 데이터로 테이블을 채워 넣을 차례이다.

이때 DML을 통해 다양한 기능을 수행할 수 있다.



## INSERT



insert 문을 통해 데이터를 입력할 수 있다.



### 기본형태 



```sql
insert into 테이블명(칼럼명,칼럼명...)VALUES(데이터값,데이터값...)
-- 위의 방식을 사용시 칼럼명과 데이터 값의 갯수는 동일해야하면 입력한 순서대로 1:1 대응하여 입력된다.
-- 문자열의 경우 작은 따옴표로 묶어준다.
insert into 테이블명 values(데이터값,데이터값...);
-- 특정 테이블의 모든 칼럼에 대한 데이터를 삽입하는 경우 칼럼명을 삭제 할 수 있다.
-- 항상 데이터타입을 순서대로 삽입하는 것에 주의하여야 한다.

```



### SELECT 문 사용



```sql
insert into 테이블 명 select * from 테이블명2
-- 데이터를 복붙한다고 보면 된다.
-- 당연히 칼럼의 구조가 같아야 가능하다.
```



### Nologging 문 사용



```sql
ALTER TABLE 테이블명 NOLOGGING ;

-- 데이터 베이스에 데이터를 입력하면 로그파일에 그 정보를 기록함
-- check point 이벤트가 발생하면 로그파일 데이터를 데이터 파일에 저장
-- nologging 옵션은 로그파일의 기록을 최소화 시켜서 입력시 성능을 향상 시키는 방법이다.
-- buffer cache 라는 메모리 영역을 생략하고 기록한다.

-- 속도향상을 위해 사용
```





## UPDATE



### 기본 사용법



```sql
UPDATE 테이블명 SET 칼럼명='입력할 값' Where ~조건~ ;

```



update문을 사용할 때는 조건문을 잘 사용하여 칼럼의 모든 row의 값이 변하지 안하게 where 조건문을 통해 내가 원하고자 하는 속성의 값만 변경하는 것이 매우 중요하다.



## DELETE



DELETE문은 조건을 검색하여 해당하는 **'행'**을 삭제한다. 

이또한 update와 마찬가지로 조건문을 제대로 입력하지 않으면 모든 데이터가 삭제 될 수 있으니 주의를 요한다.

테이블의 용량이 초기화 되지는 않는다.



### 기본 사용법



```sql
DELETE from 테이블명 where 조건 ;
-- 테이블 용량이 초기화 되지 않는다.
TRUNCATE TABLE 테이블명;
-- 테이블의 용량이 초기화 된다.
```

