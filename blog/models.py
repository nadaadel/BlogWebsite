from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	category_name=models.CharField(max_length=200)
	def __str__(self):
		return self.category_name

class Comment(models.Model):
    post_id= models.ForeignKey(Post)
    description = models.CharField(max_length=500)
    user_id = models.ForeignKey(User)
    date=models.DataTimeField()
    photo_user=models.ForeignKey(User)
    def __str__(self):
        return self.description

class Replay(models.Model):
    comment_id = models.ForeignKey(Comment)
    user_id = models.ForeignKey(User)
    photo_user = models.ForeignKey(User)
    date = models.DataTimeField()
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.description


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

