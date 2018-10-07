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

    @classmethod
    def search_profile(cls,search):
        profile = Profile.objects.filter(user__username__icontains = search)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile

    class Meta:
        ordering = ['user']

class Comment(models.Model):
    comment = models.CharField(max_length=30, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True)
    imagecommented = models.ForeignKey('pixel_app.Post',on_delete=models.CASCADE, related_name='comments',blank=True)

    def save_comment(self):
        self.save()


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
    likes=models.IntegerField(default=0)
    opinions = models.ForeignKey(Comment,on_delete=models.CASCADE, null=True, blank=True)
    user_profile = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts',blank=True)
    date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def one_image(cls, id):
        post=Post.objects.filter(id=id)
        return post


    @classmethod
    def get_post_by_id(cls,id):
        post = Post.objects.filter(id = Post.id)
        return post

    @classmethod
    def all_posts(cls):
        posts = cls.objects.all()
        return posts


    @classmethod
    def get_user_images(cls, profile_id):
        images=Post.objects.filter(profile_id=id)

    @classmethod
    def get_profile_image(cls, profile):
        posts = Post.objects.filter(user_profile__pk=profile)
        return posts

    @classmethod
    def get_post_by_id(cls,id):
        post = Post.objects.filter(id = Post.id)
        return post
    #
    # @classmethod
    # def get_post_by_id(cls, id):
    #     post = Post.objects.filter(id = Post.id)
    #     return post

class Likes(models.Model):
	post = models.IntegerField()
	liker = models.CharField(max_length=20)