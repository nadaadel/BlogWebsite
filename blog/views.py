from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Comment,Replay,Category,Post,Tag,Word
from blog.models import Comment, Replay, Post, Tag,Word, Category
from .forms import PostForm, TagForm, CommentForm, RegisterationForm,CategoryForm,WordForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import json
from django.http import JsonResponse
import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
################################################
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render_to_response ,RequestContext

#============================Home===============================#
def allPosts(request):
	all_post = Post.objects.all()
	context = {"allpost": all_post}
	return context

def allcat(request):
	allcat = Category.objects.all()
	context = {"allcat": allcat}
	return context

def allsub(request,cat_id):
	allsub=Category.cat.through.objects.filter(user_id=request.user.id)
	context = {"allsub": allsub}
	return context


def home(request):
	all_post = Post.objects.all().order_by('-date' )[:5]
	all_cat = Category.objects.all()
	all_post3 = Post.objects.order_by('-date' )[:3]
	allsub = Category.cat.through.objects.filter(user_id=request.user.id)
	categories=[]
	for s in allsub:
		# category = Category.objects.filter(id=s.category_id)
		categories.append(s.category_id)

	# contact_list = all_post
	# page = request.GET.get('page', 1)
	# paginator = Paginator(contact_list, 4)  # Show 25 contacts per page
    #
	# try:
	# 	contacts = paginator.page(page)
	# except PageNotAnInteger:
	# 	contacts = paginator.page(page)
	# except EmptyPage:
	# 	contacts = paginator.page(paginator.num_pages)
	return render(request, "index.html", {"allpost":all_post , "allcat":all_cat ,"allpost3" : all_post3 ,"allsub" : categories})
	# return HttpResponse(categories)


#=============================== search===========================#

def postshow(request):
	posts=Post.objects.filter(title__contains=request.POST['search_box'])

	try:
		tag = Tag.objects.get(tag__contains=request.POST['search_box'])
		posts2 = Post.objects.filter(tag=tag.id)

	except :
		return render(request, 'test.html', {'posts': posts})
	else:
		return render(request, 'test.html', {'posts': posts, "posts2": posts2})

#===============================end search===========================#

def get_contact(request):
	# send_mail('Subject here','minaaaaaaa','mina7esh@gmail.com',['minaibrahim1991@yahoo.com',],fail_silently=False,)
	return render(request, "contact.html")

def get_about(request):
    return render(request, "about.html")

#===========================sub & unsub =================================#

def sub(request,cat_id):
	user=request.user
	category = Category.objects.get(id=cat_id)
	category.cat.add(request.user.id)
	# subject = "Thank you ya m3lem "
	# message ="welcome ya m3lem"
	# to_list=['mina7esh@gmail.com',settings.EMAIL_HOST_USER]
	# from_email = settings.EMAIL_HOST_USER
	# send_mail(subject,message,from_email,to_list,fail_silenty=True)
	send_mail(
		'Subject here',
		'hello nada aaaaaaaaa',
		'minaibrahim1991@yahoo.com',
		['mina7esh@gmail.com'],
		fail_silently=False,
	)

	return HttpResponse(cat_id)
#

def unsub(request,cat_id):
	user=request.user

	cat_id=int(cat_id)
	# category = Category.objects.filter(id=cat_id,cat=2)
	Category.cat.through.objects.filter(category_id=cat_id,user_id=request.user.id).delete()
	return HttpResponse("done")






#====================================end home ============================#







#==================================admin panal ==========================#

def  addTag(request):
	form = TagForm()
	if request.method == "POST":
		form = TagForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/blog/addPost_admin')
	return render(request, 'addtag.html', {'form': form})


def getCat(request):
    return render(request , "category.html")

#html

def admin(request):
	 return render(request, 'indexadmin.html')

def allPosts_admin(request):
	all_posts = Post.objects.all()
	context = {"allPosts_admin": all_posts}
	return render(request, 'allposts_admin.html', context)

def delete(request,pt_id):
	pt= Post.objects.get(id=pt_id)
	pt.delete()
	return HttpResponseRedirect ('/blog/allposts_admin/')


def getPosts(request,cat_id):
	pt= Post.objects.filter(category=cat_id).order_by('-date' )
	context={"posts":pt}
	return render(request, 'category.html', context)


def  addPost_admin(request):
	form = PostForm()
	if request.method == "POST":
		form = PostForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/blog/allposts_admin/')
	return render(request, 'addpost.html', {'form': form})

def getPost(request,pt_id):
	pt = Post.objects.get(id = pt_id)
	context = {"post":pt }
	return render(request, "pt_details.html", context)

def getPost2(request,post_id):
	pt = Post.objects.get(id = post_id)
	context = {"post":pt }
	tags = Tag.objects.filter(post=post_id)
	context2={"tags":tags}
	return render(request, "single.html", {"post":pt ,"tags":tags})


def allcategories_admin(request):
	all_categories = Category.objects.all()
	context = {"allcategories_admin": all_categories}
	return render(request, 'allcategories_admin.html', context)

def delete_category(request,ct_id):
	ct= Category.objects.get(id=ct_id)
	ct.delete()
	#return HttpResponse("Deleted	")
	return HttpResponseRedirect ('/blog/allcategories_admin/')

def addCategory (request):
	category_form=CategoryForm()
	context= {"category":category_form}
	if request.method=="POST":
		category_form=CategoryForm(request.POST)
		if category_form.is_valid():
			category_form.save()
			return HttpResponseRedirect ("/blog/allcategories_admin/")
	return render(request,"newCategory.html",context)

def update_category (request,ct_id):
	ct= Category.objects.get(id=ct_id)
	category_form=CategoryForm(instance=ct)

	if request.method=="POST":
		category_form=CategoryForm(request.POST,instance=ct )
		if category_form.is_valid():
			category_form.save()
			return HttpResponseRedirect('/blog/allcategories_admin/')
	context={"category":category_form}
	return render (request,"newCategory.html",context)


def update_post (request,pt_id):
	pt= Post.objects.get(id=pt_id)
	post_form=PostForm(instance=pt)

	if request.method=="POST":
		post_form=PostForm(request.POST,request.FILES,instance=pt)
		if post_form.is_valid():
			post_form.save()
			return HttpResponseRedirect('/blog/allposts_admin/')
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
def promote(request,ut_id):
	ut=User.objects.get(id=ut_id)
	ut.is_superuser=1
	ut.save()
	return HttpResponseRedirect ('/blog/allusers_admin')

def unpromote(request,ut_id):
	ut= User.objects.get(id=ut_id)
	ut.is_superuser=0
	ut.save()
	#return HttpResponse("Deleted	")
	return HttpResponseRedirect ('/blog/allusers_admin')

def delete_user(request,ut_id):
	ut= User.objects.get(id=ut_id)
	ut.delete()
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

# def checktag
	# pattern = re.findall(r"#(\w+)", s)
	# pattern.match(string)