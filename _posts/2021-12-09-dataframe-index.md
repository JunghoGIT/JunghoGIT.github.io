---
title:  "Pandas Dataframe index"
excerpt: "dataframe의 index를 학습해보자."
categories:
 - Pandas
tags:
 - [pandas,python,study,TIL,data]
last_modified_at: 2021-12-09
toc: true
toc_sticky: true
---

# 데이터 프레임 인덱스


## 인덱스 설정과 제거

데이터 프레임에서 인덱스는 성능과도 관련이 있는 요소이므로 상황에 맞게 설계하며 조작할 수 있어야 한다.

우선 데이터셋을 만들고 다양한 조작법을 알아보자.


```python
import pandas as pd
import numpy as np

list1 = ['A','B','C','D','E']
list2 = [4,5,3,6,9]
list3 = [0.66,0.77,0.88,0.99,1.11]
list4 = ['홍길동','윤길동','이길동','박길동','김길동',]

df = pd.DataFrame({'칼럼1':list1, '칼럼2':list2,'칼럼3': list3 ,'칼럼4':list4})


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
      <th>칼럼1</th>
      <th>칼럼2</th>
      <th>칼럼3</th>
      <th>칼럼4</th>
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



### set_index()

<br>

set_index() 함수를 통해 기존의 행 인덱스를 제거하고 특정 칼럼을 인덱스로 변경할 수 있다.


```python
df2=df.set_index('칼럼1')

```


```python
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
      <th>칼럼2</th>
      <th>칼럼3</th>
      <th>칼럼4</th>
    </tr>
    <tr>
      <th>칼럼1</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>4</td>
      <td>0.66</td>
      <td>홍길동</td>
    </tr>
    <tr>
      <th>B</th>
      <td>5</td>
      <td>0.77</td>
      <td>윤길동</td>
    </tr>
    <tr>
      <th>C</th>
      <td>3</td>
      <td>0.88</td>
      <td>이길동</td>
    </tr>
    <tr>
      <th>D</th>
      <td>6</td>
      <td>0.99</td>
      <td>박길동</td>
    </tr>
    <tr>
      <th>E</th>
      <td>9</td>
      <td>1.11</td>
      <td>김길동</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.index
```




    Index(['A', 'B', 'C', 'D', 'E'], dtype='object', name='칼럼1')




```python
df2.loc['A':'D']
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
      <th>칼럼2</th>
      <th>칼럼3</th>
      <th>칼럼4</th>
    </tr>
    <tr>
      <th>칼럼1</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>4</td>
      <td>0.66</td>
      <td>홍길동</td>
    </tr>
    <tr>
      <th>B</th>
      <td>5</td>
      <td>0.77</td>
      <td>윤길동</td>
    </tr>
    <tr>
      <th>C</th>
      <td>3</td>
      <td>0.88</td>
      <td>이길동</td>
    </tr>
    <tr>
      <th>D</th>
      <td>6</td>
      <td>0.99</td>
      <td>박길동</td>
    </tr>
  </tbody>
</table>
</div>



set_index() 를 통해 기존의 0,1,2,3,4 로 이루어진 행 인덱스는 삭제하고 칼럼1이 인덱스로 바뀌었다.<br>
index name은 기존의 칼럼명을 따라가게 된다.<br>
기존 인덱스가 사라졌으므로 loc로 데이터를 인덱싱할 때에도 바뀐 칼럼 A의 값으로 데이터로 인덱싱 해야 한다.


<br>

### reset_index()

reset_index() 함수를 통해 기존의 인덱스를 제거 혹은 칼럼화 시키고, 행을 기준으로 0 부터 시작하는 일반적인 정수형 인덱스를 추가할 수 있다.




```python
df2.reset_index()
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
      <th>칼럼1</th>
      <th>칼럼2</th>
      <th>칼럼3</th>
      <th>칼럼4</th>
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



만약 drop=Ture 값을 준다면 기존 인덱스 였던 열은 칼럼으로 돌아가는 것이 아니라 삭제 된다.


```python
df2.reset_index(drop=True)
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
      <th>칼럼2</th>
      <th>칼럼3</th>
      <th>칼럼4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
      <td>0.66</td>
      <td>홍길동</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>0.77</td>
      <td>윤길동</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>0.88</td>
      <td>이길동</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6</td>
      <td>0.99</td>
      <td>박길동</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9</td>
      <td>1.11</td>
      <td>김길동</td>
    </tr>
  </tbody>
</table>
</div>



<br>

## 다중 인덱스

<br>

행이나 열에 여러 계층을 가지는 다중 인덱스를 설정 할 수 있다. 

### 생성

<br>


```python
df3 = pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], columns=[['A','A','B','B'],['칼럼1','칼럼2','칼럼3','칼럼4']])


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

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="2" halign="left">A</th>
      <th colspan="2" halign="left">B</th>
    </tr>
    <tr>
      <th></th>
      <th>칼럼1</th>
      <th>칼럼2</th>
      <th>칼럼3</th>
      <th>칼럼4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>13</td>
      <td>14</td>
      <td>15</td>
      <td>16</td>
    </tr>
  </tbody>
</table>
</div>



columns = 에 다중 리스트 형태로 인덱스를 넣어주면 된다.<br>

<br>

### 인덱스 이름 추가


```python
df3.columns.names= ['이름1','이름2']
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

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>이름1</th>
      <th colspan="2" halign="left">A</th>
      <th colspan="2" halign="left">B</th>
    </tr>
    <tr>
      <th>이름2</th>
      <th>칼럼1</th>
      <th>칼럼2</th>
      <th>칼럼3</th>
      <th>칼럼4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>13</td>
      <td>14</td>
      <td>15</td>
      <td>16</td>
    </tr>
  </tbody>
</table>
</div>



마찬가지로 칼럼 인덱스 뿐만 아니라 행 인덱스도 다중으로 생성하고 이름을 설정할 수 있다.


```python
df4 = pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],
                   columns=[['A','A','B','B'],['칼럼1','칼럼2','칼럼3','칼럼4']],
                   index=[[1,1,2,2],['하나','둘','셋','넷']])

df4.columns.names = ['이름1','이름2']
df4.index.names = ['인덱스1', '인덱스2']
df4
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>이름1</th>
      <th colspan="2" halign="left">A</th>
      <th colspan="2" halign="left">B</th>
    </tr>
    <tr>
      <th></th>
      <th>이름2</th>
      <th>칼럼1</th>
      <th>칼럼2</th>
      <th>칼럼3</th>
      <th>칼럼4</th>
    </tr>
    <tr>
      <th>인덱스1</th>
      <th>인덱스2</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">1</th>
      <th>하나</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>둘</th>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2</th>
      <th>셋</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
      <td>12</td>
    </tr>
    <tr>
      <th>넷</th>
      <td>13</td>
      <td>14</td>
      <td>15</td>
      <td>16</td>
    </tr>
  </tbody>
</table>
</div>



## 다중 인덱스 인덱싱

<br>

인덱스가 다중으로 있는 경우 인덱스 값을 튜플의 형태로 입력하여야 한다.


```python
df4.loc[(1,'하나'),('A','칼럼2')]
```




    2




```python
df4[('A','칼럼2')]=100

df4
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>이름1</th>
      <th colspan="2" halign="left">A</th>
      <th colspan="2" halign="left">B</th>
    </tr>
    <tr>
      <th></th>
      <th>이름2</th>
      <th>칼럼1</th>
      <th>칼럼2</th>
      <th>칼럼3</th>
      <th>칼럼4</th>
    </tr>
    <tr>
      <th>인덱스1</th>
      <th>인덱스2</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">1</th>
      <th>하나</th>
      <td>1</td>
      <td>100</td>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th>둘</th>
      <td>5</td>
      <td>100</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2</th>
      <th>셋</th>
      <td>9</td>
      <td>100</td>
      <td>11</td>
      <td>12</td>
    </tr>
    <tr>
      <th>넷</th>
      <td>13</td>
      <td>100</td>
      <td>15</td>
      <td>16</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4.A
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
      <th>이름2</th>
      <th>칼럼1</th>
      <th>칼럼2</th>
    </tr>
    <tr>
      <th>인덱스1</th>
      <th>인덱스2</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">1</th>
      <th>하나</th>
      <td>1</td>
      <td>100</td>
    </tr>
    <tr>
      <th>둘</th>
      <td>5</td>
      <td>100</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2</th>
      <th>셋</th>
      <td>9</td>
      <td>100</td>
    </tr>
    <tr>
      <th>넷</th>
      <td>13</td>
      <td>100</td>
    </tr>
  </tbody>
</table>
</div>




```python
df4.loc[1]['A']
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
      <th>이름2</th>
      <th>칼럼1</th>
      <th>칼럼2</th>
    </tr>
    <tr>
      <th>인덱스2</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>하나</th>
      <td>1</td>
      <td>100</td>
    </tr>
    <tr>
      <th>둘</th>
      <td>5</td>
      <td>100</td>
    </tr>
  </tbody>
</table>
</div>



주의할 점은 iloc 함수에서는 튜플 형태로 다중 인덱싱을 사용할 수 없다.
