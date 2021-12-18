---
title:  "Pandas Dataframe 합성"
excerpt: "dataframe을 합쳐보자."
categories:
 - Pandas
tags:
 - [pandas,python,study,TIL,data]
last_modified_at: 2021-12-11
toc: true
toc_sticky: true
---

# dataframe 합성

<br>

pandas 는 두 개 이상의 데이터프레임을 하나로 합치는 데이터 병합이나 연결을 지원한다.

<br>

## merge 함수

<br>

mertge 함수는 두 데이터 프레임의 공통으로 존재하는 열이나 인덱스를 기준으로 두 개의 테이블을 합친다. 이 때 기준이 되는 데이터를 key 라고 한다.

<br>

데이터셋을 만들고 기능을 살펴보자.

<br>

### 데이터 생성


```python

import pandas as pd
import numpy as np

list1 = ['A','B','C','D','E']
list2 = [4,5,3,6,9]
list3 = [0.66,0.77,0.88,0.99,1.11]
list4 = ['홍길동','윤길동','이길동','박길동','김길동']

df = pd.DataFrame({'코드':list1, 'int':list2,'float': list3 ,'이름':list4})


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
      <th>코드</th>
      <th>int</th>
      <th>float</th>
      <th>이름</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>4</td>
      <td>0.66</td>
      <td>홍길동</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>5</td>
      <td>0.77</td>
      <td>윤길동</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>3</td>
      <td>0.88</td>
      <td>이길동</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>6</td>
      <td>0.99</td>
      <td>박길동</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>9</td>
      <td>1.11</td>
      <td>김길동</td>
    </tr>
  </tbody>
</table>
</div>




```python
list5 = ['홍길동','윤길동','이길동','박길동','강길동','차길동']
list6 = [950303,941215,970205,930905,960413,970321]

df2 = pd.DataFrame({'이름': list5, '생년월일': list6})

df2
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
      <th>이름</th>
      <th>생년월일</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>홍길동</td>
      <td>950303</td>
    </tr>
    <tr>
      <th>1</th>
      <td>윤길동</td>
      <td>941215</td>
    </tr>
    <tr>
      <th>2</th>
      <td>이길동</td>
      <td>970205</td>
    </tr>
    <tr>
      <th>3</th>
      <td>박길동</td>
      <td>930905</td>
    </tr>
    <tr>
      <th>4</th>
      <td>강길동</td>
      <td>960413</td>
    </tr>
    <tr>
      <th>5</th>
      <td>차길동</td>
      <td>970321</td>
    </tr>
  </tbody>
</table>
</div>



### inner join 방식 

<br>

merge 함수는 SQL 에서 join 과 흡사한 기능을 수행하며, 기본 값은 inner join이다.
<br> SQL 의 JOIN 과 마찬가지로 두 데이터 간의 공통적으로 존재하는 값이 필요하다. <br>
<br>
위의 데이터프레임에서 공통으로 존재하는 이름 칼럼을 이용하여 merge 함수를 사용해보자.

<br> 



```python
pd.merge(df,df2)
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
      <th>코드</th>
      <th>int</th>
      <th>float</th>
      <th>이름</th>
      <th>생년월일</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>4</td>
      <td>0.66</td>
      <td>홍길동</td>
      <td>950303</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>5</td>
      <td>0.77</td>
      <td>윤길동</td>
      <td>941215</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>3</td>
      <td>0.88</td>
      <td>이길동</td>
      <td>970205</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>6</td>
      <td>0.99</td>
      <td>박길동</td>
      <td>930905</td>
    </tr>
  </tbody>
</table>
</div>



pd.merge()의 인자값으로 공통의 칼럼이 존재하는 데이퍼 프레임 2개를 주면 SQL 의 inner join 과 마찬가지로 key가 존재하는 부분만 연결된다.

### outer join 방식

outer join 방식은 한쪽에만 있는 key 값까지 모두 보여준다.


```python
pd.merge(df,df2, how='outer')
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
      <th>코드</th>
      <th>int</th>
      <th>float</th>
      <th>이름</th>
      <th>생년월일</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>4.0</td>
      <td>0.66</td>
      <td>홍길동</td>
      <td>950303.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>5.0</td>
      <td>0.77</td>
      <td>윤길동</td>
      <td>941215.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>3.0</td>
      <td>0.88</td>
      <td>이길동</td>
      <td>970205.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>6.0</td>
      <td>0.99</td>
      <td>박길동</td>
      <td>930905.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>9.0</td>
      <td>1.11</td>
      <td>김길동</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>강길동</td>
      <td>960413.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>차길동</td>
      <td>970321.0</td>
    </tr>
  </tbody>
</table>
</div>



SQL의 full outer join과 같은 결과를 얻을 수 있다.

### left, rigth join

기준이 되는 데이터의 모든 값에 키값이 존재하는 데이터만을 연결한다.


```python
pd.merge(df,df2, how='left')
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
      <th>코드</th>
      <th>int</th>
      <th>float</th>
      <th>이름</th>
      <th>생년월일</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>4</td>
      <td>0.66</td>
      <td>홍길동</td>
      <td>950303.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>5</td>
      <td>0.77</td>
      <td>윤길동</td>
      <td>941215.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>3</td>
      <td>0.88</td>
      <td>이길동</td>
      <td>970205.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>6</td>
      <td>0.99</td>
      <td>박길동</td>
      <td>930905.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>9</td>
      <td>1.11</td>
      <td>김길동</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df,df2, how='right')
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
      <th>코드</th>
      <th>int</th>
      <th>float</th>
      <th>이름</th>
      <th>생년월일</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>4.0</td>
      <td>0.66</td>
      <td>홍길동</td>
      <td>950303</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>5.0</td>
      <td>0.77</td>
      <td>윤길동</td>
      <td>941215</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>3.0</td>
      <td>0.88</td>
      <td>이길동</td>
      <td>970205</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>6.0</td>
      <td>0.99</td>
      <td>박길동</td>
      <td>930905</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>강길동</td>
      <td>960413</td>
    </tr>
    <tr>
      <th>5</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>차길동</td>
      <td>970321</td>
    </tr>
  </tbody>
</table>
</div>



### 칼럼 명이 같으나 기준 열이 아닌 경우

<br>

칼러명이 같으나 키가 되면 안되는 칼럼이 존재한다면 ON 인수로 기준을 명시한다.
<br>



```python
df['추가정보'] = [300,400,500,600,700]
df2['추가정보'] = ['27살','28살','25살','29살','26살','25살']
```


```python
# pd.merge(df,df2) 오류 발생

pd.merge(df,df2, on='이름')
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
      <th>코드</th>
      <th>int</th>
      <th>float</th>
      <th>이름</th>
      <th>추가정보_x</th>
      <th>생년월일</th>
      <th>추가정보_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>4</td>
      <td>0.66</td>
      <td>홍길동</td>
      <td>300</td>
      <td>950303</td>
      <td>27살</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>5</td>
      <td>0.77</td>
      <td>윤길동</td>
      <td>400</td>
      <td>941215</td>
      <td>28살</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>3</td>
      <td>0.88</td>
      <td>이길동</td>
      <td>500</td>
      <td>970205</td>
      <td>25살</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>6</td>
      <td>0.99</td>
      <td>박길동</td>
      <td>600</td>
      <td>930905</td>
      <td>29살</td>
    </tr>
  </tbody>
</table>
</div>



on 으로 기준키를 지정해주지 않는다면 오류가 발생한다.<br>
이름이 같은 칼럼은 구분을 위해 뒤에 _x,_y 가 추가 된다.
<br>

### 기준 열이나 칼럼명이 다를 경우

기준 열이나 칼럼명이 다를 경우엔 칼럼명을 변경하거나 left_on , right_on 인수를 작성해주면 된다.



```python
df = df.rename(columns={'이름':'name'})
```


```python
pd.merge(df,df2, left_on='name', right_on='이름')
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
      <th>코드</th>
      <th>int</th>
      <th>float</th>
      <th>name</th>
      <th>추가정보_x</th>
      <th>이름</th>
      <th>생년월일</th>
      <th>추가정보_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A</td>
      <td>4</td>
      <td>0.66</td>
      <td>홍길동</td>
      <td>300</td>
      <td>홍길동</td>
      <td>950303</td>
      <td>27살</td>
    </tr>
    <tr>
      <th>1</th>
      <td>B</td>
      <td>5</td>
      <td>0.77</td>
      <td>윤길동</td>
      <td>400</td>
      <td>윤길동</td>
      <td>941215</td>
      <td>28살</td>
    </tr>
    <tr>
      <th>2</th>
      <td>C</td>
      <td>3</td>
      <td>0.88</td>
      <td>이길동</td>
      <td>500</td>
      <td>이길동</td>
      <td>970205</td>
      <td>25살</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>6</td>
      <td>0.99</td>
      <td>박길동</td>
      <td>600</td>
      <td>박길동</td>
      <td>930905</td>
      <td>29살</td>
    </tr>
  </tbody>
</table>
</div>



## join 함수
<br>
merge 함수가 아닌 join 함수로 비슷한 기능을 수행할 수 있다.

<br> 차이점은 join 함수의 경우 left join 을 default로 가지고 있으며 **인덱스**를 키 값으로 두 데이터 프레임을 결합한다.




```python
# 데이터 초기화함

df.set_index('이름',inplace=True)
df2.set_index('이름', inplace=True)
```

inplace=True 를 통해 새로운 데이터 프레임에 입력하는 것이 아닌 해당 데이터 프레임을 바로 변환하는 방법을 이용할 수 있다.


```python
df.join(df2)
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
      <th>코드</th>
      <th>int</th>
      <th>float</th>
      <th>생년월일</th>
    </tr>
    <tr>
      <th>이름</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>홍길동</th>
      <td>A</td>
      <td>4</td>
      <td>0.66</td>
      <td>950303.0</td>
    </tr>
    <tr>
      <th>윤길동</th>
      <td>B</td>
      <td>5</td>
      <td>0.77</td>
      <td>941215.0</td>
    </tr>
    <tr>
      <th>이길동</th>
      <td>C</td>
      <td>3</td>
      <td>0.88</td>
      <td>970205.0</td>
    </tr>
    <tr>
      <th>박길동</th>
      <td>D</td>
      <td>6</td>
      <td>0.99</td>
      <td>930905.0</td>
    </tr>
    <tr>
      <th>김길동</th>
      <td>E</td>
      <td>9</td>
      <td>1.11</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



## concat 함수

concat 함수 기준 열을 사용하지 않고 물리적으로 데이터프레임을 이어 붙이는 기능을 한다.

<br>

우선 데이터 셋을 만들고 실습해보자.


```python
df3 = pd.DataFrame([['a1','a2','a3'],
                   ['b1','b2','b3'],
                   ['c1','c2','c3']],
                   columns=['A','B','C'],
                   index = [1,2,3])

df4 = pd.DataFrame([['a1','a2','a3'],
                   ['b1','b2','b3'],
                   ['d1','d2','d3']],
                   columns=['A','B','D'],
                   index = [2,3,4])
```

concat 은 default 값으로 axis=0 이 설정되어 있음으로 함수 사용시 x축을 기준으로 데이터가 결합된다.


```python
result1 = pd.concat([df3,df4])
result1
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>a1</td>
      <td>a2</td>
      <td>a3</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b1</td>
      <td>b2</td>
      <td>b3</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>c1</td>
      <td>c2</td>
      <td>c3</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a1</td>
      <td>a2</td>
      <td>NaN</td>
      <td>a3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b1</td>
      <td>b2</td>
      <td>NaN</td>
      <td>b3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>d1</td>
      <td>d2</td>
      <td>NaN</td>
      <td>d3</td>
    </tr>
  </tbody>
</table>
</div>



outer가 default 이기 때문에 비어있는 데이터에선 NaN 을 출력한다.


```python
result2 = pd.concat([df3,df4], axis=1)
result2
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>A</th>
      <th>B</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>a1</td>
      <td>a2</td>
      <td>a3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b1</td>
      <td>b2</td>
      <td>b3</td>
      <td>a1</td>
      <td>a2</td>
      <td>a3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>c1</td>
      <td>c2</td>
      <td>c3</td>
      <td>b1</td>
      <td>b2</td>
      <td>b3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>d1</td>
      <td>d2</td>
      <td>d3</td>
    </tr>
  </tbody>
</table>
</div>



axis를 1로 설정함으로서 y축을 기준으로 데이터를 결합할 수 있다.


```python
result3 = pd.concat([df3,df4], axis=1,join='inner')
result3
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>A</th>
      <th>B</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>b1</td>
      <td>b2</td>
      <td>b3</td>
      <td>a1</td>
      <td>a2</td>
      <td>a3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>c1</td>
      <td>c2</td>
      <td>c3</td>
      <td>b1</td>
      <td>b2</td>
      <td>b3</td>
    </tr>
  </tbody>
</table>
</div>



join='inner' 를 설정함으로서 교집합맞 추출하는 inner방식의 결합이 가능하다.


```python
result4 = pd.concat([df3,df4],ignore_index=True)
result4
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a1</td>
      <td>a2</td>
      <td>a3</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b1</td>
      <td>b2</td>
      <td>b3</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c1</td>
      <td>c2</td>
      <td>c3</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>a1</td>
      <td>a2</td>
      <td>NaN</td>
      <td>a3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>b1</td>
      <td>b2</td>
      <td>NaN</td>
      <td>b3</td>
    </tr>
    <tr>
      <th>5</th>
      <td>d1</td>
      <td>d2</td>
      <td>NaN</td>
      <td>d3</td>
    </tr>
  </tbody>
</table>
</div>



ignore_index=True 을 이용해서 axis=0으로 결합시 중복되는 index를 결합과 동시에 재배열 할 수 있다.
