from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.BinaryField()
    rate = models.IntegerField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    date = models.DateTimeField()
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

class Word(models.Model):
    word = models.CharField(max_length=50)

class Tag(models.Model):
    tag = models.CharField(max_length=50)