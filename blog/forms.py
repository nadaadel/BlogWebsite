from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Tag, Word, Comment, Replay, Category


class RegisterationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # User._meta.get_field_by_name('email').unique = True

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def save(self, commit=True):
        user = super(RegisterationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.status = 'unblocked'
        if commit:
            user.save()
        return user

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description',  'author','photo' ,'category','tag', )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('description',)


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('description',)


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



