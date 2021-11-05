
---
title:  "Plotly 기본 사용 연습"
excerpt: "Kaggle 자료로 공부"
categories:
 - 시각화
tags:
 - [DATA,study,TIL,plotly]
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


<html>
<head><meta charset="utf-8" /></head>
<body>
    <div>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG"></script><script type="text/javascript">if (window.MathJax) {MathJax.Hub.Config({SVG: {font: "STIX-Web"}});}</script>
                <script type="text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>    
            <div id="4edb1a0e-1e0f-40de-be15-8097b9e4c245" class="plotly-graph-div" style="height:525px; width:100%;"></div>
            <script type="text/javascript">

                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("4edb1a0e-1e0f-40de-be15-8097b9e4c245")) {
                    Plotly.newPlot(
                        '4edb1a0e-1e0f-40de-be15-8097b9e4c245',
                        [{"marker": {"color": "#496595", "size": 10}, "mode": "markers", "name": "Man", "type": "scatter", "x": [1950, 521, 114, 1886, 79, 57, 323], "y": ["Bachelor\u2019s degree", "Doctoral degree", "I prefer not to answer", "Master\u2019s degree", "No formal education past high school", "Professional doctorate", "Some college/university study without earning a bachelor\u2019s degree"]}, {"marker": {"color": "#f36196", "size": 10}, "mode": "markers", "name": "Woman", "type": "scatter", "x": [412, 134, 29, 470, 12, 15, 60], "y": ["Bachelor\u2019s degree", "Doctoral degree", "I prefer not to answer", "Master\u2019s degree", "No formal education past high school", "Professional doctorate", "Some college/university study without earning a bachelor\u2019s degree"]}],
                        {"template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "#E5ECF6", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "white", "linecolor": "white", "minorgridcolor": "white", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "pie": [{"automargin": true, "type": "pie"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "#E5ECF6", "showlakes": true, "showland": true, "subunitcolor": "white"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "#E5ECF6", "polar": {"angularaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "radialaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "yaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}, "zaxis": {"backgroundcolor": "#E5ECF6", "gridcolor": "white", "gridwidth": 2, "linecolor": "white", "showbackground": true, "ticks": "", "zerolinecolor": "white"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "baxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}, "bgcolor": "#E5ECF6", "caxis": {"gridcolor": "white", "linecolor": "white", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "white", "linecolor": "white", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "white", "zerolinewidth": 2}}}, "xaxis": {"anchor": "y", "domain": [0.0, 1.0]}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0]}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('4edb1a0e-1e0f-40de-be15-8097b9e4c245');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
   {% raw %}
 x.observe(notebookContainer, {childList: true});
 {% endraw %}
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };

            </script>
        </div>
</body>
</html>



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


<html>
<head><meta charset="utf-8" /></head>
<body>
    <div>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_SVG"></script><script type="text/javascript">if (window.MathJax) {MathJax.Hub.Config({SVG: {font: "STIX-Web"}});}</script>
                <script type="text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>    
            <div id="dcc4f7cb-b324-461d-a675-8f3cebcc2a59" class="plotly-graph-div" style="height:350px; width:100%;"></div>
            <script type="text/javascript">

                    window.PLOTLYENV=window.PLOTLYENV || {};

                if (document.getElementById("dcc4f7cb-b324-461d-a675-8f3cebcc2a59")) {
                    Plotly.newPlot(
                        'dcc4f7cb-b324-461d-a675-8f3cebcc2a59',
                        [{"marker": {"color": "#496595", "size": 10}, "mode": "markers", "name": "Man", "type": "scatter", "x": [1950, 521, 114, 1886, 79, 57, 323], "y": ["Bachelor\u2019s degree", "Doctoral degree", "I prefer not to answer", "Master\u2019s degree", "No formal education past high school", "Professional doctorate", "Some college/university study without earning a bachelor\u2019s degree"]}, {"marker": {"color": "#f36196", "size": 10}, "mode": "markers", "name": "Woman", "type": "scatter", "x": [412, 134, 29, 470, 12, 15, 60], "y": ["Bachelor\u2019s degree", "Doctoral degree", "I prefer not to answer", "Master\u2019s degree", "No formal education past high school", "Professional doctorate", "Some college/university study without earning a bachelor\u2019s degree"]}],
                        {"font": {"color": "#8a8d93"}, "height": 350, "hoverlabel": {"bgcolor": "#f2f2f2", "font": {"family": "Lato, sans-serif", "size": 13}}, "legend": {"orientation": "h", "x": 0.5, "xanchor": "center", "y": 1, "yanchor": "bottom"}, "margin": {"b": 0, "l": 20, "r": 20}, "shapes": [{"line": {"color": "#c6ccd8", "width": 2}, "type": "line", "x0": 1950, "x1": 412, "y0": 0, "y1": 0}, {"line": {"color": "#c6ccd8", "width": 2}, "type": "line", "x0": 521, "x1": 134, "y0": 1, "y1": 1}, {"line": {"color": "#c6ccd8", "width": 2}, "type": "line", "x0": 114, "x1": 29, "y0": 2, "y1": 2}, {"line": {"color": "#c6ccd8", "width": 2}, "type": "line", "x0": 1886, "x1": 470, "y0": 3, "y1": 3}, {"line": {"color": "#c6ccd8", "width": 2}, "type": "line", "x0": 79, "x1": 12, "y0": 4, "y1": 4}, {"line": {"color": "#c6ccd8", "width": 2}, "type": "line", "x0": 57, "x1": 15, "y0": 5, "y1": 5}, {"line": {"color": "#c6ccd8", "width": 2}, "type": "line", "x0": 323, "x1": 60, "y0": 6, "y1": 6}], "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "white", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "white", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "#C8D4E3", "linecolor": "#C8D4E3", "minorgridcolor": "#C8D4E3", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "#C8D4E3", "linecolor": "#C8D4E3", "minorgridcolor": "#C8D4E3", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "pie": [{"automargin": true, "type": "pie"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "white", "showlakes": true, "showland": true, "subunitcolor": "#C8D4E3"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "white", "polar": {"angularaxis": {"gridcolor": "#EBF0F8", "linecolor": "#EBF0F8", "ticks": ""}, "bgcolor": "white", "radialaxis": {"gridcolor": "#EBF0F8", "linecolor": "#EBF0F8", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "white", "gridcolor": "#DFE8F3", "gridwidth": 2, "linecolor": "#EBF0F8", "showbackground": true, "ticks": "", "zerolinecolor": "#EBF0F8"}, "yaxis": {"backgroundcolor": "white", "gridcolor": "#DFE8F3", "gridwidth": 2, "linecolor": "#EBF0F8", "showbackground": true, "ticks": "", "zerolinecolor": "#EBF0F8"}, "zaxis": {"backgroundcolor": "white", "gridcolor": "#DFE8F3", "gridwidth": 2, "linecolor": "#EBF0F8", "showbackground": true, "ticks": "", "zerolinecolor": "#EBF0F8"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "#DFE8F3", "linecolor": "#A2B1C6", "ticks": ""}, "baxis": {"gridcolor": "#DFE8F3", "linecolor": "#A2B1C6", "ticks": ""}, "bgcolor": "white", "caxis": {"gridcolor": "#DFE8F3", "linecolor": "#A2B1C6", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "#EBF0F8", "linecolor": "#EBF0F8", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "#EBF0F8", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "#EBF0F8", "linecolor": "#EBF0F8", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "#EBF0F8", "zerolinewidth": 2}}}, "title": {"font": {"color": "#444", "family": "Lato, sans-serif", "size": 25}, "text": "Highest Level of Education: Gender"}, "xaxis": {"anchor": "y", "domain": [0.0, 1.0], "showgrid": false}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "tickmode": "array", "ticktext": ["Without Bachelor's Degree", "Professional doctorate", "No formal education past high school", "Master\u2019s degree", "I prefer not to answer", "Doctoral degree", "Bachelor\u2019s degree"], "tickvals": ["Some college/university study without earning a bachelor\u2019s degree", "Professional doctorate", "No formal education past high school", "Master\u2019s degree", "I prefer not to answer", "Doctoral degree", "Bachelor\u2019s degree"]}},
                        {"responsive": true}
                    ).then(function(){

var gd = document.getElementById('dcc4f7cb-b324-461d-a675-8f3cebcc2a59');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
  {% raw %}
    x.observe(notebookContainer, {childList: true});
    {% endraw %}
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })
                };

            </script>
        </div>
</body>
</html>

