from django import forms
from .models import Comment ,Replay


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('description',)


class replayForm(forms.ModelForm):
	class Meta:
		model = Replay
		fields = ('description',)