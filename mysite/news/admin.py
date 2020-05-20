from django.contrib import admin
from django.urls import reverse
from . import models
from .models import Article, Reporter
# Register your models here.

admin.site.register(models.Article)
admin.site.register(Reporter)