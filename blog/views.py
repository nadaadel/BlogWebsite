from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Comment, Replay, Post, Tag,Word, Category
from .forms import PostForm, TagForm, CommentForm, RegisterationForm,CategoryForm,WordForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



def allPosts(request):
	all_post = Post.objects.all()
	context = {"allpost": all_post}
	return context


def  addPost(request):
	form = PostForm()
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/blog/home')
	return render(request, 'blog/addpost.html', {'form':form})



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
    return HttpResponseRedirect('login')

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

def admin(request):
	 return render(request, 'indexadmin.html')

def allPosts_admin(request):
	all_posts = Post.objects.all()
	context = {"allPosts_admin": all_posts}
	return render(request, 'allposts_admin.html', context)

def delete(request,pt_id):
	pt= Post.objects.get(id=pt_id)
	pt.delete()
	return HttpResponseRedirect ('/blog/allposts_admin')



def  addPost_admin(request):
	form = PostForm()
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/blog/home')
	return render(request, 'addpost.html', {'form':form})

def getPost(request, pt_id):
	pt = Post.objects.get(id = pt_id)
	context = {"post":pt }
	return render(request, "pt_details.html", context)


def allcategories_admin(request):
	all_categories = Category.objects.all()
	context = {"allcategories_admin": all_categories}
	return render(request, 'allcategories_admin.html', context)

def delete_category(request,ct_id):
	ct= Category.objects.get(id=ct_id)
	ct.delete()
	#return HttpResponse("Deleted	")
	return HttpResponseRedirect ('/blog/allcategories_admin')

def addCategory (request):
	category_form=CategoryForm()
	context= {"category":category_form}
	if request.method=="POST":
		category_form=CategoryForm(request.POST)
		if category_form.is_valid():
			category_form.save()
			return HttpResponseRedirect ("/blog/allcategories_admin")
	return render(request,"newCategory.html",context)

def update_category (request,ct_id):
	ct= Category.objects.get(id=ct_id)
	category_form=CategoryForm(instance=ct)

	if request.method=="POST":
		category_form=CategoryForm(request.POST,instance=ct)
		if category_form.is_valid():
			category_form.save()
			return HttpResponseRedirect('/blog/allcategories_admin')
	context={"category":category_form}
	return render (request,"newCategory.html",context)


def update_post (request,pt_id):
	pt= Post.objects.get(id=pt_id)
	post_form=PostForm(instance=pt)

	if request.method=="POST":
		post_form=PostForm(request.POST,instance=pt)
		if post_form.is_valid():
			post_form.save()
			return HttpResponseRedirect('/blog/allposts_admin')
	context={"form":post_form}
	return render (request,"addpost.html",context)

def update_word (request,wt_id):
	wt= Word.objects.get(id=wt_id)
	word_form=WordForm(instance=wt)

	if request.method=="POST":
		word_form=WordForm(request.POST,instance=wt)
		if word_form.is_valid():
			word_form.save()
			return HttpResponseRedirect('/blog/allwords_admin')
	context={"words":word_form}
	return render (request,"newWords.html",context)

def allusers_admin(request):
	all_users = User.objects.all()
	context = {"allusers_admin": all_users}
	return render(request, 'allusers_admin.html', context)

def block(request,ut_id):
	ut=User.objects.get(id=ut_id)
	ut.is_active=0
	ut.save()
	return HttpResponseRedirect ('/blog/allusers_admin')

def unblock(request,ut_id):
	ut= User.objects.get(id=ut_id)
	ut.is_active=1
	ut.save()
	#return HttpResponse("Deleted	")
	return HttpResponseRedirect ('/blog/allusers_admin')

def allwords_admin(request):
	all_words = Word.objects.all()
	context = {"allwords_admin": all_words}
	return render(request, 'allwords_admin.html', context)

def addWords(request):
	word_form=WordForm()
	context= {"words":word_form}
	if request.method=="POST":
		word_form=WordForm(request.POST)
		if word_form.is_valid():
			word_form.save()
			return HttpResponseRedirect ("/blog/allwords_admin")
	return render(request,"newWords.html",context)

def delete_word(request,wt_id):
	wt= Word.objects.get(id=wt_id)
	wt.delete()
	#return HttpResponse("Deleted	")
	return HttpResponseRedirect ('/blog/allwords_admin')
