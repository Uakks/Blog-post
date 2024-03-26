from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:pk>', views.post, name='post'),
    path('newpost', views.newpost, name='newpost'),
    path('post/<str:pk>/editpost', views.editpost, name='editpost'),
    path('post/<str:pk>/deletepost', views.deletepost, name='deletepost'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile/<str:pk>', views.profile, name='profile')
]
