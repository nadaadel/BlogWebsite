from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import PostForm, TagForm, CommentForm
from blog.models import Comment, Replay, Category, Post, Tag, Word, Category, Userlike
from django.http import HttpResponse
from blog.models import Comment, Replay, Category, Post, Tag, Word
from blog.models import Comment, Replay, Post, Tag, Word, Category
from .forms import PostForm, TagForm, CommentForm, RegisterationForm, CategoryForm, WordForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import json
from django.http import JsonResponse
import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render_to_response, RequestContext


# ============================Home===============================#
def allPosts(request):
    all_post = Post.objects.all()
    context = {"allpost": all_post}
    return context


def allcat(request):
    allcat = Category.objects.all()
    context = {"allcat": allcat}
    return context


def allsub(request, cat_id):
    allsub = Category.cat.through.objects.filter(user_id=request.user.id)
    context = {"allsub": allsub}
    return context

def home(request):
    all_post = Post.objects.all().order_by('-date')
    all_cat = Category.objects.all()
    all_post3 = Post.objects.order_by('-date')[:3]
    allsub = Category.cat.through.objects.filter(user_id=request.user.id)
    categories = []
    for s in allsub:
        categories.append(s.category_id)

    contact_list = all_post
    page = request.GET.get('page', 1)
    paginator = Paginator(contact_list, 5)  # Show 25 contacts per page

    try:
    	contacts = paginator.page(page)
    except Exception as e :
        print e
    	contacts = paginator.page(page)
    except EmptyPage:
    	contacts = paginator.page(paginator.num_pages)
    return render(request, "index.html", {"posts": contacts, "categories": all_cat, "tops": all_post3, "allsub": categories ,"slider" : all_post3})


# ============================== home===============================

def getCat(request):
    return render(request, "category.html")


# =============================== search===========================#

def postshow(request):
    posts = Post.objects.filter(title__contains=request.POST['search_box'])
    text_search = request.POST['search_box']
    try:
        tag = Tag.objects.filter(tag__contains=request.POST['search_box'])
        poststag = Post.objects.filter(tag=tag)

    except:
        return render(request, 'category.html', {'posts': posts , 'text_search' :text_search})
    else:
        return render(request, 'category.html', {'posts': posts, 'poststag': poststag ,'text_search' :text_search})


# ===============================end search===========================#

def get_contact(request):
    return render(request, "contact.html")

# ===========================sub & unsub =================================#

def sub(request, cat_id):
    user = User.objects.get(id=request.user.id)
    category = Category.objects.get(id=cat_id)
    category.cat.add(request.user.id)
    cat =category.category_name
    body="HI "+user.first_name+ " you are subscribe on "+cat+" we are happy to have you"
    send_mail(
        'Subject here',
        body,
        'mina7esh@gmial.com',
        [user.email],
        fail_silently=False,
    )

    return HttpResponse(cat_id)


#

def unsub(request, cat_id):
    user = request.user

    cat_id = int(cat_id)
    # category = Category.objects.filter(id=cat_id,cat=2)
    Category.cat.through.objects.filter(category_id=cat_id, user_id=request.user.id).delete()
    return HttpResponse("done")


# ====================================end home ============================#


# ==================================admin panal ==========================#
def add_userAdmin(request):
    user_form = RegisterationForm()
    context = {"form": user_form}
    if request.method == "POST":
        user_form = RegisterationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect("/blog/allusers_admin")
    return render(request, "register_form.html", context)

def addTag(request):
    form = TagForm()
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog/addPost_admin')
    return render(request, 'addtag.html', {'form': form})


def getCat(request):
    return render(request, "category.html")


# html

def admin(request):
    return render(request, 'indexadmin.html')


def allPosts_admin(request):
    all_posts = Post.objects.all()
    context = {"allPosts_admin": all_posts}
    return render(request, 'allposts_admin.html', context)


def delete(request, pt_id):
    pt = Post.objects.get(id=pt_id)
    pt.delete()
    return HttpResponseRedirect('/blog/allposts_admin')


def getPosts(request, cat_id):
    pt = Post.objects.filter(category=cat_id).order_by('-date')
    category = Category.objects.get(id=cat_id)
    categoryName = category.category_name
    context = {"posts": pt , "categoryName" : categoryName}
    return render(request, 'category.html', context)


def addPost_admin(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog/allposts_admin')
    return render(request, 'addpost.html', {'form': form})


def getPost(request, pt_id):
    pt = Post.objects.get(id=pt_id)
    context = {"post": pt}
    return render(request, "pt_details.html", context)


def getPost2(request, post_id):
    pt = Post.objects.get(id=post_id)
    context = {"post": pt}
    tags = Tag.objects.filter(post=post_id)
    context2 = {"tags": tags}
    return render(request, "single.html", {"post": pt, "tags": tags})

def allcategories_admin(request):
    all_categories = Category.objects.all()
    context = {"allcategories_admin": all_categories}
    return render(request, 'allcategories_admin.html', context)


def delete_category(request, ct_id):
    ct = Category.objects.get(id=ct_id)
    ct.delete()
    # return HttpResponse("Deleted	")
    return HttpResponseRedirect('/blog/allcategories_admin')


def allPosts(request):
    all_post = Post.objects.all()[:5]
    context = {"allpost": all_post}
    return context

def addCategory(request):
    category_form = CategoryForm()
    context = {"category": category_form}
    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect("/blog/allcategories_admin")
    return render(request, "newCategory.html", context)


def update_category(request, ct_id):
    ct = Category.objects.get(id=ct_id)
    category_form = CategoryForm(instance=ct)
    if request.method == "POST":
        category_form = CategoryForm(request.POST, request.FILES, instance=ct)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect('/blog/allcategories_admin')
    context = {"category": category_form}
    return render(request, "newCategory.html", context)


# ====================================post details ===================================
# @login_required
def get_post(request, post_id):
    if request.user.is_authenticated():
        if request.method == "POST":
            if 'replyBtn' in request.POST:
                textReply = request.POST['replay_text']
                words = request.POST['replay_text'].split()
                badwords = Word.objects.all()
                for word in words:
                    for wordobi in badwords:
                        if word == wordobi.word:
                            wordLen = len(word)
                            newWord = '*' * wordLen
                            textReply = textReply.replace(word, newWord)
                replay = Replay.objects.create(description=textReply,
                                               comment_id=request.POST['comment_id'], user_id=request.user.id)
                replay.save()
                return HttpResponseRedirect('/blog/single/%s' % post_id)
            elif 'commentBtn' in request.POST:
                textComment = request.POST['comment_text']
                words = request.POST['comment_text'].split()
                badwords = Word.objects.all()
                for word in words:
                    for wordobi in badwords:
                        if word == wordobi.word:
                            wordLen = len(word)
                            newWord = '*' * wordLen
                            textComment = textComment.replace(word, newWord)

                comment = Comment.objects.create(description=textComment,
                                                 post_id=post_id, user_id=request.user.id)
                comment.save()
                return HttpResponseRedirect('/blog/single/%s' % post_id)

    onePost = Post.objects.get(id=post_id)
    postAuthor = User.objects.get(id=onePost.author_id)
    all_comments = Comment.objects.filter(post_id=post_id)
    replay_comments = Replay.objects.all()
    tags = Tag.objects.filter(post=post_id)
    userLikes = Userlike.objects.filter(post_id=post_id, user_id=request.user.id)
    category = Category.objects.get(id = onePost.category_id)
    categoryName = category.category_name
    other = Post.objects.get(id=1)
    if not userLikes:
        context = {'post': onePost, 'postAuthor': postAuthor, 'allComments': all_comments, 'tags': tags,
                   'replay_comments': replay_comments ,'categoryName' : categoryName , 'other' :other}
    else:
        userLikess = Userlike.objects.get(post_id=post_id, user_id=request.user.id)
        context = {'post': onePost, 'postAuthor': postAuthor, 'allComments': all_comments, 'tags': tags,
                   'replay_comments': replay_comments, 'userlike': userLikess ,'categoryName' : categoryName , 'other' :other}

    return render(request, "single.html", context)


# ajax like handel
@login_required
def checkLike(request):
    if request.user.is_authenticated():
        post_id = request.GET.get('postid')
        checklike = Userlike.objects.filter(post_id=post_id, user_id=request.user.id)
        onepost = Post.objects.get(id=post_id)
        likeCount = onepost.likes
        dislikeCount = onepost.dislikes
        if not checklike:
            userliked = Userlike.objects.create(state=1,
                                                post_id=post_id, user_id=request.user.id)
            userliked.save()
            Post.objects.filter(id=post_id).update(likes=(likeCount + 1))
        else:
            userlike = Userlike.objects.get(post_id=post_id, user_id=request.user.id)
            if userlike.state == 1:
                userlike.delete()
                Post.objects.filter(id=post_id).update(likes=(likeCount - 1))
            else:
                userlike.update(state=1)
                Post.objects.filter(id=post_id).update(likes=(likeCount + 1))
                Post.objects.filter(id=post_id).update(dislikes=(dislikeCount - 1))

        likedata = Post.objects.get(id=post_id)
        likedata.likes
        data = json.dumps({'likedata': likedata.likes})
        # return JsonResponse(serializers.serialize('json', {'likedata': 12}), safe=False)
        return JsonResponse(data, safe=False)


# ajax dislike handle
def checkdisLike(request):
    if request.user.is_authenticated():
        post_id = request.GET.get('postid')
        checkdislike = Userlike.objects.filter(post_id=post_id, user_id=request.user.id)
        onepost = Post.objects.get(id=post_id)
        dislikeCount = onepost.dislikes
        likeCount = onepost.likes
        if not checkdislike:
            userdisliked = Userlike.objects.create(state=0,
                                                   post_id=post_id, user_id=request.user.id)
            userdisliked.save()
            Post.objects.filter(id=post_id).update(dislikes=(dislikeCount + 1))
        else:
            userdislike = Userlike.objects.get(post_id=post_id, user_id=request.user.id)
            if userdislike.state == 0:
                userdislike.delete()
                Post.objects.filter(id=post_id).update(dislikes=(dislikeCount - 1))
            else:
                checkdislike.update(state=0)
                Post.objects.filter(id=post_id).update(dislikes=(dislikeCount + 1))
                Post.objects.filter(id=post_id).update(likes=(likeCount - 1))

        dislikedata = Post.objects.get(id=post_id)
        dislikedata.likes
        dislikedata.dislikes
        data = json.dumps({'likedata': dislikedata.likes, 'dislikedata': dislikedata.dislikes})
        return JsonResponse(data, safe=False)


def post_delete(request, post_id):
    if request.method == 'POST':
        postDel = Post.objects.get(id=post_id)
        postDel.delete()
        return HttpResponseRedirect('/blog/home')


# =================================authentication===============================
def login_form(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('home')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('home')
            else:
                message = "Sorry You are blocked from admin"
                context = {'message': message}
                return render(request, "login_form.html", context)
    return render(request, "login_form.html")

def register_form(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('home')

    if request.method == "POST":
        user_form = RegisterationForm(request.POST)
        if user_form.is_valid():
            checkEmail = User.objects.filter(email=request.POST['email'])
            if checkEmail.exists():
                message = "email already exsits please enter another one"
                return render(request ,"register_form.html" , {'email_error' :message })
            user_form.save()
            user = authenticate(username=user_form.cleaned_data['username'],
                                password=user_form.cleaned_data['password1'])
            login(request, user)
            return HttpResponseRedirect('home')
    else:
        user_form = RegisterationForm()
    return render(request, "register_form.html", {'form': user_form})


def user_logout(request):
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect('home')


# =================================Routes===========================================
def get_contact(request):
    return render(request, "contact.html")


def get_about(request):
    return render(request, "about.html")


# ==================================================================================
def addCat(request):
    form = CatForm()
    if request.method == "POST":
        form = CatForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/blog/home')
    return render(request, 'addcat.html', {'form': form})






def addcomment(request, user_id):
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/blog/details')
    return render(request, 'blog/details.html', {'form': form})


# def home(request):
#     all_post = Post.objects.all().order_by('-date')[:5]
#     all_cat = Category.objects.all()
#     all_post3 = Post.objects.order_by('-date')[:3]
#     return render(request, "index1.html", {"allpost": all_post, "allcat": all_cat, "allpost3": all_post3})


def update_post(request, pt_id):
    pt = Post.objects.get(id=pt_id)
    post_form = PostForm(instance=pt)

    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES, instance=pt)
        if post_form.is_valid():
            post_form.save()
            return HttpResponseRedirect('/blog/allposts_admin')
    context = {"form": post_form}
    return render(request, "addpost.html", context)


def update_word(request, wt_id):
    wt = Word.objects.get(id=wt_id)
    word_form = WordForm(instance=wt)

    if request.method == "POST":
        word_form = WordForm(request.POST, instance=wt)
        if word_form.is_valid():
            word_form.save()
            return HttpResponseRedirect('/blog/allwords_admin')
    context = {"words": word_form}
    return render(request, "newWords.html", context)


def allusers_admin(request):
    all_users = User.objects.all()
    context = {"allusers_admin": all_users}
    return render(request, 'allusers_admin.html', context)


def block(request, ut_id):
    ut = User.objects.get(id=ut_id)
    ut.is_active = 0
    ut.save()
    return HttpResponseRedirect('/blog/allusers_admin')


def unblock(request, ut_id):
    ut = User.objects.get(id=ut_id)
    ut.is_active = 1
    ut.save()
    # return HttpResponse("Deleted	")
    return HttpResponseRedirect('/blog/allusers_admin')


def promote(request, ut_id):
    ut = User.objects.get(id=ut_id)
    ut.is_superuser = 1
    ut.save()
    return HttpResponseRedirect('/blog/allusers_admin')


def unpromote(request, ut_id):
    ut = User.objects.get(id=ut_id)
    ut.is_superuser = 0
    ut.save()
    # return HttpResponse("Deleted	")
    return HttpResponseRedirect('/blog/allusers_admin')


def delete_user(request, ut_id):
    ut = User.objects.get(id=ut_id)
    ut.delete()
    # return HttpResponse("Deleted	")
    return HttpResponseRedirect('/blog/allusers_admin')


def allwords_admin(request):
    all_words = Word.objects.all()
    context = {"allwords_admin": all_words}
    return render(request, 'allwords_admin.html', context)


def addWords(request):
    word_form = WordForm()
    context = {"words": word_form}
    if request.method == "POST":
        word_form = WordForm(request.POST)
        if word_form.is_valid():
            word_form.save()
            return HttpResponseRedirect("/blog/allwords_admin")
    return render(request, "newWords.html", context)


def delete_word(request, wt_id):
    wt = Word.objects.get(id=wt_id)
    wt.delete()
    # return HttpResponse("Deleted	")
    return HttpResponseRedirect('/blog/allwords_admin')
