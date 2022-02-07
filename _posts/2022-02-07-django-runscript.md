---
title:  "django 스크립트 파일 실행하기"
excerpt: "장고 디자인패턴에 포함되지 않은 스크립트 파일 실행"
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2022-02-07
toc: true
toc_sticky: true
published: true
---



# django 외부에서 작성된 스크립트 파일 사용하기 

<br>

장고는 개발자에게 정말 대부분의 기능을 제공한다.

<br>

하지만 개발자가 '장고'만으로 서비스를 개발할 때 다른 python 스크립트 파일이 필요할 때가 있다.

<br>

예를 들면 스크래핑한 데이터를 주기적으로 DB에 입력한다던가, 데이터의 특정 조건에 대하여 주기적으로 검사해야 될 경우 등, 장고의 기능만으론 효율적으로 개발 할 수 없을 때가 있다.

<br>

본인의 경우 원래 환율 정보를 클라이언트에서 ajax로 받아왔었는데 개발 단계에선 괜찮지만 배포 후에는 api 최대 호출 제한에 걸릴 게 분명해 보였다.

<br>

그렇다면 서버에서 호출 제한에 걸리지 않게 인터벌을 설정하여 주기적으로 데이터를 받아오고, 해당 데이터에 대한 api를 만들면 되지 않을까 란 생각을 했다.

<br>

암튼 알아보자 !

<br>

## django.setup()

<br>

핵심은 django.setup() 기능을 사용하는 것이다.

<br>

우선 서버와 함께 동작하길 바라는 스크립트 파일을 manage.py 와 같은 경로상에 저장하자.

<br>

```python
import requests
import json
import time, os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "config.settings")
django.setup()

from app.models import modelname

```

<br>

위처럼 `os.environ.setdefault('DJANGO_SETTINGS_MODULE', "config.settings")` 를 이용하여 환경 변수를 설정해주자.

현재 manage.py 에서 참조하는 settings.py 의 경로까지 포함하여 설정해주면 된다.

<br>

`django.setup()` 을 호출한 후 장고 모델이나 그 외 코드를 참조하여 사용할 수 있다.

<br>

주의할 점은 절대절대 django.setup() 후에 django 의 코드를 사용해야 한다는 것이다.

<br>

## 실행 방법


<br>


실행 방법에 대해선 여러가지 시도를 해봤으나 인터프리터 언어의 특성 탓인지 runserver 명령어와 동시에 자동으로 실행되도록 하는 것엔 실패했다.

<br>

가장 best는 runserver 명령어를 한 터미널 외에 다른 터미널에서 python [스크립트파일.py] 명령어로 해당 파일을 실행 시키는 방법이었다.

<br>

배포 단계에서는 백그라운드로 실행하는 방법이 있다.
백그라운드로 실행하는 방법은 OS마다 차이가 있다.

<br>


linux의 경우

```bash
nohup python filename.py &

```

명령어를 통해 백그라운드 실행이 가능하다.

<br>

혹시라도 더 좋은 방법이 존재한다면 댓글로 알려주시면 감사드리겠습니다. 

