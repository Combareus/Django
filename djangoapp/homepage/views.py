from django.shortcuts import render
from django.http import HttpResponse
from schedule.models import Surgeon
def base(request):
    '''
    Displays the base for all websites
    '''
    dict = {"name": "test name, should be accessing model though"}
    return render(request, 'homepage/base.html', dict)

def home(request):
    '''
    Displays homepage, using base template
    '''
    dict = {"name": "test name, should be accessing model though"} 
    return render(request, 'homepage/home.html', dict)
# Create your views here.



def index(request, id):
    '''
    Work on this later        
    '''
    return render(request, 'homepage/base.html', {"name": "test name, should be accessing model though"})

       