from django.urls import path #importing the path functions
from . import views #import view functions from current folder

#url configuration
urlpatterns = [
    path('test/', views.say_hello) #url path objects that receives the url, calls the function
]