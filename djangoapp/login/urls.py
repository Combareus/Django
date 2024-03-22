from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/signup', views.signup, name="signup"),
    path('login/signin', views.signin, name="signin"),
    path('login/signout', views.signout, name="signout"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),

]
