---
title:  "Pandas Series"
excerpt: "데이터 생성과 연산 기본"
categories:
 - Pandas
tags:
 - [pandas,python,study,TIL,data]
last_modified_at: 2021-11-22
toc: true
toc_sticky: true
---

# Pandas (series)

## Series 사용 

index - value 로만 이루어진 Series 데이터 타입을 사용해보자

### 생성




```python
import pandas as pd


series1 = pd.Series([10,20,30,40])
series1
```




    0    10
    1    20
    2    30
    3    40
    dtype: int64



시리즈 타입은 데이터에 한 가지 데이터 타입만을 허용한다.<br>
만약 위 코드에서 '50' 이라는 문자열 데이터를 입력하게 되면 전체 데이터 타입은 Object 타입으로 자동 변환된다.<br>

### 인덱스 포함 생성




```python
series1 = pd.Series([10,20,30,40],index=['일','이','삼','사'],name='테스트')
series1
```




    일    10
    이    20
    삼    30
    사    40
    Name: 테스트, dtype: int64



index를 별도로 초기화 해줄 수 있다.<br>
별로 지정해주지 않는다면 1부터 정수로 순서에 따라 인덱스가 부여된다.<br>
또한 name= 을 통해 데이터에 이름을 추가해줄 수 있다.<br>

### 딕셔너리 형태로 생성


```python
series2 = pd.Series({'Name':'윤정호', 'job':'학생', '희망 연봉' : '2억', '거주지': '수원'}, name='profile')
series2
```




    Name     윤정호
    job       학생
    희망 연봉     2억
    거주지       수원
    Name: profile, dtype: object



딕셔너리의 키 값이 데이터의 index로, 밸류 값이 데이터의 값으로 들어가게 된다.
<br>
### 데이터 연산


```python
print(series1.sum())
print(series1.mean())
```

    100
    25.0
    

pandas는 numpy의 연산 함수가 사용 가능하다.<br>

### Series 인덱싱


```python
s3 = {1:'테스트1', 2: '테스트2',3:'테스트3'}
series3 = pd.Series(s3)

print(series3[1:3]) # 슬라이싱을 사용한 인덱싱


print(series2['거주지'])
print(series3[1])
```

    2    테스트2
    3    테스트3
    dtype: object
    수원
    테스트1
    

Series는 인덱스를 이용해 데이터를 호출 할 수 있다.<br>
슬라이싱을 이용하게 되면 지정한 인덱스가 아닌 데이터 구조상 인덱스를 기준으로 index, value 모든 값을 출력한다.


```python
series2 =='윤정호'
```




    Name      True
    job      False
    희망 연봉    False
    거주지      False
    Name: profile, dtype: bool



데이터 값을 기준으로 일치 여부에 따라 boolean 값을 받을 수 있다.
<br> 이를 이용한 인덱스 또한 가능하다.



```python
series2[series2 =='윤정호']
```




    Name    윤정호
    Name: profile, dtype: object



Series의 기본적인 사용법을 알아보았다.<br>
실제 업무 프로세스에서 쓰이는 데이터는 series의 구조보다는 대부분 Data Frame의 구조로 사용 된다.<br>
그러므로 짧게 마무리 해보겠당 

