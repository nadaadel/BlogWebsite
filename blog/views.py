from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import PostForm, TagForm, CommentForm, CatForm
from blog.models import Comment, Replay, Category, Post, Tag, Word, Category, Userlike
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterationForm
import json

#============================== home===============================
def home(request):
    context = allPosts(request)
    return render(request, "index.html", context)
def getCat(request):
    return render(request, "category.html")

def postshow(request):
    posts = Post.objects.get(author_id=request.POST['search_box'])
    return render(request, 'test.html', {'posts': posts})

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

#====================================post details ===================================
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
                return HttpResponseRedirect('/blog/single/%s'%post_id)
            elif 'commentBtn' in request.POST:
                textComment = request.POST['comment_text']
                words = request.POST['comment_text'].split()
                badwords = Word.objects.all()
                for word in words:
                    for wordobi in badwords:
                        if word == wordobi.word:
                            wordLen = len(word)
                            newWord = '*' * wordLen
                            textComment=textComment.replace(word ,newWord)

                # return HttpResponse(textComment)
                comment = Comment.objects.create(description=textComment,
                                                 post_id=post_id, user_id=request.user.id)
                comment.save()
                return HttpResponseRedirect('/blog/single/%s'%post_id)

    onePost = Post.objects.get(id=post_id)
    postAuthor = User.objects.get(id=onePost.author_id)
    all_comments = Comment.objects.filter(post_id=post_id)
    replay_comments = Replay.objects.all()
    tags = Tag.objects.filter(post_id=post_id)
    userLikes = Userlike.objects.filter(post_id = post_id , user_id=request.user.id)
    if not userLikes:
       context = {'post': onePost, 'postAuthor': postAuthor, 'allComments': all_comments, 'tags': tags,
               'replay_comments': replay_comments }
    else:
        userLikess = Userlike.objects.get(post_id=post_id, user_id=request.user.id)
        context = {'post': onePost, 'postAuthor': postAuthor, 'allComments': all_comments, 'tags': tags,
                   'replay_comments': replay_comments, 'userlike': userLikess}

    return render(request, "single.html", context)

#ajax like handel
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

#ajax dislike handle
def checkdisLike(request):
    if request.user.is_authenticated():
        post_id  = request.GET.get('postid')
        checkdislike = Userlike.objects.filter(post_id=post_id, user_id=request.user.id)
        onepost = Post.objects.get(id=post_id)
        dislikeCount = onepost.dislikes
        likeCount = onepost.likes
        if not checkdislike:
            userdisliked = Userlike.objects.create(state=0,
                                                  post_id=post_id, user_id=request.user.id)
            userdisliked.save()
            Post.objects.filter(id=post_id).update(dislikes=(dislikeCount + 1))
            check_count =  Post.objects.get(id=post_id)
            if check_count.dislikes == 10:
                check_count.delete()
                return HttpResponseRedirect('/blog/home')
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
        data = json.dumps({'likedata': dislikedata.likes,'dislikedata': dislikedata.dislikes})
        return JsonResponse(data, safe=False)

        #
        # post = Post.objects.get(id=post_id)
        # num = post.dislikes
        # if (num == 10):
        #     post.delete()
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



#=================================authentication===============================
def login_form(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('home')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            loginUser = User.objects.get(username=username)
            if loginUser.is_superuser == 1:
                return HttpResponseRedirect('admin')
            else:
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

def user_logout(request):
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect('home')


#=================================Routes===============================
def get_contact(request):
    return render(request, "contact.html")

def get_about(request):
    return render(request, "about.html")


