---
title:  "[Error] django debug toolbar 안 보이는 현상"
excerpt: "debug toolbar 에러?!"
categories:
 - Django
tags:
 - [Django,python,study,TIL,Error]
last_modified_at: 2021-12-27
toc: true
toc_sticky: true
---

# [Error] django-debug-toolbar 안 보이는 현상



## 에러 확인



낮에 노트북으로 프로젝트에 `django-debug-toolbar` 를 추가하여 활성화 된 것을 확인하고, 깃헙에 push 하고 귀가하였다.



그리고 집에 데스크톱으로 마저 작업하기 위해 pull을 하였는데 이게 웬걸 django-debug-toolbar가 활성화되지 않는 것이다.



아무리 코드를 확인하여도 설정상 문제는 없었고 애초에 노트북 환경에서 잘 되는 것을 확인하고 push 한 코드기 때문에 납득이 잘 안 가는 상황이었다.



코드를 다시 싹 다 갈아엎어보고 나름 공식문서와 스택 오버 플로우의 힘을 빌려 여러 코드도 추가해봤지만 노트북에서 봤던 디버그 툴바는 다시는 볼 수 없었다.



## 에러 발생 원인



그러던 와중 혹시나해서 크롬 개발자 모드로 HTML 코드를 검사해봤다.



그런데 HTML 코드에는 static 루트에서 debug_toolbar 를 잘 가져오고 있었다.



debug_toolbar 는 무조건 body 태그 안에 생성이 되기 때문에 body 태그를 보니 debug_toolbar div 의 class 명이 "djdt-hidden" 으로 되어있었다.



즉 성공적으로 불러왔지만 숨기기 옵션이 default 로 적용이 되어 있는 상태였다.





## 에러 해결



뭐 결국 에러 같지 않은 에러였지만 코드에는 문제가 없다는 것을 확인하고, 여러 시도 끝에 브라우저의 쿠키를 삭제하니 다시 제대로 적용 됐다.



아마도 노트북에서 숨기기 했던 정보가 구글 계정의 쿠키에 담겨져 온 것이 아닐까 하는 의심이든다.



암튼 숨기기 이후에 활성화가 안 될 경우엔 그냥 빠르고 편하게 쿠키를 지워버리자 ! 

 
끝 !