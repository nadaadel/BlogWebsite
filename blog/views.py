from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm,TagForm
from blog.models import Comment,Replay,Category,Post,Tag,Word
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


def allPosts(request):
	all_post = Post.objects.all()
	context = {"allpost": all_post}
	return render(request, "blog/home.html", context)
	return render(request, "blog/home.html")

def  addPost(request):
	form = PostForm()
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/blog/home')
	return render(request, 'blog/addpost.html', {'form':form})


def  addTag(request):
	form = TagForm()
	if request.method == "POST":
		form = TagForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/blog/home')
	return render(request, 'blog/addpost.html', {'form':form})

def search(request):
	if request.method == "POST":
		search_text=request.POST['search_text']
	else:
		search_text=''
	post =Post.objects.filter(title__contains=search_text)
	return render_to_response("ajax_search.html",{"post" : post})


def postshow(request):
	post=Post.objects.get(title="ttttt")
	return render(request, 'blog/home.html', {'post': post})