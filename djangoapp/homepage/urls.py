from django.urls import path #importing the path functions
from . import views #import view functions from current folder

#url configuration
urlpatterns = [
    path('', views.home, name = "home"),
    path('base', views.base, name="base"),
    path('<int:id>',views.index,name='index')
]
