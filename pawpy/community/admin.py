from django.contrib import admin
from .models import HashTag, DailyPost
# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = ('name')

class DailyPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image', 'writer','created_date', 'tags')
    
admin.site.register(HashTag, TagAdmin)
admin.site.register(DailyPost, DailyPostAdmin)