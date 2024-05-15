from django.contrib import admin
from bachelor_projects.models import *
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article, ArticleAdmin)



