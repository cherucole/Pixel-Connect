from django.db import models
from tinymce.models import HTMLField
from .models import *

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    bio = HTMLField()
    email= models.EmailField()
    avatar = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.username

    def save_user(self):
        self.save()

    class Meta:
        ordering = ['username']

class Post(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    # name = models.CharField(max_length=30)
    caption = HTMLField()
    likes=models.IntegerField()
    comments = models.ForeignKey(Comment,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)


    # pub_date = models.DateTimeField(auto_now_add=True)
    @classmethod
    def all_posts(cls):
        posts = cls.objects.all()
        return posts


class Comment(models.Model):
    comment = models.CharField(max_length=30)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Likes(models.Model):
	post_id = models.IntegerField()
	liker = models.CharField(max_length=20)

