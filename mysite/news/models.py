'''
from django.db import models
from django.utils import timezone
from django.urls import reverse
import datetime
# Create your models here.
class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    
    #def was_published_recently(self):
        #now = timezone.now()
        #return now - datetime.timedelta(days=1) <= self.pub_date <= now
    #was_published_recently.admin_order_field = 'pub_date'
    #was_published_recently.boolean = True
    #was_published_recently.short_description = 'Published recently?'
    
    def __str__(self):
        return self.headline
'''
from django.db import models
from django.urls import reverse

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name


class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
    
    def get_absolute_url(self):
        return reverse("news:detail", args=(self.id,))