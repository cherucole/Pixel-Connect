from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt


# Create your models here.

class Profile(models.Model):
    bio = HTMLField()
    avatar = models.ImageField(upload_to='images/', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.user

    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls, id):
        profile = Profile.objects.get(user=id)
        return profile

    class Meta:
        ordering = ['user']

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
    user_profile = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts')
    date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def all_posts(cls):
        posts = cls.objects.all()
        return posts


    @classmethod
    def get_user_images(cls, profile_id):
        images=Post.objects.filter(profile_id=id)

    @classmethod
    def get_profile_image(cls, profile):
        posts = Post.objects.filter(profile__pk=profile)
        return posts


class Likes(models.Model):
	post = models.IntegerField()
	liker = models.CharField(max_length=20)