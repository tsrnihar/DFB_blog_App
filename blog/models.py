from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail',args = [str(self.id)])



