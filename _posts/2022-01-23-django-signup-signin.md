---
title:  "django 회원가입과 로그인/로그아웃"
excerpt: "장고 auth의 회원가입, 로그인/로그아웃"
categories:
 - Django
tags:
 - [Django,python,study,TIL]
last_modified_at: 2022-01-23
toc: true
toc_sticky: true
published: true
---

# django 회원가입과 로그인/로그아웃 구현

<br>

장고 auth에서 제공하는 기능들로 회원가입과 로그인/로그아웃을 구현해보자.

<br>

## 회원가입 



<br>

장고의 모든 기능이 그러하듯 회원가입도 FBV/CBV 두 가지 방법을 제시한다.

<br>

본 글에서는 회원가입은 두 기능을 적절히 섞어서 구현해보겠다.

<br>

### 클래스 기반 form 생성

<br>

우선 회원가입을 위한 POST 요청을 받기 위해서 form 을 만들어보자.

<br>

장고에서는 회원가입 폼을 위해 django.contrib.auth.forms에서 `UserCreationForm` 클래스를 제공한다. 

해당 클래스를 상속받아 기능을 확장하는 식으로 진행해보자.

<br>

우선  `UserCreationForm`  의 기본 코드는 다음과 같다.


<br>


```python
class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = True

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
```

<br>

기본 form 필드로는 비밀번호, 비밀번호 확인, 아이디 이렇게만 존재한다.

그리고 유효성 검사와 저장에대한 함수가 선언되어있다.

<br>

해당 클래스를 상속받아 나만의 회원가입 form 을 만들 수 있다.

<br>

```python
class SignupForm(UserCreationForm):
    class Meta:
        model= get_user_model()
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'nickname',
        ]
    def clean_nickname(self):
        nickname= self.cleaned_data['nickname']
        if get_user_model().objects.filter(nickname=nickname).exists():
            raise forms.ValidationError("사용중인 닉네임 입니다.")
        else :
            return nickname
```

<br>

Meta 클래스에서 모델과 필드 위젯등을 지정해줄 수있다.

위젯은 별도로 설정해주지 않는다면 모델 필드에 맞게 생성된다.

<br>

나는 닉네임에 대한 중복 검사 항목을 추가했다.

해당 항목을 통해 닉네임 모델에 Unique = True 설정 없이도 데이터의 유일성을 유지할 수있다.

<br>

### 함수 기반 회원가입 view 생성

<br>

제너릭 뷰의 `CreateView` 를 상속받아 CBV 방식으로 회원 가입을 구현할 수 있지만, 나는 함수 기반으로 구현해봤다.

<br>

```python
from django.contrib.auth import login as Sign_login
from django.shortcuts import render, redirect

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            Sign_login(request, signed_user)
            return redirect('index')
    else :
        form = SignupForm()
    return render(request, 'accounts/signup_form.html',{
            'form': form
        })
```

<br>


http 요청의 방식에 따라 POST 이면 지정해둔 모델 form 을 이용하여 유효성 검사후 저장한다.

이후에 auth의 login 기능을 이용하여 회원가입 이후 로그인 세션을 유지시켜 준다. 

그리고 redirect로 회원가입 후 이동할 페이지를 설정한다.

만약 POST 요청이 아니면 빈 폼을 만들어서 회원가입 폼을 작성할 수 있는 템플릿으로 render해준다.

<br>

*url 맵핑과 form 에 대한 부분은 회원가입이라고 특별할 게 없어 생략했습니다.*


<br>


## 로그인

<br>

로그인 기능 또한 auth 앱에서 제공해주는 기능들을 이용하면 어렵게 세션을 만들고 유지시키는 과정을 모두 생략해도 된다.


<br>


로그인의 경우엔 form을 작성할 필요도 없다.

auth에 내장되어 있는 `LoginView` 를 이용하면 url 맵핑과 로그인 템플릿만 만들어주면 모든 준비가 끝난다.

<br>

### 클래스 기반 로그인 뷰 생성

<br>

```python
from django.contrib.auth.views import LoginView

login = LoginView.as_view(template_name='accounts/login_form.html')
```

<br>

이게 전부이다.

<br>

놀랍지 아니한가.

<br>

물론 기본 기능만을 이용한 것이며 as_view에 몇몇 인수로 자세한 설정도 가능하다.

그러나 기본 로그인만을 원한다면 로그인 폼을 작성할 템플릿만 명시해주면 된다.

<br>



### settings.py 설정

<br>

아래 코드는 auth앱의 LoginView 클래스 코드이다.

<br>

```python
class LoginView(SuccessURLAllowedHostsMixin, FormView):
    """
    Display the login form and handle the login action.
    """
    form_class = AuthenticationForm
    authentication_form = None
    next_page = None
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'registration/login.html'
    redirect_authenticated_user = False
    extra_context = None

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return self.get_redirect_url() or self.get_default_redirect_url()

    def get_redirect_url(self):
        """Return the user-originating redirect URL if it's safe."""
        redirect_to = self.request.POST.get(
            self.redirect_field_name,
            self.request.GET.get(self.redirect_field_name, '')
        )
        url_is_safe = url_has_allowed_host_and_scheme(
            url=redirect_to,
            allowed_hosts=self.get_success_url_allowed_hosts(),
            require_https=self.request.is_secure(),
        )
        return redirect_to if url_is_safe else ''

    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        return resolve_url(self.next_page or settings.LOGIN_REDIRECT_URL)

    def get_form_class(self):
        return self.authentication_form or self.form_class

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update({
            self.redirect_field_name: self.get_redirect_url(),
            'site': current_site,
            'site_name': current_site.name,
            **(self.extra_context or {})
        })
        return context
```

<br>

```python
 def get_default_redirect_url(self):
        """Return the default redirect URL."""
        return resolve_url(self.next_page or settings.LOGIN_REDIRECT_URL)
```

<br>

중간에 보면 위와 같은 함수가 정의되어 있다. 

resolve_url 에서 참조하는 `settings.LOGIN_REDIRECT_URL` 덕분에 로그인 뷰를 사용하였을 때 해당 설정의 default인 'accounts/profile' URL 로 이동하게 된다.

뭐 구현해놨다면 상관 없지만 일반적인 경우라면 404 에러를 마주칠 수 밖에 없다.

<br>

이 문제는 프로젝트의 settings.py 에서 해당 설정 부분을 추가해주면 된다..

<br>

```python
LOGIN_REDIRECT_URL ='/'
```

<br>

나의 경우엔 기본 index 페이지로 이동하도록 설정했다.

<br>



## 로그아웃

<br>

로그아웃은 로그인보다도 간단하다.

<br>

form도 template도 필요 없다.

<br>

url 맵핑과 매우 간단하 함수 기반 view 만으로도 구현 할 수 있다.

<br>

### 함수 기반 ..?  로그아웃 구현


<br>


```python
from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('index')

```

<br>

logout 에 별칭을 붙여준 이유는 함수명과 충돌이 남을 방지하기 위함이다.



<br>