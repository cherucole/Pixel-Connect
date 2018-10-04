from django import forms
from .models import *

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')

# class NewAricleForm(forms.ModelForm):
#     class Meta:
#         model=Article
#         exclude = ['editor', 'pub_date']
#         widgets = {
#             'tags': forms.CheckboxSelectMultiple(),
#         }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('user_id', 'comment',)