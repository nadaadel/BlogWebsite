from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm,TagForm ,CommentForm
from blog.models import Comment,Replay,Category,Post,Tag,Word
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterationForm
# from django.views.generric import ListView


def allPosts(request):
	all_post = Post.objects.all()
	context = {"allpost": all_post}
	return context






def addPost(request):
	form = PostForm()
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/blog/home')
	return render(request,'blog/addpost.html', {'form':form})


def  addTag(request):
	form = TagForm()
	if request.method == "POST":
		form = TagForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/blog/home')
	return render(request,'blog/addpost.html', {'form':form})


def postshow(request):
	post=Post.objects.get(title="ttttt")
	return render(request, 'blog/home.html', {'post': post})



def allComment(request,post_id):
	all_comments = Comment.objects.all(post_id)
	context = {"allposts": all_comments}
	return render(request, "post/details.html", context)

def  addTag(request):
	form = TagForm()
	if request.method == "POST":
		form = TagForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/blog/home')
	return render(request, 'blog/addpost.html', {'form':form})

def  addcomment(request,user_id):
	form = CommentForm()
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/blog/details')
	return render(request, 'blog/details.html', {'form':form})


def like(request,post_id):
	post = Post.objects.get(id =post_id)
	if request.method == "POST":
		post.likes+=1
		post.update()
	return




def checkdislike(request,post_id):
	post = Post.objects.get(id=post_id)
	num =post.dislikes
	if (num==8):
		post.delete()

# def get_home(request):
#     return render(request, "index.html")

# Create your views here.

def get_contact(request):
    return render(request, "contact.html")
# def get_home(request):
    # return render(request, "index.html")
def get_about(request):
    return render(request, "about.html")


def user_logout(request):
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect('home')

def login_form(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('home')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("Login success")
    return render(request, "login_form.html")

def register_form(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('home')
    if request.user.is_authenticated():
        return HttpResponse("You are Logged in")
    if request.method == "POST":
        user_form = RegisterationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect('home')
    else:
        user_form = RegisterationForm()
    return render(request, "register_form.html", {'form': user_form})

def home(request):
	context = allPosts(request)
	# get_home(request)
	return render(request, "index.html", context)


