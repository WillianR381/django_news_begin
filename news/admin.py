from django.contrib import admin

# Register your models here.
from .models import Article, Reporter

admin.site.register(Article)
admin.site.register(Reporter)