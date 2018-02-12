from django.db import models

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