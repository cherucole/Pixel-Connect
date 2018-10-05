from django.db import models
from tinymce.models import HTMLField
import datetime as dt


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

class Comment(models.Model):
    comment = models.CharField(max_length=30, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    imagecommented = models.ForeignKey('pixel_app.Post',on_delete=models.CASCADE, related_name='comments')

    def save_comment(self):
        self.save()

    # @classmethod
    # def get_comments(cls, id):
    #
    #     comments = Comment.objects.filter(id=id)
    #     return comments

    @classmethod
    def get_comments(cls, id):
        comments = Comment.objects.filter(post_id=id).all()
        return comments

    def __str__(self):
        return self.comment


class Post(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    # name = models.CharField(max_length=30)
    caption = HTMLField(blank=True)
    likes=models.IntegerField()
    opinions = models.ForeignKey(Comment,on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts')
    date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def all_posts(cls):
        posts = cls.objects.all()
        return posts

    @classmethod
    def show_by_id(cls, id):
        posts = cls.objects.filter(id=id)
        return posts


class Likes(models.Model):
	post = models.IntegerField()
	liker = models.CharField(max_length=20)