from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	category_name=models.CharField(max_length=200)
	def __str__(self):
		return self.category_name

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(blank=True ,null=True,
    upload_to="cover/%Y/%m/%D/")
    rate = models.IntegerField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    date = models.DateTimeField()
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post_id= models.ForeignKey(Post)
    description = models.CharField(max_length=500)
    userid = models.ForeignKey(User)
    date=models.DateTimeField()
    def __str__(self):
        return self.description

class Replay(models.Model):
    comment_id = models.ForeignKey(Comment)
    userid = models.ForeignKey(User)
    date = models.DateTimeField()
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.description




class Word(models.Model):
    word = models.CharField(max_length=50)

class Tag(models.Model):
    tag = models.CharField(max_length=50)

