from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginRedirect, name = 'loginredirect'),
    path('login/', views.loginPage, name = 'login'),
    path('signup/', views.signupPage, name = 'signup'),
    path('home/', views.home, name = 'home'),
    path('newtopic/', views.createTopic, name = 'createtopic'),
    path('topic/<str:topicId>', views.topicListPage, name = 'topic'),
    path('delete-topic/<str:topicId>/', views.deleteTopic, name = 'deletetopic'),
    path('logout/', views.logoutUser, name = 'logout'),
]
