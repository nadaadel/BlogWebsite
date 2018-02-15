from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import PostForm, TagForm, CommentForm, CatForm
from blog.models import Comment, Replay, Category, Post, Tag, Word, Category
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterationForm


# from django.views.generric import ListView


def allPosts(request):
    all_post = Post.objects.all()[:5]
    context = {"allpost": all_post}
    return context


def addPost(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/blog/home')
    return render(request, 'addpost.html', {'form': form})


def get_post(request, post_id):
    if request.user.is_authenticated():
        if request.method == "POST":
            if 'replyBtn' in request.POST:
               replay =Replay.objects.create(description = request.POST['replay_text'] ,
                                          comment_id = request.POST['comment_id'], user_id =request.user.id)
               replay.save()
               return HttpResponseRedirect('blog/single/1')
            if 'commentBtn' in request.POST:
                comment = Comment.objects.create(description=request.POST['comment_text'],
                                                 post_id=post_id, user_id=2)
                comment.save()
                return HttpResponseRedirect('/blog/single/1')

            # if request.POST['replyBtn']:
            #    replay = Replay.objects.create(description=request.POST['replay_text'],
            #                                    comment_id=request.POST['comment_id'], user_id=1)
            #    replay.save()
            #    return HttpResponseRedirect('blog/single/1')



    onePost = Post.objects.get(id=post_id)
    postAuthor = User.objects.get(id=onePost.author_id)
    all_comments = Comment.objects.filter(post_id=post_id)
    replay_comments = Replay.objects.all()
    tags = Tag.objects.filter(post_id =post_id)
    context = {'post': onePost, 'postAuthor': postAuthor, 'allComments': all_comments , 'tags' :tags , 'replay_comments' : replay_comments}
    return render(request, "single.html", context)


def addCat(request):
    form = CatForm()
    if request.method == "POST":
        form = CatForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/blog/home')
    return render(request, 'addcat.html', {'form': form})


def addTag(request):
    form = TagForm()
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/blog/home')
    return render(request, 'blog/addpost.html', {'form': form})


def postshow(request):
    posts = Post.objects.get(author_id=request.POST['search_box'])
    return render(request, 'test.html', {'posts': posts})


def allComment(request, post_id):
    all_comments = Comment.objects.all(post_id)
    context = {"allposts": all_comments}
    return render(request, "post/details.html", context)


def addTag(request):
    form = TagForm()
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/blog/home')
    return render(request, 'blog/addpost.html', {'form': form})


def addcomment(request, user_id):
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/blog/details')
    return render(request, 'blog/details.html', {'form': form})


# Ajax Request
def like(request):
    return HttpResponse("likea")
    likes = request.GET.get('likecount', None)
    data = {
        'test': 'in views'
    }
    if data['test']:
        data['error_message'] = 'i am here nada'
    return JsonResponse(data)
    post = Post.objects.get(id=1)
    if request.method == "POST":
        post.likes += 1
        post.update()


def checkdislike(request, post_id):
    post = Post.objects.get(id=post_id)
    num = post.dislikes
    if (num == 10):
        post.delete()


def get_home(request):
    return render(request, "index.html")


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
            return HttpResponseRedirect('home')
    return render(request, "login_form.html")


def register_form(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('home')

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
