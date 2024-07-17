from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginRedirect, name = 'loginredirect'),
    path('login/', views.loginPage, name = 'login'),
    path('signup/', views.signupPage, name = 'signup'),
    path('home/', views.home, name = 'home'),
    path('newtopic/', views.createTopic, name = 'createtopic'),
    path('delete-topic/<str:topicId>/', views.deleteTopic, name = 'deletetopic'),
    path('topic/<str:topicId>', views.taskListPage, name = 'topic'),
    path('delete-task/<str:taskId>', views.deleteTask, name= 'deletetask'),
    path('task-completed/<str:taskId>', views.taskCompleted, name = 'taskcompleted'),
    path('logout/', views.logoutUser, name = 'logout'),
]
