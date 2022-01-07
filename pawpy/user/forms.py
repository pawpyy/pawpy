from django import forms
from django.forms import ModelForm
from django import forms
from . import models

class registerform(ModelForm):
    class Meta: # 연결할 model과 사용할 field를 지정
        model = models.user
        fields = (
            "email",
            "password",
            "pet_num"
        )
        password = forms.CharField(widget = forms.PasswordInput)
    
    
    
    