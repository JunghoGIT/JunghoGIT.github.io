---
title:  "WEB과 Server 기초"
excerpt: "기본지식 훈련"
categories:
 - Server
tags:
 - [web,server,study,TIL]
last_modified_at: 2021-10-15
toc: true
toc_sticky: true
---





<br>

# WEB and SERVER

<br>
<br>

## WEB

<br>
<br>

### what is web ?

<br>
<br>

>웹은 인터넷 상에서 동작하는 하나의 서비스이다.
>
>[출처:네이버지식백과](https://terms.naver.com/entry.naver?docId=4383203&cid=59941&categoryId=59941)



조금 더 자세히 표현하자면 웹은 인터넷 상에서 많은 문서들이 거미줄처럼 연결되어 *'정보'*를 주고 받을 수 있는 시각화 된*'서비스'*이다.



## 웹의 구성
<br>
<br>



웹의 구성은 해석,분류범위에 따라서 블로그 글로 정리할 수 없을만큼 방대하고 복잡하게 구성되어있다. 

그나마 최대한 간단히 나열한 구성 요소들을 이렇다.

<ul>

    - HTML<br>
    - URI(URL)<br>
    - WEB Browser<br>
    - WEB Server<br>
    - HTTP<br>
</ul>
<br>

### HTML
<br>
<br>

`HTML` 이란 웹을 구성하는 가장 기본적인 문서다.

HTML 은 고유의 규칙 하에 작성된 TEXT 코드로 구성되어있다.


![html예시](\assets\images\HTML예시.JPG)





위의 사진처럼 HTML은 정적이고 기능 자체에 다양한 웹을 만드는 것에 한계가 있기 때문에 다양한 언어가 포함되어 같이 쓰인다.

![프론트언어](\assets\images\프론트언어.jpeg){: width="270" height="270"}




<br>


`css` 는 HTML로 작성된 요소들을 시각적으로 꾸밀 수 있는 언어이다.

`javascript`는 정적인 HTML의 문제점을 해결하고 동적인 다양한 기능을 추가 할 수 있게 해준다.

<br>



### URI & URL , HTTP

<br>
<br>

![URI](\assets\images\URL.JPG)



`HTTP` 란 ??

>인터넷에서, 웹 서버와 사용자의 인터넷 브라우저 사이에 문서를 전송하기 위해 사용되는 통신 규약을 말한다.
>
>[출처:네이버지식백과](https://terms.naver.com/entry.naver?docId=1180001&cid=40942&categoryId=32851)



`URI` 는 자원의 위치 + 자원을 식별하는 식별자 까지 나타나 있는 인터넷 주소의 전체 부분에 해당한다고 볼 수 있다. 



 `URL` 은 요청하고자 하는 자원의 위치를 나타낸다. URI보다 작은 개념이라고 보면 된다.

<br>

### WEB Browser

<br>
<br>


`웹 브라우저`는 우리가 아는 일반적인 '익스플로어','크롬' 등의 브라우저이며 웹에 있어서 웹을 사용하는 주체이자 **'클라이언트'**라고 볼 수 있다.




### WEB Server

<br>
<br>


`웹 서버`는 우리가 원하는 정보를 갖고 있으며 해당 서비스를 '제공'하는 **서버**이다.



<br>

<hr>
<br>


## SERVER

<br>
<br>

### what is server?

<br>
<br>



`서버`란  하나의 컴퓨터이다. 실제로 우리가 사용하는 데스크톱의 컴퓨터 형태일 수도 있고 서버만의 목적으로 만들어진 특수한 형태의 컴퓨터일 수도 있다.



서버라는 말의 어원인 'serve'의 뜻은 '무언가를 제공하다'이다.

이렇듯 서버는 인터넷연결망으로 게임, 웹, 앱 등등 다양한 환경에서 원하는 정보와 '서비스'를 제공한다.



그러나 서버는 인공지능이 아니기에 요청 없이는 서비스를 제공해주지 않는다.

이때 **요청(Request)**하는 주체가 바로 **클라이언트** 이다.

그리고 이 요청을 받으면 **서버** 는 서비스를 **제공(Response)** 한다.



### Request & Response



웹을 예로 서버가 클라이언트에게 요청을 받고 그 요청에 대응 하는 대략적인 과정은 이렇다.

![ppt자료](\assets\images\슬라이드1.JPG)



대부분의 강의에서도 해당 부분을 설명할 때에 우리의 일상에 빗대어 설명한다.

만약 위의 과정을 식당에서 스테이크를 주문하는 과정에 비유하자면 이렇다.



식당에서 <span style="color : red">손님(클라이언트)</span>이 <span style="color : blue">웨이터(서버)</span>에게 <span style="color : green">스테이크(HTML)</span>을 정확하게 미디움굽기(URI)로 구워 달라고 요청(Request) 을 한다. 

그리고 요청(Request) 을 받은 웨이터(서버)는 <span style="color : orange">주방장(백엔드언어)</span>에게 미디움스테이크(구체적인HTML파일)을 달라고 하면 <span style="color : orange">주방장(백엔드언어)</span>은 <span style="color : pink">냉장고(데이터베이스)</span>로가서 재료를 꺼내어 미디움 스테이크를 만들고 서버에게 전달하여 최종적으로 <span style="color : blue">웨이터(서버)</span>는<span style="color : red"> 손님(클라이언트)</span>에게 <span style="color : green">스테이크</span>를 제공(Response)한다.



서버는 이렇게 서비스를 제공해주며 때로는 요청을 하기도 한다.

