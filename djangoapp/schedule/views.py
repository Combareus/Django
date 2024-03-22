from django.shortcuts import render
from django.http import HttpResponse

from .models import Surgeon
# Create your views here.
# view function: request -> response (request handler)

def masterschedule(request):
    '''
    Testing View Function that is called at an url
    '''
    dict = {}
    Surgeons = [Surgeon(fullName = "John Smith", assignments = [], availability = [], exp = "Sr", qualifications = [])] #list of surgeon objects to be linked with database
    dict["surgeons"] = Surgeons
    return render(request, 'masterschedule.html', dict)

def appointment(request):
    '''
    Website to add scheduling stuff
    '''
    dict = {}
    surgeonlst = [Surgeon("John Doe", ["www"], ["www"], "Sr", ["www"]), Surgeon(fullName = "John Smith", assignments = [], availability = [], exp = "Sr", qualifications = [])] #list of surgeon objects to be linked with database
    dict["surgeons"] = surgeonlst
    return render(request, 'appointment.html', dict)


def index(request):
    '''
    View function displays calls template to display current surgeons
    Input:
        request (HTML request)
    Output:
        render() (HTML file): note 
    '''
    return render(request, 'index.html',{})


"""
#login page at /schedule/login
def login(request):
    return HttpResponse('<h1> This is a login page </h1>')

#signup page at /schedule/signup
def signup(request):
    return HttpResponse('<h1> This is a signup page </h1>')
"""