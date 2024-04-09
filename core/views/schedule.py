from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import RequestContext
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User



from ..models import Surgeon
# Create your views here.
# view function: request -> response (request handler)
class masterschedule(TemplateView):
    template_name = 'masterschedule.html'
    def post(self, request):
        '''
        Testing View Function that is called at an url
        '''
        dict = {}
        Surgeons = [Surgeon(fullName = "John Smith", assignments = [], availability = [], exp = "Sr", qualifications = [])] #list of surgeon objects to be linked with database
        dict["surgeons"] = Surgeons
        return render(request, self.template_name, dict)

def appointment(request):

    if request.method == "POST":
        patientfname = request.POST['fname']
        patientlname = request.POST['lname']
        cleanerfname = request.POST['cfname']
        cleanerlname = request.POST['clname']
        j1fname = request.POST['j1fname']
        j1lname = request.POST['j1lname']
        j2fname = request.POST['j2fname']
        j2lname = request.POST['j2lname']
        month = request.POST['Month']
        day = int(request.POST['Day'])
        year = int(request.POST['Year'])

        list1 = ["January", "March", "May", "July", "August", "October", "December"]

        if month not in list1 and day >= 31:
            messages.error(request, "Day Error: Invalid Date.")
            return redirect('appointment')
        elif month == "February" and day >= 30:
            messages.error(request, "Day Error: Invalid Date.")
            return redirect('appointment')
        elif month == "February" and day == 29:
            if year % 4 == 0:
                if year % 400 == 0:
                    pass
                elif year % 100 == 0:
                    messages.error(request, "Day Error: Invalid Date.")
                    return redirect('appointment')
            else:
                messages.error(request, "Day Error: Invalid Date.")
                return redirect('appointment')
        
        appoint = [patientfname, patientlname, month, day, year, cleanerfname, cleanerlname, j1fname, j1lname, j2fname, j2lname]

        #add appoint to something here

        return redirect('personschedule')

    return render(request, "appointment.html")


class personschedule(TemplateView):
    template_name = 'personschedule.html'
    def post(self, request):
        return render(request, self.template_name, {})

class index(TemplateView):
    template_name = 'index.html'
    def post(self, request):
        '''
        View function displays calls template to display current surgeons
        Input:
            request (HTML request)
        Output:
            render() (HTML file): note 
        '''
        return render(request, self.template_name,{})


"""
#login page at /schedule/login
def login(request):
    return HttpResponse('<h1> This is a login page </h1>')

#signup page at /schedule/signup
def signup(request):
    return HttpResponse('<h1> This is a signup page </h1>')
"""