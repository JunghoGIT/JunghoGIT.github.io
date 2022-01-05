---
title:  "virtualenv로 python 가상환경 만들기"
excerpt: "virtualenv 기본 사용법"
categories:
 - Python
tags:
 - [python,study,TIL,data]
last_modified_at: 2021-12-02
toc: true
toc_sticky: true
---

# python 가상 환경 virtualenv 



프로그래밍을 할 때 OS, 언어, 프레임워크, 라이브러리, 패키지 등의 다양한 요소들이 합쳐서 완성된 결과물을 만든다.

문제는 이 다양한 요소들의 어떤 상황에서든 호환되는 것이 아니다.

예를 들어 최상위 버전의 python을 사용할 때에 특정 라이브러리가 호환이 안 되는 경우가 그러하다.

그렇다면 어떻게 해야할까 ?

프로젝트를 진행할 때 마다 데스트톱의 모든 환경을 다시 재설치하고 설정값을 변경해야할까 ?

너무 번거롭고 위험성이 높은 방법이다.



이럴 때 **가상 환경** 이라는 기능을 사용하면 내가 원하는 프로젝트 래파지토리에 별도의 환경을 설치함으로서 해당 프로젝트만을 위한 개발 공간을 만들 수 있다.



실제 프로그래밍부터 배포 전의 테스트 까지 가상환경에서 한다면 안정적인 프로그래밍이 가능하다.



가상 환경은 anaconda, virtualenv 등 다양한 방법이 있지만 이번 글에선 virtualenv를 이용해 가상환경을 만들고 관리해보겠다.



## virtualenv 



### 설치 



우선 virtualenv 를 설치하기 전에 pip이 올바른 버전으로 설치되어 있어야 한다.



```shell
c:>pip install virtualenv
```



### 가상환경 생성



```shell
c:>virtualenv venv
```



위 명령어로 뒤에 설정한 venv 라는 이름의 가상환경을 만들 수 있다.

해당 이름으로 물리적인 가상환경 디렉토리가 생성된다.



```shell
virtualenv venv -p python3.9

```



위의 -p \<python 버전> 형식으로 설치할 파이썬의 버전을 지정할 수 있다.



### 가상환경 진입



```shell
c:> cd venv
c:\venv> cd Scripts
c:\venv\Scripts> activate

(venv) c:\venv\Scripts>
```



우선 가상환경이 설치된 디렉토리로 가서 그 안에 Scirpts 디렉토리로 이동하게 되면 폴더 안에 activate.bat 이라는 파일이 있다.

이 파일을 실행해줌으로서 가상환경에 접근이 가능하다.

성공적으로 가상환경에 진입하면 파일경로 앞에 (가상환경이름) 이 붙게 된다.

만약 오류 메시지가 안 나오는데 가상환경으로 진입이 안 된다면 파일 경로에 한글이 있는지와 관리자모드로 cmd 를 실행했는지 확인해보자.





### 가상환경 사용



```shell
(venv) c:\venv\Scripts> pip install pandas

```



이제 가상환경 내에서 pip 명령어를 통해 필요한 패키지를 설치 할 수 있다.



### 가상환경 종료



```shell
(venv) c:\venv\Scripts> deactivate
c:\venv\Scripts>

```



deactivate 명령어로 손 쉽게 가상환경을 종료할 수 있다. 

진입할 때와 마찬가지로 파일경로 앞에 괄호를 통해 가상환경 여부를 확인한다.



