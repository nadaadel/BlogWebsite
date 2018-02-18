from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Tag(models.Model):
    tag = models.CharField(max_length=50)
    def __str__(self):
        return self.tag



class Category(models.Model):
    category_name = models.CharField(max_length=200)
    cat = models.ManyToManyField(User)
    def __str__(self):
        return self.category_name


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.FileField()
    rate = models.IntegerField(null=True)
    likes = models.IntegerField(null=True)
    dislikes = models.IntegerField(null=True)
    date = models.DateTimeField(default=datetime.now())
    author = models.ForeignKey(User)
    category =models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag)
    def __str__(self):
        return self.title




class Comment(models.Model):
    post_comment= models.ForeignKey(Post)
    description = models.CharField(max_length=500)
    user_comment = models.ForeignKey(User)
    date=models.DateTimeField()
    def __str__(self):
        return self.description

class Replay(models.Model):
    comment_replay = models.ForeignKey(Comment)
    user_replay = models.ForeignKey(User)
    date = models.DateTimeField()
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.description




class Word(models.Model):
    word = models.CharField(max_length=50)



class Contact(models.Model):
    name= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    date=models.DateTimeField()
    def __str__(self):
        return self.description

# class Profile(models.Model):
#    name = models.CharField(max_length = 50)
#    picture = models.ImageField(upload_to = 'pictures')
#
#    class Meta:
#       db_table = "profile"


# class usersub(models.Model):
#     userid = models.ForeignKey(User)
#     categoryid=models.ForeignKey(Category)
