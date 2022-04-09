from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='main'),
    path('myposts', views.myposts, name='myposts'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('addpost', views.addpost, name='addpost'),
    path('addingpost', views.addingpost, name='addingpost'),
    path('deletepost', views.deletepost, name='deletepost'),
    path('deletingpost', views.deletingpost, name='deletingpost')
]
