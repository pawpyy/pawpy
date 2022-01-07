from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class usermanager(BaseUserManager):
    def create_user(self, password, email, pet_num):
        user = self.model(
            email = self.normalize_email(email),
            pet_num = pet_num,
            is_superuser = 0,
            is_staff = 0,
            is_active = 1
        )
        user.set_password(password)
        user.save(using = self._db)

        return user
    
    def create_superuser(self, password, email, pet_num):
        user = self.create_user(
            email = email,
            password = password,
            pet_num = pet_num
        )
        user.is_superuser = 1
        user.is_staff = 1
        user.save(using = self._db)
        
        return user

# Create your models here.
class user(AbstractBaseUser):
    password = models.CharField(max_length = 100)
    # 사용자가 처음에 회원가입을 할 때에 이메일을 등록하도록 한다.
    email = models.EmailField(unique = True, null = False, blank = False, primary_key=True) # 사용자 이름을 따로 입력하라고 하는 대신 사용
    username = models.CharField(unique = True, max_length = 100, default = str(email).split('@')[0], auto_created = True) # 이메일을 입력하면 동시에 사용자 이름으로 지정
    is_superuser = models.IntegerField()
    is_staff = models.IntegerField()
    is_active = models.IntegerField()

    pet_num = models.IntegerField() # 총 키우는 / 등록하고자 하는 동물의 수

    objects = usermanager()

    USERNAME_FIELD = 'username' # 사용자 ID로 사용할 속성
    REQUIRED_FIELDS = ['email', 'password', 'pet_num']

    def has_perm(self, perm, obj = None):
        return True
    
    def has_module(self, app_label):
        return True
    
    class Meta:
        db_table = 'auth_user' # db table이름으로 auth_user으로 설정

    def mail_to_name(self):
        email = self.email
        a,b = email.split('@')
        return a

class pet(models.Model):
    pet_no = models.AutoField(primary_key=True) # 사이트에 등록한 동물의 번호 (고유키 값으로 사용)
    name = models.CharField('NAME', max_length = 30) # name of the pet
    owner = models.ForeignKey('user', on_delete = models.CASCADE, verbose_name = 'OWNER', blank = False, null = False) # 무조건 주인이 정해져 있어야 함
    age = models.IntegerField('AGE')
    birth = models.DateField('BIRTHDAY',  blank = False, null = False)

    def __str__(self):
        return self.owner.username + '_' + self.name

