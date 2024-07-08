from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginRedirect, name = 'loginredirect'),
    path('login/', views.loginPage, name = 'login'),
    path('signup/', views.signupPage, name = 'signup'),
    path('home/', views.home, name = 'home'),
    path('newtopic/', views.createTopic, name = 'createtopic'),
    path('topic/<str:pk>', views.topicListPage, name = 'topiclist'),
    path('task/<str:pk>', views.taskDetail, name = 'tasks'),
    path('topic/<str:pk>', views.deleteTopic, name = 'deletetopic'),
    path('logout/', views.logoutUser, name = 'logout'),
]
