---
title: "Plotly 기본 사용 연습"
excerpt: "Kaggle 자료로 공부"
categories:
 - visualize
tags:
 - [data,study,TIL,plotly]
last_modified_at: 2021-11-06
toc: true
toc_sticky: true
---

**본 글은 kaggle 의 '2021 Kaggle Machine Learning & Data Science Survey' 시각화 대회의 데이터를 이용하였습니다.**
**KASHISH RASTOGI 님의 [2021 Kaggle Gender Survey Analysis](https://www.kaggle.com/kashishrastogi/2021-kaggle-gender-survey-analysis-plotly/notebook)를 토대로 코드를 분석 하며 공부하였습니다.**


## 사전 준비


```python
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import plotly.offline as offline
import plotly.graph_objs as go
offline.init_notebook_mode(connected = True)
import plotly.io as pio
pio.renderers.default = 'colab'
```


<script type="text/javascript">
window.PlotlyConfig = {MathJaxConfig: 'local'};
if (window.MathJax) {MathJax.Hub.Config({SVG: {font: "STIX-Web"}});}
if (typeof require !== 'undefined') {
require.undef("plotly");
requirejs.config({
    paths: {
        'plotly': ['https://cdn.plot.ly/plotly-latest.min']
    }
});
require(['plotly'], function(Plotly) {
    window._Plotly = Plotly;
});
}
</script>



## 데이터 파일 분류

우선 Pandas의 read-csv 함수를 통해 데이터를 df 객체로 로딩한다.<br>
질문 부분에 해당하는 0번 인덱스 데이터를 따로 qusetion 객체로 복사한다.<br>
그리고 응답에 해당하는 1번 인덱스 이후 모든 행을 df 객체로 초기화 시켜준다.<br>
iloc[] 뒤에 붙는 T는 'Transposed Data Frame' 란 의미로 행과 열을 바꾸는 기능을 한다.

low_memory 참고 : https://ahnty0122.tistory.com/99


```python
df = pd.read_csv('kaggle_survey_2021_responses.csv',low_memory=False)
# low_memory=False 는 여러 type의 데이터가 섞여 있을 때 나오는 오류를 방지해주는 기능
questions = df.iloc[0, :].T
df = df.iloc[1:, :]

```

## Highest Level of Education: Gender

## 데이터 정리


```python
df_q2_q4 = df[df['Q2']!='ETC'][['Q2','Q4']] # ETC로 제외할 필요 없음
#df_q2_q4 = df[0:][['Q2','Q4']]
df_q2_q4

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
      <th>Q2</th>
      <th>Q4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Man</td>
      <td>Bachelor’s degree</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Man</td>
      <td>Master’s degree</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Man</td>
      <td>Master’s degree</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Man</td>
      <td>Doctoral degree</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Man</td>
      <td>Doctoral degree</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>6157</th>
      <td>Man</td>
      <td>Master’s degree</td>
    </tr>
    <tr>
      <th>6158</th>
      <td>Man</td>
      <td>Bachelor’s degree</td>
    </tr>
    <tr>
      <th>6159</th>
      <td>Prefer not to say</td>
      <td>Master’s degree</td>
    </tr>
    <tr>
      <th>6160</th>
      <td>Woman</td>
      <td>Master’s degree</td>
    </tr>
    <tr>
      <th>6161</th>
      <td>Man</td>
      <td>Doctoral degree</td>
    </tr>
  </tbody>
</table>
<p>6161 rows × 2 columns</p>
</div>



위 코드를 통해 Q2의 성별에 대한 질문에 ETC라고 응답한 행을 제외한 데이터 프레임(df[df['Q2']!='ETC']) 중에서 Q2,Q4(학위에 대한 질문)열에 해당하는 데이터([['Q2','Q4']])를 추출하여 저장한다. 


```python
df_q2_q4 = pd.crosstab(df_q2_q4.Q2, df_q2_q4.Q4)
df_q2_q4
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
      <th>Q4</th>
      <th>Bachelor’s degree</th>
      <th>Doctoral degree</th>
      <th>I prefer not to answer</th>
      <th>Master’s degree</th>
      <th>No formal education past high school</th>
      <th>Professional doctorate</th>
      <th>Some college/university study without earning a bachelor’s degree</th>
    </tr>
    <tr>
      <th>Q2</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Man</th>
      <td>1950</td>
      <td>521</td>
      <td>114</td>
      <td>1886</td>
      <td>79</td>
      <td>57</td>
      <td>323</td>
    </tr>
    <tr>
      <th>Nonbinary</th>
      <td>11</td>
      <td>2</td>
      <td>0</td>
      <td>7</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Prefer not to say</th>
      <td>20</td>
      <td>11</td>
      <td>5</td>
      <td>21</td>
      <td>3</td>
      <td>2</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Prefer to self-describe</th>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Woman</th>
      <td>412</td>
      <td>134</td>
      <td>29</td>
      <td>470</td>
      <td>12</td>
      <td>15</td>
      <td>60</td>
    </tr>
  </tbody>
</table>
</div>



pd.crosstab(X,Y) 함수를 통해 X의 값이 행의 인덱스가 되고 Y의 값이 columm이 된다. 이를 통해 빈도수를 계산하여 dataFrame을 바꾸는 함수이다.<br>
참고 : https://3months.tistory.com/194


```python
df_q2_q4 = pd.crosstab(df_q2_q4.Q2, df_q2_q4.Q4).T.reset_index()
df_q2_q4
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
      <th>Q2</th>
      <th>Q4</th>
      <th>Man</th>
      <th>Nonbinary</th>
      <th>Prefer not to say</th>
      <th>Prefer to self-describe</th>
      <th>Woman</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bachelor’s degree</td>
      <td>1950</td>
      <td>11</td>
      <td>20</td>
      <td>5</td>
      <td>412</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Doctoral degree</td>
      <td>521</td>
      <td>2</td>
      <td>11</td>
      <td>0</td>
      <td>134</td>
    </tr>
    <tr>
      <th>2</th>
      <td>I prefer not to answer</td>
      <td>114</td>
      <td>0</td>
      <td>5</td>
      <td>0</td>
      <td>29</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Master’s degree</td>
      <td>1886</td>
      <td>7</td>
      <td>21</td>
      <td>2</td>
      <td>470</td>
    </tr>
    <tr>
      <th>4</th>
      <td>No formal education past high school</td>
      <td>79</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>12</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Professional doctorate</td>
      <td>57</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>15</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Some college/university study without earning ...</td>
      <td>323</td>
      <td>2</td>
      <td>5</td>
      <td>1</td>
      <td>60</td>
    </tr>
  </tbody>
</table>
</div>



Transposed Data Frame 을 통해 행과 열을 바꾸고 reset_index()로 인덱스 넘버를 추가한다.


```python
fig = make_subplots(specs=[[{"type": "scatter"}]])
fig.add_trace(go.Scatter(x=df_q2_q4['Man'], y=df_q2_q4['Q4'], mode = 'markers', name='Man',
                          marker=dict(color='#496595', size = 10),
             ))
fig.add_trace(go.Scatter(x=df_q2_q4['Woman'], y=df_q2_q4['Q4'], mode = 'markers', name='Woman',
                         marker=dict(color='#f36196', size = 10),
            ))
fig
```


![이미지1](\assets\images\plotly공부_1\1.JPG)


```python
from google.colab import drive
drive.mount('/content/drive')
```

figure 객체를 만들어준 후 빈 캔버스에 add_trace()함수를 통해 Scatter형식의 데이터 포인트를 입력해준다.<br>
mode = 'markers'점만 찍는 형식의 산점도 그래프를 의미한다.
그리고 makers의 설정은 딕셔너리 형태의 값으로 색상이나 사이즈를 입력한다.


```python
for i in range(0, len(df_q2_q4)):
    fig.add_shape(type='line',
                              x0 = df_q2_q4['Man'][i],
                              y0 = i,
                              x1 = df_q2_q4['Woman'][i],
                              y1 = i,
                              line=dict(color='#c6ccd8', width = 2))
```

add_shape()함수로 선을 추가해준다.
x0,y0 의 지점과 x1,y1의 지점을 잇는 선을 그어준다.


```python
fig.update_xaxes(showgrid=False)# 캔버스의 세로 격자 무늬를 지운다.
fig.update_yaxes(tickmode='array', 
                 tickvals=["Some college/university study without earning a bachelor’s degree",
                           "Professional doctorate",
                           "No formal education past high school",
                           "Master’s degree","I prefer not to answer","Doctoral degree",
                           "Bachelor’s degree"],
                 ticktext=["Without Bachelor's Degree","Professional doctorate",
                           "No formal education past high school",
                           "Master’s degree","I prefer not to answer","Doctoral degree",
                           "Bachelor’s degree"])# 기존에 너무 길었던 첫번째 항목의 제목을 바꾼다.
fig.update_layout(height=350, 
                  margin=dict(b=0,r=20,l=20), # 각각 bottom right left를 의미
                  title_text="Highest Level of Education: Gender",#제목
                  template="plotly_white",
                  title_font=dict(size=25, color='#444', family="Lato, sans-serif"), #폰트 설정
                  font=dict(color='#8a8d93'),
                  hoverlabel=dict(bgcolor="#f2f2f2", font_size=13, font_family="Lato, sans-serif"), # 그래프 위에 마우스를 올려놨을 때 나오는 hoverlabel설명 설정
                  legend=dict(orientation="h", yanchor="bottom", y=1, xanchor="center", x=0.5))
fig.show()
```


![이미지2](\assets\images\plotly공부_1\2.JPG)

