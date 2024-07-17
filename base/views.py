from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Task
from .forms import TopicForm, TaskForm

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
    topics = Topic.objects.filter(user = user)
    context = {'topics':topics}
    return render(request, 'base/home.html', context)

def createTopic(request):
    form = TopicForm()
    page = 'Create New Topic'
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic_form = form.save(commit=False)
            topic_form.user = request.user
            topic_form.title = request.POST.get('title').title()
            topic_form.description = request.POST.get('description')
            if request.POST.get('deadline'): 
                topic_form.deadline = request.POST.get('deadline')
            topic_form.save()
            return redirect('home')
        
    else:
        context = {'page':page,'form':form}
        return render(request, 'base/topic-form.html', context)

def taskListPage(request, topicId):
    topic = Topic.objects.get(id = topicId)
    tasks = Task.objects.filter(topic = topic)
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            new_task = Task.objects.create(
                title = title,
                user = request.user,
                topic = topic
            )
            return redirect('topic', topicId = topicId)

    context = {'topic':topic,'tasks':tasks}
    return render(request, 'base/topic-page.html', context)

def deleteTopic(request, topicId):
    topic = get_object_or_404(Topic, id=topicId)
    topic.delete()
    return redirect('home')

def deleteTask(request, taskId):
    task = Task.objects.filter(id=taskId)
    task.delete()
    return redirect(request.META.get('HTTP_REFERER'))

def taskCompleted(request, taskId):
    pass

def logoutUser(request):
    logout(request)
    return redirect('login')
