---
title:  "django model validator"
excerpt: "model에서의 유효성 검사 설정"
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2022-02-04
toc: true
toc_sticky: true
published: true
---

# django model에서 validator 커스텀

<br>

장고에서 모델 객체에 대한 유효성 검사는 보통 view에서 이루어진다.

<br>

유효성 검사를 위한 기준은 기본 모델 필드 속성 마다 정의되어 있으나 form과 model에서 별도로 개발자의 입맛에 맞게 추가적인 설정이 가능하다.

<br>

이번 글에선 model에서 validator를 재정의 하는 법을 알아보자.

<br>

## 장고 model field class

<br>

우선 장고 깃헙에서 모델 필드 클래스가 정의 된 부분을 확인해보자.

<br>

model field class github : [https://github.com/JunghoGIT/django/blob/main/django/db/models/fields/__init__.py](https://github.com/JunghoGIT/django/blob/main/django/db/models/fields/__init__.py)

<br>

```python
  @cached_property
    def validators(self):
        """
        Some validators can't be created at field initialization time.
        This method provides a way to delay their creation until required.
        """
        return [*self.default_validators, *self._validators]

    def run_validators(self, value):
        if value in self.empty_values:
            return

        errors = []
        for v in self.validators:
            try:
                v(value)
            except exceptions.ValidationError as e:
                if hasattr(e, 'code') and e.code in self.error_messages:
                    e.message = self.error_messages[e.code]
                errors.extend(e.error_list)

        if errors:
            raise exceptions.ValidationError(errors)

    def validate(self, value, model_instance):
        """
        Validate value and raise ValidationError if necessary. Subclasses
        should override this to provide validation logic.
        """
        if not self.editable:
            # Skip validation for non-editable fields.
            return

        if self.choices is not None and value not in self.empty_values:
            for option_key, option_value in self.choices:
                if isinstance(option_value, (list, tuple)):
                    # This is an optgroup, so look inside the group for
                    # options.
                    for optgroup_key, optgroup_value in option_value:
                        if value == optgroup_key:
                            return
                elif value == option_key:
                    return
            raise exceptions.ValidationError(
                self.error_messages['invalid_choice'],
                code='invalid_choice',
                params={'value': value},
            )

        if value is None and not self.null:
            raise exceptions.ValidationError(self.error_messages['null'], code='null')

        if not self.blank and value in self.empty_values:
            raise exceptions.ValidationError(self.error_messages['blank'], code='blank')

    def clean(self, value, model_instance):
        """
        Convert the value's type and run validation. Validation errors
        from to_python() and validate() are propagated. Return the correct
        value if no error is raised.
        """
        value = self.to_python(value)
        self.validate(value, model_instance)
        self.run_validators(value)
        return value
```

<br>



유효성 검사와 관련된 부분만 가져와봤다.

<br>

## validation 만들기

<br>

```python
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse


class Note(models.Model):
    def validate_title(value):
        if "바보" in value:
            raise ValidationError("바보는 나쁜말")
        else:
            return value

    title = models.TextField(max_length=20, validators=validate_title)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

```

<br>

- 모델 클래스 안 혹은 models.py 안에 value 를 인자로 받아 조건을 확인하는 함수를 선언
- 해당 함수를 적용하길 원하는 필드에 `validators` 속성에 추가
  - 만약 여러가지 validator를 추가 하고 싶다면  `validators=[validators1,validators2]` 처럼 리스트 형식으로도 가능하다.