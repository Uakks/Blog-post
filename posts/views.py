from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Post
from .dboperations import *


# Create your views here.
def index(request):
    posts = Post.objects.order_by('created_at')
    return render(request, 'index.html', {'posts': posts})


def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'post.html', {'posts': posts})


def newpost(request):
    user = request.user
    if request.POST.get('title') is not None and request.POST.get('content') is not None:
        new_post(request.POST['title'], request.POST['content'], str(user))
        return HttpResponseRedirect('/')
    return render(request, 'newpost.html')


def deletepost(request, pk):
    user = request.user.id
    post_id = Post.objects.get(id=pk)
    if user is not None:
        if request.method == 'POST':
            post_id.delete()
            return render(request, 'deletepost.html')
    else:
        messages.info(request, "Authorize first to delete")
        return redirect('/post/{pk}'.format(pk=pk))


def editpost(request, pk):
    current_post = Post.objects.get(id=pk)
    if request.POST.get('title') is not None and request.POST.get('content') is not None:
        update_posts(request.POST['title'], request.POST['content'], current_post.id)
        return HttpResponseRedirect(f"/post/{current_post.id}")
    return render(request, 'editpost.html', {'current_post': current_post})


def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already registered")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken, choose another one")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password,
                                                first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Passwords does not match")
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def profile(request, pk):
    user = User.objects.get(pk=pk)
    posts = Post.objects.filter(username=user).order_by('created_at')
    return render(request, 'profile.html', {'user': user, 'posts': posts})
