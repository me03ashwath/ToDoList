from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Task

def loginRedirect(request):
    return redirect('login') 

def loginPage(request):
    page = 'Login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'username not found')
        
        if authenticate(request, username = username, password = password) is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'password wrong')
    
    context = {'page': page}
    return render(request, 'base/login-signup.html', context)

def signupPage(request):
    request._messages._queued_messages.clear()

    page = 'SignUp'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        if username is not None and password is not None:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already exists')
            else:
                if password != re_password:
                    messages.error(request, 'passwords do not match')
                else:
                    try:
                        user = User.objects.create_user(username=username, password=password)
                        logout(request)
                        return redirect('login')
                    except:
                        messages.error(request, 'error occured during creating account')
            
    context = {'page':page}
    return render(request, 'base/login-signup.html', context)

def home(request):
    user = request.user
    # topics = Topics.object.get(owner = user.username)
    topics = ['trip', 'groceries', 'homework']

    context = {'topics':topics}
    return render(request, 'base/home.html', context)

def createTopic(request):
    pass

def topicListPage(request):
    pass

def taskDetail(request):
    pass

def deleteTopic(request):
    pass

def taskList(request):
    tasks = Task.objects.all()
    context ={'tasks' : tasks}   
    return render(request, 'base/home.html', context)

def taskDetail(request,pk):
    task = Task.objects.get(id = pk)
    context = {'task' : task} 
    return render(request, 'base/task.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
