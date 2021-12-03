---
title:  "dash로 dashboard 만들기"
excerpt: "dashboard 만들기"
categories:
 - Python
tags:
 - [python,study,TIL,data,pandas,dash]
last_modified_at: 2021-12-03
toc: true
toc_sticky: true
---

# python 가상 환경 virtualenv 

# dash로 dashboard 만들기 



## dash란 ?



python의 강력한 라이브러리 중 하나인 dash를 이용하여 dashboard를 만들어보자.

dash는 프레임워크 flask를 를 기반으로 코드 몇줄 만으로 dashboard 앱을 만들 수 있는 라이브러리이다.

dash 안에는 많은 라이브러리 패키지 들을 포함하고 있으며 그렇기에 다른 라이브러리에 비해 무거운 편이다.



*dash 공식  가이드 : https://dash.plotly.com/*



## 사전 준비



### 가상환경 설치



가상환경을 통해 적절한 환경을 구성하여 작업을 해보자.

[내가 쓴 글 ](https://junghogit.github.io/python/python_virtualenv/) 에 가상환경에 대한 부분을 정리해놨으니 참고하자.



### 라이브러리 설치



```shell
pip install dash
pip install pandas
pip install numpy
pip install gunicorn
```



해당 프로젝트의 메인이 되는 dash 와 데이터 작업을 도와줄 pandas, numpy 배포를 위한 gunicorn 을 설치해준다.



### 데이터 및 디렉토리 준비



```shell
C:.
│ .gitignore
│  app.py
│
│
├─assets        
│
└─data
        Bitcoin.csv
        Ethereum.csv
```



프로젝트 파일의 구성은 다음 과 같다.



- app.py : main 실행 파일
- data : 사용할 데이터 파일을 저장
- assets : css 파일과 favicon 등을 저장
- gitignore : 배포를 할 때에 제외 될 파일을 명시



데이터는 [인베스팅닷컴](https://kr.investing.com/) 에서 2020/10/29~2021/11/29 까지의 비트코인과 이더리움의 가격, 거래량 정보 데이터를 수집해왔다.



## 코드 작성





### import



```python
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go

```



- dash_core_components : 대화형 사용자 인터페이를 만들기 위한 python 추상화를 제공한다. 그래프, 드롭다운, 체크박스 등 interactive elements 를 만드는 데 사용한다.
- dash_html_components : html 의 기본 구성을 만들 수 있는 라이브러리이다.



### 데이터 불러오기 및 전처리



```python
data = pd.read_csv('data\Bitcoin.csv')
data['coinname'] = 'BTC'
data2 = pd.read_csv('data\Ethereum.csv')
data2['coinname'] = 'ETH'

data=data.append(data2)


data['날짜'] = data['날짜'].str.replace(pat=r'[^A-Za-z0-9]', repl=r'-', regex=True)
data['거래량'] = data['거래량'].str.replace(pat=r'[^0-9]', repl=r'', regex=True)
data['날짜'] = pd.to_datetime(data['날짜'], format="%Y--%m--%d-")

data=data.sort_values(by=['coinname','날짜'])

data=data.reset_index(drop=True)
```



저장한 데이터 파일을 pandas를 통해 저장하고 필요한 전처리를 해준다.

기존에 데이터의 날짜가 한글로 년 월 일 형태로 저장되어 있어서 datetime 형으로 변경해줬다.

후에 ETH와 BTC 데이터프레임을 합치면서 중복된 index를 재설정했다.



### dash 객체 생성



```python
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "JH's first dashboard"
server = app.server
```



app 이란 이름의 dash 클래스 객체 인스턴스를 만들어준다.

external_stylesheets 은 외부의 css 를 가져오는 역할을 하는데 선택 사항이다.

app.title 은 외부에서 보는 웹사이트의 제목을 설정한다.

server = app.server 배포를 위한 서버 정보를 저장한다.



### html 코드 작성



```python
app.layout = html.Div(

    children=[

        html.Div(children=[
            html.H1(children="Bitcoin & Ethereum",style={"fontSize": "50px", "text-align": "center","padding-top" :"50px"}, className='header_title' ),
            html.P(
                children="1일 가격과 거래량",style={"fontSize": "30px", "text-align": "center"},className='header_description'
            )
        ],className='header')
        
```



app.layout 에 html 라이브러리를 통해 html 코드를 작성하여 기본적인 layout을 설정해줄 수 있다.



위의 코드는 html로 표현하면 다음과 같다.



```html
<div class='header'>
    <h1 class="header_title" style="fontsize:50px~~~~~">
        Bitcoin & Ethereum
    </h1>
     <p class="header_description" style="fontsize:50px~~~~~">
        1일 가격과 거래량
    </p>
</div>
```



### 그래프 코드 작성





```python
fig1 = go.Figure(data=[go.Candlestick(
    x=data['날짜'],
    open=data['오픈'], high=data['고가'],
    low=data['저가'], close=data['종가'],
    increasing_line_color= 'red', decreasing_line_color= 'blue'
)]) #app.layout = html.Div() 안에서 작성한 코드 아님
"""
app.layout = html.Div(

    children=[

        html.Div(children=[
            html.H1(children="Bitcoin & Ethereum",style={"fontSize": "50px", "text-align": "center","padding-top" :"50px"}, className='header_title' ),
            html.P(
                children="1일 가격과 거래량",style={"fontSize": "30px", "text-align": "center"},className='header_description'
            )
        ],className='header')
"""

			html.Div(
           		 children=[
            	    dcc.Graph(id="candlestick-chart", figure=fig1),
               		 dcc.Graph(id="chart",
                          figure={
                              "data": [
                                  {
                                      "x": data["날짜"],
                                      "y": data["거래량"],
                                      "type": "lines",
                                  },
                              ],
                              "layout": {"title": "거래량 선 그래프"},
                          },
                          )
            ],className="chart"
        ),
    )
    



```

app.layout = html.Div( ) 안에 계속해서 그래프 코드를 작성해준다. 

완성한 이후 단계별 설명을 하다보니 코드가 조금 복잡하게 편집된 점 이해 부탁드린다.. 흑..

dcc.graph 를 통해 figure 객체에 그래프에 대한 정보를 넘겨준다.

plotly나 matplotlib 에서 하는 것과 크게 다르지 않다.

여기서 figure를 설정하는 방식은 여러가지가 있는데 추후에 기회가 되면 다른 포스팅으로 설명해보겠다.

우선 본인은 figure 객체 미리 만들어서 넘겨주는 방법과 바로 초기화 해주는 방법 두 가지를 사용해서 만들어봤다.



### localhost 테스트 배포



```python
if __name__ == "__main__":
    app.run_server(debug=True)

```



위의 코드를 추가하여 localhost에 배포해보자.

debug=True 를 통해 서버를 재시동 하는 일 없이 새로고침 만으로 변경 사항을 적용시킬 수 있다.



```shell
C:.
│  .gitignore
│  app.py
│
├─.idea
│  │  .gitignore
│  │  .name
│  │  dashboard_project.iml
│  │  misc.xml
│  │  modules.xml
│  │  vcs.xml
│  │  workspace.xml
│  │
│  └─inspectionProfiles
│          profiles_settings.xml
│
├─assets
│
└─data
        Bitcoin.csv
        Ethereum.csv

```



디렉토리의 상태는 다음과 같다.



브라우저에서 http://127.0.0.1:8050/ 주소를 통해 결과물을 확인 할 수 있다



### style.css 작성



위의 코드에서 작성한 html 태그의 클래스 명을 이용해 인터페이스를 좀 더 아름답게 꾸며보자



```css
.header{
background-color: #4D4D4D;
margin-bottom : 100px;
}

.header_title {
    color: #FFFFFF;
    font-size: 52px;
    font-weight: bold;
    text-align: center;
    margin-top : 0px;
}

.header_description {
    color: #CFCFCF;
    margin: 4px auto;
    text-align: center;
    max-width: 384px;
}

```



assets 폴더에 style.css 파일을 만들어서 css코드로 클래스에 해당하는 부분을 꾸며줄 수 있다.



### interactive programming



코인 데이터의 날짜를 선택하여 해당 날짜의 차트만 본다거나 btc와 eth 두 데이터의 종류를 사용자가 마음대로 편하게 골라 볼 수 있게 만들어보자.



우선 날짜를 선택할 수 있는 메뉴와 코인의 종류를 선택할 수 있는 메뉴를 만들어보자.



설명하고 있는 부분의 코드만 따로 불러온다. 시각적 불편함 주의



```python
app.layout = html.Div(

    children=[

        html.Div(children=[
            html.H1(children="Bitcoin & Ethereum",style={"fontSize": "50px", "text-align": "center","padding-top" :"50px"}, className='header_title' ),
            html.P(
                children="1일 가격과 거래량",style={"fontSize": "30px", "text-align": "center"},className='header_description'
            )
        ],className='header'
        ),# 이하로 메뉴 생성 코드
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(
                            children="Date Range",
                            className="menu-title"
                        ),
                        dcc.DatePickerRange(
                            id="date-range",
                            min_date_allowed=data.날짜.min().date(),
                            max_date_allowed=data.날짜.max().date(),
                            initial_visible_month=data.날짜.min().date(),
                            start_date=data.날짜.min().date(),
                            end_date=data.날짜.max().date(),
                        ),
                    ],className="menu_date"
                ),
                html.Div(
                    children=[
                        html.Div(children="BTC or ETH", className="menu-title"),
                        dcc.Dropdown(
                            id="coin-name",
                            options=[
                                {"label": "BTC", "value": "BTC"},
                                {"label": "ETH", "value": "ETH"}
                            ],
                            value="BTC",
                            clearable=False,

                        ),
                    ],className="menu_coin",
                ),
            ],
            className="menu",
        ),
```



dcc 라이브러리를 통해 원하는 메뉴를 만들어준다.

여기서 제일 중요한 점은 value 와 id 이다.

하단에 작성할 callback 부분에서 id 를 통해 해당 id 의 value 를 가져와서 동적으로 다시 만들어주는 역할을 한다.

html 에서 form 을 받는 것과 거의 동일한 원리라고 보면 된다.



### callback



Callback 함수란, 개발자는 이벤트를 등록하기만 할 뿐, 실제 사이트 방문자가 특정 이벤트를 발생시키면, 특정 시점에 도달했을 때 해당 기능을 활성화 시키는 것이다.



```python
@app.callback(
    [dash.dependencies.Output("candlestick-chart", "figure"), dash.dependencies.Output("chart", "figure")],
    [
        dash.dependencies.Input("coin-name", "value"),
        dash.dependencies.Input("date-range", "start_date"),
        dash.dependencies.Input("date-range", "end_date"),
    ],
)

def update_charts(coin_name, start_date, end_date):
    mask = (
            (data.날짜 >= start_date) & (data.날짜 <= end_date) & (data.coinname == coin_name)
    )
    filtered_data = data.loc[mask, :]

    fig1 = go.Figure(data=[go.Candlestick(
        x=filtered_data['날짜'],
        open=filtered_data['오픈'], high=filtered_data['고가'],
        low=filtered_data['저가'], close=filtered_data['종가'],
        increasing_line_color='red', decreasing_line_color='blue'
    )])

    candlestick_chart_figure = fig1
    fig1.update_layout(title={'text' : "1일 가격 차트",
                              'y':0.9,
                              'x':0.5,
                              'xanchor': 'center',
                              'yanchor': 'top'},
                       xaxis_title="날짜",
                       yaxis_title="가격",
                       height = 700,
                       paper_bgcolor = '#4D4D4D',
                       font_color= "#FFFFFF",
                       plot_bgcolor= '#525252')


    chart_figure = {
        "data": [
            {
                "x": filtered_data["날짜"],
                "y": filtered_data["거래량"],
                "type": "lines",
            },
        ],
        "layout": {"title": {"text" :"거래량 선 그래프"},
                   "xaxis":{"title":"날짜"},
                   "yaxis":{"title":"거래량"},
                   "height" : "300",
                   "paper_bgcolor": "#4D4D4D",
                   "font": {"color":"#FFFFFF"},
                   "plot_bgcolor": "#525252",
                   }
    }

    return candlestick_chart_figure, chart_figure

```



각 id 이름으로 연결이 돼서 값을 가져온다.

해당 값을 인자로 update_charts 함수에서 필터링된 데이터를 만들고 figure 객체를 반환하여 다시 그래프를 생성한다.



배포는 다른 글에서 다뤄보겠다.



완성된 코드는 [깃헙](https://github.com/JunghoGIT/project/blob/main/dashboard_project/app.py) 에서 확인 가능하다.