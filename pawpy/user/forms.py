from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from django import forms
from . import models

class registerform(ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label = 'password confirm', widget=forms.PasswordInput)
    email = forms.EmailField(required=True,widget=forms.EmailInput())
    class Meta: # 연결할 model과 사용할 field를 지정
        model = models.user
        fields = (
            "email",
            "pet_num",
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit = True):
        user = super().save(commit = False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class userchangeform(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label = 'password')
    class Meta:
        model = models.user
        fields = ('email', 'password', 'pet_num',)
    
    def clean_password(self):
        return self.initial['password']

class loginform(ModelForm):
    class Meta:
        model = models.user
        fields = (
            "email",
            "password"
        )
        # 로그인 시에는 이메일 주소와 비밀번호만 입력 받는다.

    
    