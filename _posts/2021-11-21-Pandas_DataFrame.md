---
title:  "Pandas DataFrame 1"
excerpt: "DataFrame의 기본 사용법"
categories:
 - Pandas
tags:
 - [pandas,python,study,TIL,Data]
last_modified_at: 2021-11-21
toc: true
toc_sticky: true
---

# Data Frame (Pandas)

pandas의 Dataframe 구조는 Index-Column-Value 의 형태로 이루어진 데이터 구조로서, 비즈니스에서 가장 많이 사용되어지는 기본적인 데이터 구조이다.<br>
DateFrame을 사용함으로서 Series 구조보다 시각적으로나 기능적으로 훨씬 개선된 방식으로 데이터를 관리할 수 있다.<br>
다른 시스템과 연동이 쉬우며, 데이터 전처리에서 강력한 모습을 보여준다.<br>
## DataFrame 생성


### 기본 생성



```python
import pandas as pd

df1 = pd.DataFrame([10,20,30,40,50])
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
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
    </tr>
    <tr>
      <th>2</th>
      <td>30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>40</td>
    </tr>
    <tr>
      <th>4</th>
      <td>50</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2= pd.DataFrame([[10,20,30,40,50],['A','B','C','D','F']])
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10</td>
      <td>20</td>
      <td>30</td>
      <td>40</td>
      <td>50</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A</td>
      <td>B</td>
      <td>C</td>
      <td>D</td>
      <td>F</td>
    </tr>
  </tbody>
</table>
</div>



DataFrame() 함수를 통해 데이터 프레임 객체를 만들 수 있다.<br>
매개 값으로 단일 리스트를 주어지게 된다면 열로 들어가게 되고, 이중 리스트의 경우 각 리스트 하나 하나가 행으로서 입력 된다.
 



### column 과 index를 포함한 생성


```python
df3= pd.DataFrame([['윤정호','1995-03-03','수원','동국대',5000],
                   ['홍길동','1997-07-07','서울','서울대',4000],
                   ['스미스','1999-09-09','뉴욕','하버드',2000],
                   ['나카무라','1990-04-04','도쿄','동경대',3000]],
                  columns=['이름','생년월일','거주지','학교','재산(만)'],
                  index=['1번','2번','3번','4번'])
df3
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
      <th>거주지</th>
      <th>학교</th>
      <th>재산(만)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1번</th>
      <td>윤정호</td>
      <td>1995-03-03</td>
      <td>수원</td>
      <td>동국대</td>
      <td>5000</td>
    </tr>
    <tr>
      <th>2번</th>
      <td>홍길동</td>
      <td>1997-07-07</td>
      <td>서울</td>
      <td>서울대</td>
      <td>4000</td>
    </tr>
    <tr>
      <th>3번</th>
      <td>스미스</td>
      <td>1999-09-09</td>
      <td>뉴욕</td>
      <td>하버드</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>4번</th>
      <td>나카무라</td>
      <td>1990-04-04</td>
      <td>도쿄</td>
      <td>동경대</td>
      <td>3000</td>
    </tr>
  </tbody>
</table>
</div>



series 구조와 dataframe 사이에서 가장 확연하게 드러나는 차이는 Column의 유무이다.<br>
dataframe 함수 안에 columns=[] 형태로 칼럼명을 설정해줄 수 있다.<br>
만약 따로 설정해주지 않는다면 기본 값은 0부터 차례대로 정수가 들어가게 된다.
<br>

## 데이터 정보 확인


```python
df3.shape
```




    (4, 5)



.shape 를 통해 행(데이터)의 개수와 열(칼럼)의 개수를 알 수 있다.
<br> (행,열) 순으로 출력된다.



```python
df3.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Index: 4 entries, 1번 to 4번
    Data columns (total 5 columns):
     #   Column  Non-Null Count  Dtype 
    ---  ------  --------------  ----- 
     0   이름      4 non-null      object
     1   생년월일    4 non-null      object
     2   거주지     4 non-null      object
     3   학교      4 non-null      object
     4   재산(만)   4 non-null      int64 
    dtypes: int64(1), object(4)
    memory usage: 352.0+ bytes
    

.info() 함수를 통해 데이터의 타입과 데이터의 개수등 다양한 정보를 얻을 수 있다.<br>
해당 정보들을 통해 데이터의 문제점을 파악할 수 있다.


```python
df3.describe()
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
      <th>재산(만)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>3500.000000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1290.994449</td>
    </tr>
    <tr>
      <th>min</th>
      <td>2000.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2750.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>3500.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>4250.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>5000.000000</td>
    </tr>
  </tbody>
</table>
</div>



.describe() 함수를 통해 숫자로 이루어진 데이터(연속형 데이터)들에 한하여 다섯수치요약(five number summary)을 가져 올 수 있다. <br>
해당 정보를 이용해 데이터의 문제점을 파악 가능하다.<br>
<br>
ex)비정상적으로 높은 최댓값, 50% 와 평균값의 큰 차이


```python
df3.isnull()
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
      <th>거주지</th>
      <th>학교</th>
      <th>재산(만)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1번</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2번</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3번</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4번</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



isnull을 통해 데이터의 결측치 (Missing Data)의 존재 여부를 확인 할 수 있다. <br>
True 일 경우 결측치가 존재한다는 것을 의미한다.


```python
df3.isnull().sum()
```




    이름       0
    생년월일     0
    거주지      0
    학교       0
    재산(만)    0
    dtype: int64



isnull에 sum을 을 같이 사용하여 한 눈에 결측치의 존재 여부와 양을 알 수 있다.

## 기본적인 데이터 추출과 연산


```python
df3.head()
df3.tail()
```

.head()와 .tail() 을 통해 각각 상위 5개 하위 5개 데이터를 확인 할 수 있다.


```python
df3['이름']

```




    1번     윤정호
    2번     홍길동
    3번     스미스
    4번    나카무라
    Name: 이름, dtype: object



dataframe에서 칼럼명을 기준으로 데이터를 탐색할 수 있다.<br>
데이터 타입은 칼럼(열)을 기준으로 각각의 타입을 갖게 된다.<br>
위의 코드처럼 하나의 대괄호 안에 칼럼명을 입력하면 series형태로 데이터를 출력해준다.<br>


```python
df3[['이름']]
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1번</th>
      <td>윤정호</td>
    </tr>
    <tr>
      <th>2번</th>
      <td>홍길동</td>
    </tr>
    <tr>
      <th>3번</th>
      <td>스미스</td>
    </tr>
    <tr>
      <th>4번</th>
      <td>나카무라</td>
    </tr>
  </tbody>
</table>
</div>



series 형태가 아닌 dataframe의 형태로 결과를 받아보고 싶다면 중첩된 대괄호를 이용하여 찾고 싶은 값을 입력해주면 된다.<br>



```python
#df3['이름','생년월일'] 오류 발생
df3[['이름','생년월일']]
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
      <th>1번</th>
      <td>윤정호</td>
      <td>1995-03-03</td>
    </tr>
    <tr>
      <th>2번</th>
      <td>홍길동</td>
      <td>1997-07-07</td>
    </tr>
    <tr>
      <th>3번</th>
      <td>스미스</td>
      <td>1999-09-09</td>
    </tr>
    <tr>
      <th>4번</th>
      <td>나카무라</td>
      <td>1990-04-04</td>
    </tr>
  </tbody>
</table>
</div>



2가지 이상의 복수의 칼럼을 가져오고 싶을 때는 series로는 표현할 수 없기 때문에 dataframe의 구조로만 가져올 수 있다. <br>
따라서 중첩된 대괄호의 형태로 값을 입력하여야 한다.



```python
print(df3['재산(만)'].sum())
print(df3['재산(만)'].mean())
```

    14000
    3500.0
    

series와 마찬가지로 여러 함수들을 이용해 연산을 할 수 있다.<br>

## 저장


Pandas는 파일 관리를 할 수 있는 여러 기능을 포함하고 있다.
데이터를 생성했으니 파일로서 저장해보자.


```python
df3.to_csv("Pandas_learn.csv")

#df.to_excel("test.xlsx") 엑셀 형태로 저장
#df.to_pickle("df.pkl") 피클 형태로 저장
"""
  SQLite3 DB로 저장하기

  con = sqlite3.connect("test.db")

  df.to_sql("table_name", con, if_exists="append", index=False)

  con.close()

  # 데이터프레임을 html표로 바꾸기

  df.to_html()



  # html 파일로 저장하기

  df.to_html("test.html")
"""


```




    '\n  SQLite3 DB로 저장하기\n\n  con = sqlite3.connect("test.db")\n\n  df.to_sql("table_name", con, if_exists="append", index=False)\n\n  con.close()\n\n  # 데이터프레임을 html표로 바꾸기\n\n  df.to_html()\n\n\n\n  # html 파일로 저장하기\n\n  df.to_html("test.html")\n'



파일 장소 지정은 파일명 앞에 저장할 위치를 지정해주면 된다.
