---
title:  "django form validator"
excerpt: "form에서의 유효성 검사 설정"
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2022-02-02
toc: true
toc_sticky: true
published: true
---


# django form에서 validator 커스텀

<br>

장고에서 모델 객체에 대한 유효성 검사는 보통 view에서 이루어진다.

<br>

유효성 검사를 위한 기준은 기본 모델 필드 속성 마다 정의되어 있으나 form과 model에서 별도로 개발자의 입맛에 맞게 추가적인 설정이 가능하다.

<br>

이번 글에선 form에서 validator를 재정의 하는 법을 알아보자.

<br>

## 장고 form class


<br>


우선 장고 깃헙에서 form 클래스가 정의 된 부분을 확인해보자.

<br>

form class github : [https://github.com/JunghoGIT/django/blob/main/django/forms/forms.py](https://github.com/JunghoGIT/django/blob/main/django/forms/forms.py)

<br>

```python
 def full_clean(self):
        """
        Clean all of self.data and populate self._errors and self.cleaned_data.
        """
        self._errors = ErrorDict()
        if not self.is_bound:  # Stop further processing.
            return
        self.cleaned_data = {}
        # If the form is permitted to be empty, and none of the form data has
        # changed from the initial data, short circuit any validation.
        if self.empty_permitted and not self.has_changed():
            return

        self._clean_fields()
        self._clean_form()
        self._post_clean()

    def _clean_fields(self):
        for name, bf in self._bound_items():
            field = bf.field
            value = bf.initial if field.disabled else bf.data
            try:
                if isinstance(field, FileField):
                    value = field.clean(value, bf.initial)
                else:
                    value = field.clean(value)
                self.cleaned_data[name] = value
                if hasattr(self, 'clean_%s' % name):
                    value = getattr(self, 'clean_%s' % name)()
                    self.cleaned_data[name] = value
            except ValidationError as e:
                self.add_error(name, e)

    def _clean_form(self):
        try:
            cleaned_data = self.clean()
        except ValidationError as e:
            self.add_error(None, e)
        else:
            if cleaned_data is not None:
                self.cleaned_data = cleaned_data

    def _post_clean(self):
        """
        An internal hook for performing additional cleaning after form cleaning
        is complete. Used for model validation in model forms.
        """
        pass

    def clean(self):
        """
        Hook for doing any extra form-wide cleaning after Field.clean() has been
        called on every field. Any ValidationError raised by this method will
        not be associated with a particular field; it will have a special-case
        association with the field named '__all__'.
        """
        return self.cleaned_data
```

<br>

유효성 검사와 관련된 부분만 가져와봤다.

<br>

코드 전체를 딱 보고 이해할 순 없지만 대략적으로 파악해보면 clean 함수를 통해 유효성 검사를 하겠다 이말이다.


<br>


## clean 을 사용하여 validator 커스텀


<br>


### 필드별로 선언 

<br>

```python
from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model= Note
        fields =[
            'title',
            'content',
        ]
        
    def clean_title(self):
        clean_title = self.cleaned_data['title']
        if '바보' in clean_title:
            raise forms.ValidationError("바보는 나쁜 말")
        return clean_title

    def clean_content(self):
        cleaned_content = self.cleaned_data['content']
        if '멍청이' in cleaned_content:
            raise forms.ValidationError("멍청이는 나쁜 말")
        return cleaned_content
```

<br>

- `clean_[필드명]` 으로 인스턴스 함수를 선언
- `self.cleaned_data` 를 통해 인스턴의 값을 가져오기
- 원하는 조건 설정
- ValidationError 발생시키거나 해당하는 필드의 값을 return

<br>

주의할 점은 함수가 오버라이딩 되는 방식이기 때문에 함수명은 위의 구조를 꼭 지켜주어야 한다.



<br>

### 필드 전체적으로 선언


<br>


```python
from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model= Note
        fields =[
            'title',
            'content',
        ]
	def clean(self):
        cleaned_content = self.cleaned_data['content']
        clean_title = self.cleaned_data['title']
        if '바보' in clean_title:
            raise forms.ValidationError("바보는 나쁜 말")
        elif '멍청이' in cleaned_content:
            raise forms.ValidationError("멍청이는 나쁜 말")
        return self.cleaned_data
```

<br>

- clean 을 사용하게 되면 필드별 설정은 불가능하다.
  - 혹시라도 clean_필드 와 같이 사용하지 않게 주의하자.
  - 만약 전체적으로 적용하고 싶은 validator와 각 필드별 validator가 존재한다면 model에서 정의하는 것이 좋은 방법이라 생각됨.