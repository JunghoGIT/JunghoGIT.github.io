---
title:  "Pandas eval"
excerpt: "eval 함수를 사용해보자."
categories:
 - Pandas
tags:
 - [pandas,python,study,TIL,data]
last_modified_at: 2021-12-08
toc: true
toc_sticky: true
---

# eval 함수를 이용한 data frame 연산

<br>

## eval 함수란 

<br>

eval 함수는 여러 프로그래밍 언어에 존재하는 함수이다. <br>
문자열을 입력 받아 그 문자열을 식으로 해석하여 결과를 반환하는 함수이다.

<br>

예를 들어 A= "2+2" 라는 문자열 변수가 있을 때 eval(A) 는 문자열 안의 식을 계산하여 4를 반환한다.

<br>

### 주의할 점

<br>

eval 함수의 주의할 점은 caller의 권한으로 수행하는 함수이기 때문에 치명적인 보안 위험이 존재한다. <br>
일반적인 프로그래밍에선 아예 사용하지 않는 것을 권고한다.
<br> 우스개 소리로 eval is evil 이라는 말도 있다. 


<br>

하지만 pandas 의 dataframe 연산에서는 꽤나 편한 기능을 제공하니 한번 사용해보자.

## dataframe 에서의 사용

우선 실습에 필요한 데이터를 만들어보자.



```python
import pandas as pd

list1 = [70,80,90,60]
list2 = [50,45,85,75]
list3 = [65,70,45,95]

df = pd.DataFrame({'국어': list1, '영어':list2 , '수학': list3})
df['이름'] = ['윤정호','아이유','슬기','윈터']
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
      <th>국어</th>
      <th>영어</th>
      <th>수학</th>
      <th>이름</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>70</td>
      <td>50</td>
      <td>65</td>
      <td>윤정호</td>
    </tr>
    <tr>
      <th>1</th>
      <td>80</td>
      <td>45</td>
      <td>70</td>
      <td>아이유</td>
    </tr>
    <tr>
      <th>2</th>
      <td>90</td>
      <td>85</td>
      <td>45</td>
      <td>슬기</td>
    </tr>
    <tr>
      <th>3</th>
      <td>60</td>
      <td>75</td>
      <td>95</td>
      <td>윈터</td>
    </tr>
  </tbody>
</table>
</div>



### 수치 연산

간단한 성적 데이터프레임을 만들어봤다.
<br>
우선 각 성적의 총점을 구해보자


```python
df.eval("국어+영어+수학")
```




    0    185
    1    195
    2    220
    3    230
    dtype: int64



결과를 통해 알 수 있듯이 eval 함수는 수치 연산시 series 형태로 결과를 반환한다.
<br> 그리고 이 결과는 바로 새로운 열로 추가 가능하다.

### 기존 데이터프레임 새로운 열에 결과 값 추가


```python
df.eval("총점=국어+영어+수학", inplace=True)
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
      <th>국어</th>
      <th>영어</th>
      <th>수학</th>
      <th>이름</th>
      <th>총점</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>70</td>
      <td>50</td>
      <td>65</td>
      <td>윤정호</td>
      <td>185</td>
    </tr>
    <tr>
      <th>1</th>
      <td>80</td>
      <td>45</td>
      <td>70</td>
      <td>아이유</td>
      <td>195</td>
    </tr>
    <tr>
      <th>2</th>
      <td>90</td>
      <td>85</td>
      <td>45</td>
      <td>슬기</td>
      <td>220</td>
    </tr>
    <tr>
      <th>3</th>
      <td>60</td>
      <td>75</td>
      <td>95</td>
      <td>윈터</td>
      <td>230</td>
    </tr>
  </tbody>
</table>
</div>




```python
import numpy as np

df.eval("평균 = 총점 / 3", inplace=True)
df['평균']= np.round(df['평균'].values,2)

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
      <th>국어</th>
      <th>영어</th>
      <th>수학</th>
      <th>이름</th>
      <th>총점</th>
      <th>평균</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>70</td>
      <td>50</td>
      <td>65</td>
      <td>윤정호</td>
      <td>185</td>
      <td>61.67</td>
    </tr>
    <tr>
      <th>1</th>
      <td>80</td>
      <td>45</td>
      <td>70</td>
      <td>아이유</td>
      <td>195</td>
      <td>65.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>90</td>
      <td>85</td>
      <td>45</td>
      <td>슬기</td>
      <td>220</td>
      <td>73.33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>60</td>
      <td>75</td>
      <td>95</td>
      <td>윈터</td>
      <td>230</td>
      <td>76.67</td>
    </tr>
  </tbody>
</table>
</div>





아주 간단하게 연산과 열 추가를 할 수 있다.<br>

inplace 는 값이 true 일 경우 원본 데이터를 변경하고 false 일 경우 적용된 결과 값만을 반환한다.

<br>

### 논리 연산

eval 함수를 통해 논리 연산도 가능하다.


```python
df.eval("평균>70")
```




    0    False
    1    False
    2     True
    3     True
    dtype: bool




논리 연산 수행시 boolean 의 값을 가지는 series 형태로 결과를 반환한다.

<br> 그리고 이 값을 이용해 loc[bool, 칼럼명] = '값' 형태의 함수를 사용해보자


```python
df.loc[df.eval("평균>=75 and 평균<80"),'등급'] = 'S'
df.loc[df.eval("평균>=70 and 평균<75"),'등급'] = 'A'
df.loc[df.eval("평균>=65 and 평균<70"),'등급'] = 'B'
df.loc[df.eval("평균>=60 and 평균<65"),'등급'] = 'C'

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
      <th>국어</th>
      <th>영어</th>
      <th>수학</th>
      <th>이름</th>
      <th>총점</th>
      <th>평균</th>
      <th>등급</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>70</td>
      <td>50</td>
      <td>65</td>
      <td>윤정호</td>
      <td>185</td>
      <td>61.67</td>
      <td>C</td>
    </tr>
    <tr>
      <th>1</th>
      <td>80</td>
      <td>45</td>
      <td>70</td>
      <td>아이유</td>
      <td>195</td>
      <td>65.00</td>
      <td>B</td>
    </tr>
    <tr>
      <th>2</th>
      <td>90</td>
      <td>85</td>
      <td>45</td>
      <td>슬기</td>
      <td>220</td>
      <td>73.33</td>
      <td>A</td>
    </tr>
    <tr>
      <th>3</th>
      <td>60</td>
      <td>75</td>
      <td>95</td>
      <td>윈터</td>
      <td>230</td>
      <td>76.67</td>
      <td>S</td>
    </tr>
  </tbody>
</table>
</div>



### 번외, rank 함수 사용하기

<br>
만들어진 데이터프레임에서 rank 함수를 사용해 등수 칼럼을 추가해보자.





```python
df['순위'] = df['평균'].rank(ascending=False)
df.sort_values(by=['순위']).reset_index(drop=True)

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
      <th>국어</th>
      <th>영어</th>
      <th>수학</th>
      <th>이름</th>
      <th>총점</th>
      <th>평균</th>
      <th>등급</th>
      <th>순위</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>60</td>
      <td>75</td>
      <td>95</td>
      <td>윈터</td>
      <td>230</td>
      <td>76.67</td>
      <td>S</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>90</td>
      <td>85</td>
      <td>45</td>
      <td>슬기</td>
      <td>220</td>
      <td>73.33</td>
      <td>A</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>80</td>
      <td>45</td>
      <td>70</td>
      <td>아이유</td>
      <td>195</td>
      <td>65.00</td>
      <td>B</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70</td>
      <td>50</td>
      <td>65</td>
      <td>윤정호</td>
      <td>185</td>
      <td>61.67</td>
      <td>C</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>



> 참조 [네이버블로그](https://m.blog.naver.com/PostView.naver?blogId=wideeyed&logNo=221874910289&targetKeyword=&targetRecommendationCode=1)
