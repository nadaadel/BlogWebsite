from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterationForm

# Create your views here.
def get_home(request):

	return render(request, "home.html")

def user_logout(request):
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect('home')

def login_form(request):
    if request.user.is_authenticated():
       return HttpResponseRedirect('home')
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request ,user)
            return HttpResponse("Login success")
    return render(request, "login_form.html")

def register_form(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('home')
    if request.user.is_authenticated():
       return HttpResponse("You are Logged in")
    if request.method =="POST":
        user_form = RegisterationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect('home')
    else:
        user_form=RegisterationForm()
    return render(request, "register_form.html" , {'form':user_form})

# def register_form(request):
#     if request.user.is_authenticated():
#        return HttpResponse("You are Logged in")
#     if request.method =="POST":
#         user_form = UserCreationForm(request.POST)
#         if user_form.is_valid():
#             user_form.save()
#             username = user_form.cleaned_data.get('username')
#             password = user_form.cleaned_data.get('passsword')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return HttpResponseRedirect('home')
#     else:
#         user_form=UserCreationForm()
#     return render(request, "register_form.html" , {'form':user_form})