from django import forms
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import FormView, TemplateView
from django.contrib.auth import authenticate, login, logout

from . import forms

def sign_up(request):
    if request.method == 'POST':
        form = forms.registerform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('http://127.0.0.1:8000/')
    else:
        form = forms.registerform()
    context = {
        'form' : form
    }
    return render(request, 'register.html', context)

def log_in(request):
    if request.method == 'POST':
        form = forms.loginform(request, data = request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('')
    else:
        form = forms.loginform()
    
    context = {
        'form' : form
    }
    return render(request, 'login.html', context)

# Create your views here.
class registerview(FormView):
    template_name = 'H:\\GitHub\\pawpy\\pawpy\\user\\templates\\register.html'
    form_class = forms.registerform
    success_url = 'http://127.0.0.1:8000/'
    initial = {
        "email" : "enter_your_email_address",
        "pet_num" : "enter_the_number_of_your_pet"
    }

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        pet_num = form.cleaned_data.get("pet_num")

        user = authenticate(email = email, password = password, pet_num = pet_num)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

def error(TemplateView):
    render('error.html')

class loginview(FormView):
    template_name = 'H:\\GitHub\\pawpy\\pawpy\\user\\templates\\login.html'
    form_class = forms.loginform
    success_url = 'http://127.0.0.1:8000/'
    
    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request,username= email,password = password)
        if user is not None:
            login(self.request, user)
    
    
        return super().form_valid(form)
    
    def log_out(request):
        logout(request)
        return redirect(reverse(''))

def log_out(request):
    logout(request)
    return render(request, 'index.html')
