from django import forms
from django.contrib.auth.models import User
from .models import Post , Tag , Word ,Comment ,Replay


from .models import Comment ,Replay


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('description',)


class replayForm(forms.ModelForm):
	class Meta:
		model = Replay
		fields = ('description',)

# class UserForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields = ('username','first_name','last_name' ,'email','password','status','type',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'photo', 'rate', 'likes', 'dislikes', 'date','author',)

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('tag',)

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ('word',)

