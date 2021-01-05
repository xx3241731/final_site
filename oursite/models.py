from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True) #日期 
    

    class Meta:
        ordering = ('-pub_date',) #排序方式=(-日期)   -由新到舊排序

    def __str__(self):
        return self.title
    
class Covid(models.Model):
    country = models.CharField(max_length=100)
    cases = models.CharField(max_length=100)
    new_cases = models.CharField(max_length=100)
    deaths = models.CharField(max_length=100)
    new_deaths = models.CharField(max_length=100)

    class Meta:
        ordering = ('cases',) #排序方式=(-日期)   -由新到舊排序

    def __str__(self):
        return self.country