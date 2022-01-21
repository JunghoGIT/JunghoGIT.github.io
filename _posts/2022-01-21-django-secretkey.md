---
title:  "django secret key 숨기기"
excerpt: "secret key를 secret 하게 "
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2022-01-21
toc: true
toc_sticky: true
published: true
---

# django secret key 숨기기

<br>

장고 프로젝트중 버전관리를 위해 커밋을 했을 때 깃헙으로부터 secret key가 노출되었다는 경고 메시지를 받아본 경험이 있을거다.

<br>


secret key는 암호화 서명, 세션, 패스워드 리셋 등등 다양한 기능에서 쓰인다.

secret key가 없다면 장고 프로젝트는 실행되지 않는다.

<br>


해당 키 코드만 봐도 이리저리 암호화되어 있는 것을 보면 중요한 정보고 private 해야 된다는 게 느껴진다.

<br>


secret key 를 숨기는 방법은 크게 2가지이다.

- 환경변수에 secret key 추가.
- 비밀 파일로 secret key 저장

<br>


본 글에서는 비밀 파일로 관리하는 방법에 대해서만 알아보겠다.

<br>


## secrets.json

<br>


secret key 정보를 가지고 있는 json 파일을 만들어보자.

<br>


```json
{
	"SECRET_KEY": "settings.py에 있는 secret key"
}
```

<br>


## settings.py

<br>


이제 settings.py 에서 장고 프로젝트가 시작 될 때 secrets.json 파일로부터 secret key를 가져오도록 코드를 구성해보자.

<br>


```python
# settings.py

import os, json
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent


secret_file = os.path.join(BASE_DIR, 'secrets.json')  # secrets.json 파일 위치를 명시

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting):
    """비밀 변수를 가져오거나 명시적 예외를 반환한다."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret("SECRET_KEY")

```


<br>



## gitignore


<br>



이제 gitignore 안에 해당 secrets.json 을 명시해줌으로서 git 파일관리에서 제외되도록 설정해주자.



```markdown
secrets.json
```

<br>

