from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    tittle = models.CharField(max_length=255)
    slug = models.SlugField(max_length= 255, unique=True)
    #slug para acesso da página
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now= True)

    def __str__(self):
        return self.tittle