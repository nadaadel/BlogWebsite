from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post , Tag , Word ,Comment ,Replay,Category


class RegisterationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)

    class Meta:
        model=User
        fields = ('username','first_name','last_name' ,'email','name',)


    def save(self, commit=True):
        user = super(RegisterationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.status ='unblocked'
        if commit:
            user.save()
        return user



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'photo', 'rate', 'likes', 'dislikes', 'date','author',)

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('description',)

# class CatForm(forms.ModelForm):
# 	class Meta:
# 		model = Category
# 		fields = ('category_name',)

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ('category_name',)

class replayForm(forms.ModelForm):
	class Meta:
		model = Replay
		fields = ('description',)

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('tag',)

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ('word',)

# class searchForm(forms.Form):
#    search = forms.CharField(max_length = 100)
#
#
# class ProfileForm(forms.Form):
#    name = forms.CharField(max_length = 100)
#    picture = forms.ImageFields()
#
