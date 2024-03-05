from django.shortcuts import render
from django.http import HttpResponse

from .models import Surgeon
# Create your views here.
# view function: request -> response (request handler)

def say_hello(request):
    '''
    Testing View Function that is called at an url
    '''
    x=1
    y=2
    return render(request, 'hello.html', {
        'key': '1', 
        })


def index(request):
    '''
    View function displays calls template to display current surgeons
    Input:
        request (HTML request)
    Output:
        render() (HTML file): note 
    '''
    surgeonlst = [Surgeon("John Doe", "Sr"), Surgeon("Smith", "Sr")] #list of surgeons to be linked with database
    return render(request, 'index.html',{
        'Surgeons': [Surgeon("John Doe", "Sr"), Surgeon("Smith", "Sr")]
    })


"""
#login page at /schedule/login
def login(request):
    return HttpResponse('<h1> This is a login page </h1>')

#signup page at /schedule/signup
def signup(request):
    return HttpResponse('<h1> This is a signup page </h1>')
"""