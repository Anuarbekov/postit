from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Post


def index(request):
    return render(request, 'index.html')


def myposts(request):
    posts = Post.objects.filter(owner_id=request.user.id)
    return render(request, 'myposts.html', {'myposts': posts})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.warning(request, "Invalid inputs or account wasn't created")
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).first():
                messages.info(request, 'Username already exists')
                print('Username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=name)
                user.save()
                messages.success(request, 'Successfully registered!')
                return redirect('/login')
        else:
            messages.warning(request, "Passwords don't match, try again!")
            return redirect('/register')
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def addpost(request):
    return render(request, 'addpost.html')


def addingpost(request):
    title = request.POST['title']
    text = request.POST['text']
    owner = request.user
    post = Post.objects.create(title=title, text=text, owner=owner)
    post.save()
    messages.success(request, 'Successfully added post')
    return redirect('/')


def deletepost(request):
    posts = Post.objects.filter(owner_id=request.user.id)
    return render(request, 'deletepost.html', {'myposts': posts})


def deletingpost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        post = Post.objects.get(title=title)
        post.delete()
        messages.success(request, 'Successfully deleted post')
        return redirect('/')
    else:
        return redirect('/deletepost')