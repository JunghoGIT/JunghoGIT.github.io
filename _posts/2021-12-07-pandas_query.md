---
title:  "Pandas query"
excerpt: "query 함수를 사용해보자."
categories:
 - Pandas
tags:
 - [pandas,python,study,TIL,data]
last_modified_at: 2021-12-07
toc: true
toc_sticky: true
---

# Query

<br>

pandas 는 .query() 함수를 통해 질의 형식으로 조건을 통한 데이터 필터링이 가능하다.

<br>

가독성과 편의성이 좋아 자주 사용 되지만 loc나 iloc에 비해 속도가 느리다는 단점이 있다.

<br>

기본적으로 포함된 기능은 다음과 같다.
<br>
- 비교 연산자
- in 연산자
- 논리 연산자
- 외부 변수, 함수 참조 연산
- 인덱스 검색
- 문자열 부분 검색 
<br>

학습용 데이터 셋을 만들고 함수를 사용하면서 알아보자.

<br>


```python
import pandas as pd
import numpy as np

list1 = ['정호','노제','노제','윈터','정호','노제','윈터','정호','노제','윈터','정호']
list2 = ['11/25','11/25','11/25','11/25','11/26','11/27','11/27','11/28','11/28','11/28','11/29']
list3 = ['아이폰','갤럭시','갤럭시','에어팟','에어팟','갤럭시','에어팟','아이폰','갤럭시','아이폰','에어팟']
list4 = [1,2,1,3,2,1,1,2,4,3,4]
df= pd.DataFrame({'판매원' : list1 , '판매날짜':list2 , '판매물품':list3, '판매개수':list4 })

df

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
      <th>판매원</th>
      <th>판매날짜</th>
      <th>판매물품</th>
      <th>판매개수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>정호</td>
      <td>11/25</td>
      <td>아이폰</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>노제</td>
      <td>11/25</td>
      <td>갤럭시</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>노제</td>
      <td>11/25</td>
      <td>갤럭시</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>윈터</td>
      <td>11/25</td>
      <td>에어팟</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>정호</td>
      <td>11/26</td>
      <td>에어팟</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>노제</td>
      <td>11/27</td>
      <td>갤럭시</td>
      <td>1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>윈터</td>
      <td>11/27</td>
      <td>에어팟</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7</th>
      <td>정호</td>
      <td>11/28</td>
      <td>아이폰</td>
      <td>2</td>
    </tr>
    <tr>
      <th>8</th>
      <td>노제</td>
      <td>11/28</td>
      <td>갤럭시</td>
      <td>4</td>
    </tr>
    <tr>
      <th>9</th>
      <td>윈터</td>
      <td>11/28</td>
      <td>아이폰</td>
      <td>3</td>
    </tr>
    <tr>
      <th>10</th>
      <td>정호</td>
      <td>11/29</td>
      <td>에어팟</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



이번 포스팅에도 어김없이 저번에 만든 데이터를 재활용한다.

## 비교 연산자

우리가 가장 자주 쓰는 연산자인 비교 연산자 (==,>,>=,!=) 을 통해 데이터를 필터링 할 수 있다.



```python
df.query("판매개수 == 2")
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
      <th>판매원</th>
      <th>판매날짜</th>
      <th>판매물품</th>
      <th>판매개수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>노제</td>
      <td>11/25</td>
      <td>갤럭시</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>정호</td>
      <td>11/26</td>
      <td>에어팟</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>정호</td>
      <td>11/28</td>
      <td>아이폰</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.query("판매개수 >= 2")
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
      <th>판매원</th>
      <th>판매날짜</th>
      <th>판매물품</th>
      <th>판매개수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>노제</td>
      <td>11/25</td>
      <td>갤럭시</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>윈터</td>
      <td>11/25</td>
      <td>에어팟</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>정호</td>
      <td>11/26</td>
      <td>에어팟</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>정호</td>
      <td>11/28</td>
      <td>아이폰</td>
      <td>2</td>
    </tr>
    <tr>
      <th>8</th>
      <td>노제</td>
      <td>11/28</td>
      <td>갤럭시</td>
      <td>4</td>
    </tr>
    <tr>
      <th>9</th>
      <td>윈터</td>
      <td>11/28</td>
      <td>아이폰</td>
      <td>3</td>
    </tr>
    <tr>
      <th>10</th>
      <td>정호</td>
      <td>11/29</td>
      <td>에어팟</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.query("판매원 == '노제'")
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
      <th>판매원</th>
      <th>판매날짜</th>
      <th>판매물품</th>
      <th>판매개수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>노제</td>
      <td>11/25</td>
      <td>갤럭시</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>노제</td>
      <td>11/25</td>
      <td>갤럭시</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>노제</td>
      <td>11/27</td>
      <td>갤럭시</td>
      <td>1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>노제</td>
      <td>11/28</td>
      <td>갤럭시</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



 " " 안에 원하는 조건을 작성한다.<br>
 따로 칼럼명을 따옴표로 표시할 필요는 없으나, 비교할 값이 문자열일 경우엔 해당 문자열에 작은 따옴표로 표시하여야 한다.

 <br>

 ## in 연산자

 칼럼에 리스트or튜플의 값이 하나라도 존재하면 참,아니라면 거짓으로 데이터를 추출한다.<br>
 in 과 not in 을 사용하는데 이는 곧 == , != 와 같은 의미이다.



```python
df.query("판매개수 in [1,4]")
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
      <th>판매원</th>
      <th>판매날짜</th>
      <th>판매물품</th>
      <th>판매개수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>정호</td>
      <td>11/25</td>
      <td>아이폰</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>노제</td>
      <td>11/25</td>
      <td>갤럭시</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>노제</td>
      <td>11/27</td>
      <td>갤럭시</td>
      <td>1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>윈터</td>
      <td>11/27</td>
      <td>에어팟</td>
      <td>1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>노제</td>
      <td>11/28</td>
      <td>갤럭시</td>
      <td>4</td>
    </tr>
    <tr>
      <th>10</th>
      <td>정호</td>
      <td>11/29</td>
      <td>에어팟</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.query("판매원 != ['정호','윈터']")
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
      <th>판매원</th>
      <th>판매날짜</th>
      <th>판매물품</th>
      <th>판매개수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>노제</td>
      <td>11/25</td>
      <td>갤럭시</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>노제</td>
      <td>11/25</td>
      <td>갤럭시</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>노제</td>
      <td>11/27</td>
      <td>갤럭시</td>
      <td>1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>노제</td>
      <td>11/28</td>
      <td>갤럭시</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



## 논리 연산자

<br>

and, or, not 을 사용해 논리 연산이 가능하다.
<br>

true and true = true<br>
true and false = false<br>
true or false = true <br>
false or false = false<br>


주의할 점은 모두 소문자를 사용해야 한다.


```python
df.query("(판매개수 in [1,4]) and (판매원 != ['정호','윈터'])")
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
      <th>판매원</th>
      <th>판매날짜</th>
      <th>판매물품</th>
      <th>판매개수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>노제</td>
      <td>11/25</td>
      <td>갤럭시</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>노제</td>
      <td>11/27</td>
      <td>갤럭시</td>
      <td>1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>노제</td>
      <td>11/28</td>
      <td>갤럭시</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.query("(판매개수 in [1,4]) and not (판매원 != ['정호','윈터'])")
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
      <th>판매원</th>
      <th>판매날짜</th>
      <th>판매물품</th>
      <th>판매개수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>정호</td>
      <td>11/25</td>
      <td>아이폰</td>
      <td>1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>윈터</td>
      <td>11/27</td>
      <td>에어팟</td>
      <td>1</td>
    </tr>
    <tr>
      <th>10</th>
      <td>정호</td>
      <td>11/29</td>
      <td>에어팟</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



## 외부 변수, 함수 참조 연산



<br>
쿼리문을 날리는 dataframe 외부의 변수나 함수를 조건 값으로 하여 연산할 수 있다.
<br><br>

**중요한 점은 외부 변수명과 함수명 앞에 필수적으로 @ 를 붙여 사용해야 한다.**


```python
x = 3

df.query("판매개수 == @x")
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
      <th>판매원</th>
      <th>판매날짜</th>
      <th>판매물품</th>
      <th>판매개수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>윈터</td>
      <td>11/25</td>
      <td>에어팟</td>
      <td>3</td>
    </tr>
    <tr>
      <th>9</th>
      <td>윈터</td>
      <td>11/28</td>
      <td>아이폰</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
def sum(x,y):
  return x+y



df.query("판매개수 == @sum(1,2)")
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
      <th>판매원</th>
      <th>판매날짜</th>
      <th>판매물품</th>
      <th>판매개수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>윈터</td>
      <td>11/25</td>
      <td>에어팟</td>
      <td>3</td>
    </tr>
    <tr>
      <th>9</th>
      <td>윈터</td>
      <td>11/28</td>
      <td>아이폰</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



## 인덱스 검색

<br>

index를 통해 데이터를 필터링할 수 있다.

<br>

만약 index에 이름이 존재한다면 이름으로도 검색이 가능하다.

<br> 
index명과 칼럼명이 겹쳤을 땐 칼럼을 기준으로 검색한다.



```python
df.query("(index >=3 ) and (index <= 7)")
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
      <th>판매원</th>
      <th>판매날짜</th>
      <th>판매물품</th>
      <th>판매개수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>윈터</td>
      <td>11/25</td>
      <td>에어팟</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>정호</td>
      <td>11/26</td>
      <td>에어팟</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>노제</td>
      <td>11/27</td>
      <td>갤럭시</td>
      <td>1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>윈터</td>
      <td>11/27</td>
      <td>에어팟</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7</th>
      <td>정호</td>
      <td>11/28</td>
      <td>아이폰</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.index.name = '인덱스'

df.query("(인덱스 >=4 ) and (인덱스 <= 6)")
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
      <th>판매원</th>
      <th>판매날짜</th>
      <th>판매물품</th>
      <th>판매개수</th>
    </tr>
    <tr>
      <th>인덱스</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>정호</td>
      <td>11/26</td>
      <td>에어팟</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>노제</td>
      <td>11/27</td>
      <td>갤럭시</td>
      <td>1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>윈터</td>
      <td>11/27</td>
      <td>에어팟</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



## 문자열 부분검색

<br>

str.contains, str.startswith, str.endswith 3가지 문을 통해 문자열을 검색 할 수 있다.

<br>

### str.contains()

<br>

괄호안에 문자열이 포함된 값을 검색한다.


```python
df.query("판매원.str.contains('정')",engine='python')
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
      <th>판매원</th>
      <th>판매날짜</th>
      <th>판매물품</th>
      <th>판매개수</th>
    </tr>
    <tr>
      <th>인덱스</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>정호</td>
      <td>11/25</td>
      <td>아이폰</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>정호</td>
      <td>11/26</td>
      <td>에어팟</td>
      <td>2</td>
    </tr>
    <tr>
      <th>7</th>
      <td>정호</td>
      <td>11/28</td>
      <td>아이폰</td>
      <td>2</td>
    </tr>
    <tr>
      <th>10</th>
      <td>정호</td>
      <td>11/29</td>
      <td>에어팟</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



위의 engine='python' 설정을 안 해준다면 쿼리문을 해석하는 엔진의 기본 값이 'numexpr' 로 되어있는데 이 엔진은 문자열 검색함수를 해석하지 못 한다.


```python
df['temp']= ['Good','Python','good','Python','good','Good','Python','good','Good','good','Good']

df.query("temp.str.contains('G')",engine='python')
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
      <th>판매원</th>
      <th>판매날짜</th>
      <th>판매물품</th>
      <th>판매개수</th>
      <th>temp</th>
    </tr>
    <tr>
      <th>인덱스</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>정호</td>
      <td>11/25</td>
      <td>아이폰</td>
      <td>1</td>
      <td>Good</td>
    </tr>
    <tr>
      <th>5</th>
      <td>노제</td>
      <td>11/27</td>
      <td>갤럭시</td>
      <td>1</td>
      <td>Good</td>
    </tr>
    <tr>
      <th>8</th>
      <td>노제</td>
      <td>11/28</td>
      <td>갤럭시</td>
      <td>4</td>
      <td>Good</td>
    </tr>
    <tr>
      <th>10</th>
      <td>정호</td>
      <td>11/29</td>
      <td>에어팟</td>
      <td>4</td>
      <td>Good</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.query("temp.str.contains('G',case=False)",engine='python')
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
      <th>판매원</th>
      <th>판매날짜</th>
      <th>판매물품</th>
      <th>판매개수</th>
      <th>temp</th>
    </tr>
    <tr>
      <th>인덱스</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>정호</td>
      <td>11/25</td>
      <td>아이폰</td>
      <td>1</td>
      <td>Good</td>
    </tr>
    <tr>
      <th>2</th>
      <td>노제</td>
      <td>11/25</td>
      <td>갤럭시</td>
      <td>1</td>
      <td>good</td>
    </tr>
    <tr>
      <th>4</th>
      <td>정호</td>
      <td>11/26</td>
      <td>에어팟</td>
      <td>2</td>
      <td>good</td>
    </tr>
    <tr>
      <th>5</th>
      <td>노제</td>
      <td>11/27</td>
      <td>갤럭시</td>
      <td>1</td>
      <td>Good</td>
    </tr>
    <tr>
      <th>7</th>
      <td>정호</td>
      <td>11/28</td>
      <td>아이폰</td>
      <td>2</td>
      <td>good</td>
    </tr>
    <tr>
      <th>8</th>
      <td>노제</td>
      <td>11/28</td>
      <td>갤럭시</td>
      <td>4</td>
      <td>Good</td>
    </tr>
    <tr>
      <th>9</th>
      <td>윈터</td>
      <td>11/28</td>
      <td>아이폰</td>
      <td>3</td>
      <td>good</td>
    </tr>
    <tr>
      <th>10</th>
      <td>정호</td>
      <td>11/29</td>
      <td>에어팟</td>
      <td>4</td>
      <td>Good</td>
    </tr>
  </tbody>
</table>
</div>



case=False 를 contains()의 파라미터 값으로 넣어주면 대소문자 구분 없이 검색해준다.

<br>

### str.startswith()

<br>

특정 문자열로 시작하는 값을 찾을 수 있다.


```python
df.query("temp.str.startswith('P')",engine='python')
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
      <th>판매원</th>
      <th>판매날짜</th>
      <th>판매물품</th>
      <th>판매개수</th>
      <th>temp</th>
    </tr>
    <tr>
      <th>인덱스</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>노제</td>
      <td>11/25</td>
      <td>갤럭시</td>
      <td>2</td>
      <td>Python</td>
    </tr>
    <tr>
      <th>3</th>
      <td>윈터</td>
      <td>11/25</td>
      <td>에어팟</td>
      <td>3</td>
      <td>Python</td>
    </tr>
    <tr>
      <th>6</th>
      <td>윈터</td>
      <td>11/27</td>
      <td>에어팟</td>
      <td>1</td>
      <td>Python</td>
    </tr>
  </tbody>
</table>
</div>



### str.endswith()

<br>

특정 문자열로 끝나는 값을 찾을 수 있다.


```python
df.query("temp.str.endswith('d')",engine='python')
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
      <th>판매원</th>
      <th>판매날짜</th>
      <th>판매물품</th>
      <th>판매개수</th>
      <th>temp</th>
    </tr>
    <tr>
      <th>인덱스</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>정호</td>
      <td>11/25</td>
      <td>아이폰</td>
      <td>1</td>
      <td>Good</td>
    </tr>
    <tr>
      <th>2</th>
      <td>노제</td>
      <td>11/25</td>
      <td>갤럭시</td>
      <td>1</td>
      <td>good</td>
    </tr>
    <tr>
      <th>4</th>
      <td>정호</td>
      <td>11/26</td>
      <td>에어팟</td>
      <td>2</td>
      <td>good</td>
    </tr>
    <tr>
      <th>5</th>
      <td>노제</td>
      <td>11/27</td>
      <td>갤럭시</td>
      <td>1</td>
      <td>Good</td>
    </tr>
    <tr>
      <th>7</th>
      <td>정호</td>
      <td>11/28</td>
      <td>아이폰</td>
      <td>2</td>
      <td>good</td>
    </tr>
    <tr>
      <th>8</th>
      <td>노제</td>
      <td>11/28</td>
      <td>갤럭시</td>
      <td>4</td>
      <td>Good</td>
    </tr>
    <tr>
      <th>9</th>
      <td>윈터</td>
      <td>11/28</td>
      <td>아이폰</td>
      <td>3</td>
      <td>good</td>
    </tr>
    <tr>
      <th>10</th>
      <td>정호</td>
      <td>11/29</td>
      <td>에어팟</td>
      <td>4</td>
      <td>Good</td>
    </tr>
  </tbody>
</table>
</div>


[참고 블로그](https://m.blog.naver.com/wideeyed/221867273249)