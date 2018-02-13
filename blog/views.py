from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Comment,Replay,Category,Post,Tag,Word
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


def allPosts(request):
	# all_post = Post.objects.all()
	# context = {"allpost": all_post}
	# return render(request, "blog/home.html", context)
	return render(request, "blog/home.html")