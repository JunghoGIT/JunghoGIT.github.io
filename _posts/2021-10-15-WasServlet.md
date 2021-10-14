---
title:  "WAS와 Servlet 기초"
excerpt: "배경지식 학습"
categories:
 - TIL
tags:
 - [web,server,study,TIL,java]
last_modified_at: 2021-10-15
toc: true
toc_sticky: true
---

# WAS&Servlet
<br>


## 1. WAS

<br>

### 1-1 동적?? 정적 ?? WAS의 탄생 이유 !
<br>


서버는 클라이언트에게 요청을 받는다.

이 때 클라이언트에게 받는 요청은 크게 동적 요청, 정적 요청 두가지로 나눌 수 있다.

서버는 요청을 받은 후에 해당 요청을 정적으로 처리할지 동적으로 처리할지 판단한다.

![PPT1](\assets\images\WAS슬라이드.jpg)

정적인 요청을 예로 들면 지금 포스팅 하고 있는 깃헙 블로그라고 할 수 있다.

웹 브라우저에서 포스팅을 요청 하게 되면 서버는 깃헙 래파지토리에서 이미 완성된 파일로서 존재하는 정적인 markdown 파일을 HTML형식으로 웹브라우저에 보내게 된다.

이렇듯 서버는 그저 클라이언트에게서 URI을 통해 정확히 뭘 요청하는지 파악하고 요청한 파일이 서버내에 존재한다면 Response 해주고 없다면 404에러를 보내는 것이다.



웹이 개발된 초기에는 이러한 정적인 요청이 대부분이었지만 웹이 크게 성장하면서 동적인 요청을 필요로 하게 됐다.



동적인 요청의 예는 클라이언트가 서버에게 여성회원의 정보를 요청했다고 치자.

문제는 member_girl.html 같은 정적인 파일로서 존재하지 않는다는 것이다.

이때 서버는 파일이 없다고 404error.html을 Response하는 것이 아니라 클라이언트의 요청을 HTML코드로 출력하여 Response하게 된다.
<br>


### 1-2 WAS란?!

<br>

`WAS(Web Application Server)`는 클라이언트가 동적으로 처리해야하는 서비스를 요청 했을 때 서비스를 *동적인 페이지를 가공하여 서비스를 제공 하는 것* 을 도와 주는 *'환경'* 이다.

WAS는 독립적으로 데이터나 요청을 처리하는 것이 아닌 서버와 서블릿 컨테이너가 소통하고 상호작용 할 수 있도록 도와주는 환경이다.



대표적인 예로 아파치 톰캣이 있다.

<br>

<hr>

## Servlet

<br>

### 2-1 Servlet = API

<br>

Servlet은 자바에서 제공하는 API이다.

API에 대한 정리가 필요하다.



`API(Application Programming Interface)`는 응용 프로그램에서 사용할 수 있도록, 운영 체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스를 뜻한다. 주로 파일 제어, 창 제어, 화상 처리, 문자 제어 등을 위한 인터페이스를 제공한다.



정확한 이해가 어렵지만 대부분 레스토랑 점원에 비유하곤 한다.

손님(프로그램)이 점원(API)에게 음식을 주문하면 점원은 우리가 주문한 음식을 가져다준다.

`Servlet`은 자바라는 레스토랑에서 일하고 있는 점원이라고 생각하면 된다.



API을 사용할 때 장점은 점원이 나에게 음식을 갖다주기 위해 어떻게 하는지 알 필요가 없다는 것이다.

그저 레스토랑 룰에 맞춰서 주문만 하면 내가 주문한 음식을 가져다준다.

즉 어떠한 방식으로 코드가 작성 되어 있는지 몰라도 우린 그저그냥 원하는 것만 얻어내면 되는 것이다.
<br>


### 2-2  Container in WAS
<br>


`WAS`는 정말 여러 정보를 찾아봤지만 확실히 뭐라고 정의 내리기엔 정보의 차이가 조금씩 있어 어려웠다.

그래도 정리해보자면 WAS는 웹서버와 서블릿 컨테이너의 기능을 내제하며 둘의 기능을 서포트해주는 환경이라는 거다. 

> 간혹 웹서버를 WAS에서 분리 시켜서 설명하는 사람도 있고 웹서버와 서블릿 컨테이너를 포함한다고 설명하는 글도 있어서 확실하게 정의 내리지 못했다. 이부분은 추후 시간이 될 때 더 공부할 예정...



`서블릿 컨테이너`는 간단하게 말해서 Servlet을 **실행하고 관리해주는 역할** 을 한다.

이름 뜻 그대로 Servlet에 관한 여러 기능들을 가지고 있다.



WAS는 웹서버로 받은 클라이언트의 요청을 서블릿 컨테이너로 보내게 된다.

<br>

### 2-3 what is Servlet ?
<br>

`Servlet`은 자바에서 제공하는 API중 하나이며, 클라이언트에게 요청 받은 서비스를 동적으로 처리하여 서비스하는 데에 목적이 있다.

주된 기능은 클라이언트에게 받은 요청을 동적으로 HTML코드로 작성하여 서비스 하는 것이다.



Servlet에는 **생명주기** 라는 것이 있다.

종류와 순서는 다음과 같다.



| 종류                       | 메소드 실행 시점                  | 기능과 특징                      |
| -------------------------- | --------------------------------- | -------------------------------- |
| init()                     | 최초 서블릿에 요청이 도착 했을 때 | 초기화 작업이며 한번만 가능하다. |
| service(),doGET(),doPost() | 요청이 올 때마다 실행             | 실제 기능을 수행한다.횟수제한x   |
| destroy()                  | 서버중지or웹어플리케이션 중지     | 자원을 해제한다.                 |

서블릿의 기본적인 구조는 다음과 같다.

```java
import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class FirstServlet extends HttpServlet{

	@Override
	public void init()  {
		System.out.println("init");
	}
	
	@Override
	protected void service(HttpServletRequest request, HttpServletResponse response){
		System.out.println("service");
	}


}

```



기본적으로 Servlet은 'HttpServlet' 클래스를 상속 받는 구조이다.

그리고 HttpServlet 는 'GenericServlet'을 상속 받는다.

API의 장점이 어떤 구조인지 몰라도 되는 것인 만큼 자세한 건 모르는 체로 넘어가자.


<br>


### 2-4 Servlet의 동작 과정

<br>

![서블릿](\assets\images\Servlet과정.jpg)



서블릿 과정은 위에 그림과 같다.

<OL>
    <li>클라이언트가 서버로 요청을 보낸다</li>
    <li>서버에서 동적처리여부 판단 후 서블릿컨테이너로 요청URI전송</li>
    <li>URL과 web.xml을 참조하여 담당 Servblet 확인</li>
    <li>최초 여부 판단 후 최초라면 객체 생성 (init) 아니라면 servlet에 매개변수 전달</li>
    <li>요청을 받은 후 DB에 접근 하여 데이터 확보</li>
    <li>받은 java코드를 HTML로 작성 동적페이지 생성</li>
    <li>역순으로 클라이언트까지 전송 후 객체삭제</li>
</ol>

