from django.db import models
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
# 태그 기능은 게시글과 다대다 관계(M:N)를 가질 수 있도록 해야 한다.

class HashTag(models.Model):
    name = models.CharField(max_length = 50, blank = False, verbose_name = 'HashTag')
    created_date = models.DateTimeField(auto_now_add = True, veerbose_name)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'HashTag'
        verbose_name = "해시태그"
        verbose_name_pural = "해시태그"
    
class DailyPost(models.Model):
    title = models.CharField(max_length = 100, blank = False) # 제목
    content = models.TextField(verbose_name = '본문') # 긴 글
    
    created_date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to = 'daily_post_imgs')
    
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, verbose_name = "작성자")
    tags = models.ManyToManyField('HashTag', verbose_name = '해시태그')
    
    def __str__(self):
        # django model 필드에 id라는 pk값이 자동으로 생성이 된다.
        return f"{self.id} : {self.title}"
    
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    class Meta:
        db_table = 'DailyPost'
        verbose_name = '일상 톡'
        
    
