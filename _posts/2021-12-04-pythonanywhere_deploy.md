---
title:  "pythonanywhere에서 dashboard 배포"
excerpt: "flask app 배포"
categories:
 - Python
tags:
 - [python,study,TIL,flask,dash]
last_modified_at: 2021-12-04
toc: true
toc_sticky: true
---


# pythonanywhere 에서 flask app 배포하기



이전 글에서 만든 [대시보드](https://junghogit.github.io/python/dash_dashboard_1/)를 localhost 가 아닌 실제 서버에 배포해보자.



우선 무료로 flask app을 무료로 배포할 수 있는 방법은 대표적으로 Heroku 와 pythonanywhere 을 이용하는 방법이 있다.



Heroku 를 통해 배포 하는 방법은 [https://dash.plotly.com/deployment](https://dash.plotly.com/deployment) 에서 확인할 수 있다.



본인은 처음에 heroku 를 통해 배포하려다가 약 12시간의 에러와 사투 끝에 패배를 인정하고 pythonanywhere를 통해 배포에 성공했다.



물론 후자의 방법에서도 4시간 이상 소요되었다. 

인생 첫 배포여서 우여곡절도 많았지만 그만큼 많은 걸 배워서 의미가 깊었다.

잡설은 여기까지 하고 본론으로 돌아가서 배포를 진행해보자.



## 사전 준비



### pythonanywhere 가입 & 로그인





우선 [https://www.pythonanywhere.com/](https://www.pythonanywhere.com/) 로 접속하여 간단한 회원 가입 후 로그인을 진행하면 된다.

회원가입은 Create a Beginner account 를 선택하여 한다.

회원 가입, 로그인을 위한 설명은 굳이 하지 않겠다.



### requirements.txt



pythonanywhere 서버에 가상환경을 설치해야 한다. 

그러기 위해서 작업한 프로젝트의 가상환경의 버전 정보를 가져와야 한다.

가상환경에 진입한 상태에서 

```shell
pip freeze > requirements.txt
```

를 사용하여 사용중인 모든 패키지 버전 정보가 담긴 파일을 만들어준다.







###  깃허브 준비





많은 방법이 있지만 git hub 를 통해 프로젝트를 clone 해오는 방식으로 pythonanywhere 서버에 업로드 하는 방법을 사용한다.

그러므로 우선 github에 해당 프로젝트 래파지토리를 만들어 push 가 되어있어야 한다.





## 파일 업로드



![1](\assets\images\pythonanywhere\1.JPG)





우선 pythonananywher(이하 '파애') 페이지에서 우측 상단의 콘솔 메뉴로 진입하고 bash 콘솔을 선택한다.



![2](\assets\images\pythonanywhere\2.JPG)



그리고 깃헙의 해당 래파지토리에서 https 주소를 복사한다.



이후에 bash에서 



```bash
$ git clone https://복사한 주소
```



를 입력해준다. 

![3](\assets\images\pythonanywhere\3.JPG)

성공적으로 복사가 완료 되었다면 파애의 우측 상단 files 메뉴에서 제대로 clone 되었는지 확인한다.



### 가상 환경 구축



```bash
06:43 ~ $ mkvirtualenv venv
~~
~~
~~
(venv) 06:45 ~ $ 
```



위의 명령어로 venv 라는 이름의 가상환경을 만들어준다.

위 가상 환경 이름은 자유롭게 지정해주면 된다.



```bash
(venv) 06:45 ~ $ cd project
```



위에서 클론한 프로젝트 디렉토리로 이동해준다.



```bash
(venv) 06:48 ~/project (main)$ pip install -r requirements.txt 
```



위 명령어로 기존에 만들었던 requirements.txt 를 읽어서 존재하는 모든 패키지를 가상환경에 설치해준다.





## web app 생성 및 설정





### 생성





가상환경의 패키지 까지 완료 되었다면 파애 사이트의 우측상단 메뉴에서 WEB 탭을 클락하여 

web app 을 만들어준다.



![4](\assets\images\pythonanywhere\4.JPG)

그리고 파이썬 버전과 프레임 워크 종류를 선택하면 되는데 당연히 flask를 선택하고 파이썬 버전은 가상환경에 설치된 파이썬 버전을 선택해야 한다.



![5](\assets\images\pythonanywhere\5.JPG)

이후에 path 를 설정하는 창이 나오는데 저 부분을 본인의 app.py가 존재하는 디렉토리 경로로 해서 설정해주면 된다.



### 설정



이후 생성이 끝나면 여러가지 설정 페이지가 나온다.



해당 페이지에서 우선 source code 부분의 경로를 수정하고 가상환경을 설정해준다.



![6](\assets\images\pythonanywhere\6.JPG)



그 이후에 코드 탭에 WSGI configuration file 을 클릭하여 안에 코드를 수정해주어야 한다.



![7](\assets\images\pythonanywhere\7.JPG)



prject_home 의 경로를 수정해주고 나머지 부분도 해당 코드와 동일하게 수정한다.







## app.py 코드 수정



왜인진 모르겠지만 메인 코드에서 pd.read_csv('상대경로') 로 하면 오류가 발생했다.

그래서 이 오류를 해결 하기 위해 경로를 깃헙의 절대경로를 이용해서 데이터를 가져오는 코드로 수정하였다.

![8](\assets\images\pythonanywhere\8.JPG)

깃헙의 raw 형식의 절대 경로를 얻고 싶다면,



깃헙에서 해당 csv 파일을 오픈하고 



![9](\assets\images\pythonanywhere\9.JPG)



Raw 메뉴를 클릭하여 나오는 페이지 주소를 사용하면 된다.





## 배포



![10](\assets\images\pythonanywhere\10.JPG)



위의 순으로 클릭하면 배포가 완료 된다.



## 발생 했던 에러



- csv 상대경로로 load 실패
  - github 의 절대경로로 수정하여 성공
- 패키지 설치 실패 
  - 가상환경에 패키지가 완전히 설치되지 않아 배포가 안됐음
  - 원인을 파악해보니 pythonanywhere에서 무료로 제공하는 데이터 공간이 500MB 밖에 안됐음
  - 보아하니 dash에 생각보다 많은 패키지가 포함되어 있었고 용량을 꽤 많이 차지함
  - dash에 포함된 패키지들을 검색하여 현 app에 필요 없어 보이는 라이브러리 모두 삭제
  - 그 외 불필요한 파일들 모두 삭제 후 성공
- WSGI 설정 오류
  - from app import app as application 부분을 from app import server as application 로 수정하여 해결
  - 구글링으로 해결 하였으나 정확한 코드 이해는 실패함 





## 결과



[http://yoonjungho.pythonanywhere.com/](http://yoonjungho.pythonanywhere.com/)



사실 dash와 flask 의 기본적인 tool을 사용해보기 위한 초미니 프로젝트였다보니 꾸미는 것엔 크게 노력 하지 않았다.



아마 이 프로젝트는 여기서 더 이상 수정하지 않고 다른 공부를 더 할 것 같다.



많이 허접해보이나 앞으로 개발자 인생에서 수 없이 많을 배포 중 첫 번째 배포라 생각하니 의미가 깊다.



첫 번째 배포 프로젝트 끝,