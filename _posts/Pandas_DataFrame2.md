---
title:  "Pandas DataFrame 2"
excerpt: "DataFrame 필터를 이용한 추출"
categories:
 - Pandas
tags:
 - [pandas,python,study,TIL,Data]
last_modified_at: 2021-11-23
toc: true
toc_sticky: true
---

# Data Frame (Pandas)



## 데이터 불러오기


```python
import pandas as pd

df1 = pd.read_csv('Pandas_learn.csv')

df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>이름</th>
      <th>생년월일</th>
      <th>거주지</th>
      <th>학교</th>
      <th>재산(만)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1번</td>
      <td>윤정호</td>
      <td>1995-03-03</td>
      <td>수원</td>
      <td>동국대</td>
      <td>5000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2번</td>
      <td>홍길동</td>
      <td>1997-07-07</td>
      <td>서울</td>
      <td>서울대</td>
      <td>4000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3번</td>
      <td>스미스</td>
      <td>1999-09-09</td>
      <td>뉴욕</td>
      <td>하버드</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4번</td>
      <td>나카무라</td>
      <td>1990-04-04</td>
      <td>도쿄</td>
      <td>동경대</td>
      <td>3000</td>
    </tr>
  </tbody>
</table>
</div>



이전 글에서 만들어두었던 데이터를 read_csv() 함수를 통해 불러왔다.
<br> 저장과 마찬가지로 파일 경로와 파일 명을 입력해서 불러올 수 있다.
<br>





## 데이터 행 추출


```python
df1.iloc[1]
```




    Unnamed: 0            2번
    이름                   홍길동
    생년월일          1997-07-07
    거주지                   서울
    학교                   서울대
    재산(만)               4000
    Name: 1, dtype: object



iloc를 통해 인덱싱을 이용해서 특정 행을 출력 할 수 있다.


```python
df1.iloc[1:]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>이름</th>
      <th>생년월일</th>
      <th>거주지</th>
      <th>학교</th>
      <th>재산(만)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2번</td>
      <td>홍길동</td>
      <td>1997-07-07</td>
      <td>서울</td>
      <td>서울대</td>
      <td>4000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3번</td>
      <td>스미스</td>
      <td>1999-09-09</td>
      <td>뉴욕</td>
      <td>하버드</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4번</td>
      <td>나카무라</td>
      <td>1990-04-04</td>
      <td>도쿄</td>
      <td>동경대</td>
      <td>3000</td>
    </tr>
  </tbody>
</table>
</div>



파이썬의 슬라이싱을 이용한 인덱싱 또한 가능하다.<br>
복수의 행을 추출할 때는 series가 아닌 dataframe의 형태로 출력 된다.


```python
df1.iloc[1,3]
```




    '서울'



df.iloc[행,열] 방식으로 인덱싱을 함으로서 특정 범위의 값을 추출할 수 있다.<br>

## 데이터 정렬




```python
df1.sort_values(by='재산(만)')
#df1.sort_values(by='재산(만)',ascending=False)


```

재산을 기준으로 데이터를 정렬하여 추출하였다.<br>

defalut는 오름차순으로 정렬이 되며, 위 주석과 같이 ascending=False 를 설정해주면 내림차순으로 정렬된다.
<br>
정렬의 조건을 여러개 두고 싶다면 by=['칼럼1','칼럼2'] 의 형식으로 해주면 칼럼1을 기준으로 먼저 정렬해주고 이후에 동일한 값 안에선 칼럼 2를 기준으로 정렬된다.<br>
정렬방식 또한 ascending=[true,false] 의 방식으로 지정 가능하다.

## 데이터 필터


### counts


```python

df1.iloc[1,3]='수원' # 중복값을 만들기 위해 값을 변경함 ㅠ 

df1[['거주지']].value_counts()
```




    거주지
    수원     2
    도쿄     1
    뉴욕     1
    dtype: int64



칼럼에 동일한 값의 개수를 계산해준다.

### 특정 항목에 대한 데이터 추출


```python
temp = (df1['거주지']=='수원')

df1.loc[temp]

#df1.loc[(df1['거주지']=='수원')] = 같은 결과이다.
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>이름</th>
      <th>생년월일</th>
      <th>거주지</th>
      <th>학교</th>
      <th>재산(만)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1번</td>
      <td>윤정호</td>
      <td>1995-03-03</td>
      <td>수원</td>
      <td>동국대</td>
      <td>5000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2번</td>
      <td>홍길동</td>
      <td>1997-07-07</td>
      <td>수원</td>
      <td>서울대</td>
      <td>4000</td>
    </tr>
  </tbody>
</table>
</div>



특정 칼럼에 해당 값을 가진 행만 추출하는 방식이다.<br>



```python
df1.loc[~temp]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>이름</th>
      <th>생년월일</th>
      <th>거주지</th>
      <th>학교</th>
      <th>재산(만)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>3번</td>
      <td>스미스</td>
      <td>1999-09-09</td>
      <td>뉴욕</td>
      <td>하버드</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4번</td>
      <td>나카무라</td>
      <td>1990-04-04</td>
      <td>도쿄</td>
      <td>동경대</td>
      <td>3000</td>
    </tr>
  </tbody>
</table>
</div>



위 코드처럼 '~' 를 붙여준다면 반대되는 조건의 값만 추출 할 수 있다.


```python
temp2 = (df1['생년월일']=='1995-03-03')

df1.loc[temp & temp2]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>이름</th>
      <th>생년월일</th>
      <th>거주지</th>
      <th>학교</th>
      <th>재산(만)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1번</td>
      <td>윤정호</td>
      <td>1995-03-03</td>
      <td>수원</td>
      <td>동국대</td>
      <td>5000</td>
    </tr>
  </tbody>
</table>
</div>



And 를 의미하는 '&' 를 이용해 두 가지 이상의 조건을 만족하는 항목에 대한 추출도 가능하다.<br> Or의 경우는 '|'를 이용해서 표현할 수 있다. 


```python
df1[df1.이름=='윤정호']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>이름</th>
      <th>생년월일</th>
      <th>거주지</th>
      <th>학교</th>
      <th>재산(만)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1번</td>
      <td>윤정호</td>
      <td>1995-03-03</td>
      <td>수원</td>
      <td>동국대</td>
      <td>5000</td>
    </tr>
  </tbody>
</table>
</div>



위 코드처럼 데이터명[데이터명.비교연산자 '값'] 의 순서로도 데이터를 필터링해서 추출할 수 있다.


```python
df1.query("거주지 == '수원'")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>이름</th>
      <th>생년월일</th>
      <th>거주지</th>
      <th>학교</th>
      <th>재산(만)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1번</td>
      <td>윤정호</td>
      <td>1995-03-03</td>
      <td>수원</td>
      <td>동국대</td>
      <td>5000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2번</td>
      <td>홍길동</td>
      <td>1997-07-07</td>
      <td>수원</td>
      <td>서울대</td>
      <td>4000</td>
    </tr>
  </tbody>
</table>
</div>



query 함수를 통해 SQL 의 where 조건 같은 구조로 데이터를 추출할 수 있다.<br>
단점은 iloc 에 비해 속도가 느리다.


```python
df1.query("(학교 == '서울대') and (거주지 == '수원')")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>이름</th>
      <th>생년월일</th>
      <th>거주지</th>
      <th>학교</th>
      <th>재산(만)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2번</td>
      <td>홍길동</td>
      <td>1997-07-07</td>
      <td>수원</td>
      <td>서울대</td>
      <td>4000</td>
    </tr>
  </tbody>
</table>
</div>



and,or,not 같은 논리 연산자와 in 연산자 또한 사용 가능하다는 장점이 있다.
