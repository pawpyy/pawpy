# user/backends.py

from django.contrib.auth.backends import ModelBackend
from .models import user
from django.contrib.auth.hashers import check_password

class userBackend(ModelBackend):
    def authenticate(self, request, email, password):
        try:
            logined_user = user.objects.get(email = email)
            #return logined_user
            if logined_user.check_password(password):
                return logined_user
            
            
        except user.DoesNotExist:
            pass