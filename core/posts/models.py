from django.db import models

class Posts(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=100000)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

class UserLikes(models.Model):
    user_id = models.IntegerField()
    likes = models.CharField(max_length=100000)

class UserComments(models.Model):
    comment_id = models.IntegerField()
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=100000)