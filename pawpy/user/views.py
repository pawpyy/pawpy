from django import forms
from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from . import forms

# Create your views here.
class registerview(FormView):
    template_name = 'H:\\GitHub\\pawpy\\pawpy\\user\\templates\\register.html'
    form_class = forms.registerform
    success_url = reverse_lazy('')
    initial = {
        "email" : "enter_your_email_address",
        "password" : "enter_your_password",
        "pet_num" : "enter_the_number_of_your_pet"
    }