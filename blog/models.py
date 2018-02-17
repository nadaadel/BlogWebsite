from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class Post(models.Model):
    title = models.CharField(max_length=200)
    # photo = models.TextField(default='null')
    description = models.TextField()
    rate = models.IntegerField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    date = models.DateTimeField(default=datetime.now())
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    description = models.CharField(max_length=500)
    user = models.ForeignKey(User)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.description


class Replay(models.Model):
    comment = models.ForeignKey(Comment)
    user = models.ForeignKey(User)
    date = models.DateTimeField(default=datetime.now())
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.description


class Test(models.Model):
    text = models.CharField(max_length=50)


class Word(models.Model):
    word = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.word


class Tag(models.Model):
    tag = models.CharField(max_length=50)
    post = models.ForeignKey(Post)


class Userlike(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    state = models.IntegerField()
