from django import forms

class DailyPostForm(forms.Form):
    title = forms.CharField(error_messages = {'required' : "Title Required"}, label = "제목")
    content = forms.TextField(error_messages = {'required' : "Content Required", label = "본문"})
    
    tags = forms.CharField(required = False, label = "태그")
    