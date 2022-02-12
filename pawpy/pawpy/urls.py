"""pawpy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import user.views as user
import home.views as home
import community.views as community

urlpatterns = [
    path('admin/', admin.site.urls),
    # home
    path('', home.home, name = 'home'),
    # user
    path("register/", user.sign_up, name = 'register'),
    path('login/', user.log_in, name = 'login'),
    path("logout/",user.log_out, name = 'logout'),
    path('error/', user.error, name = 'error'),
    path('mypage/', user.mypage, name = 'mypage'),
    # community
    path('daily_post/', community.list_daily, name = 'list_daily'),
    path('daily_post/new', community.write_daily, name = 'write_daily'),
    path('daily_post/<int:pk>/detail', community.show_daily, name = 'show_daily'),
    
]
