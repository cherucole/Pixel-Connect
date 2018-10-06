from django import forms
from .models import *

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['user', 'imagecommented']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

class UploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

