from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import RequestContext
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from core.models import Time, Employee, Surgeon, Cleaner, Patient, Surgery, Schedule


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
        
        appoint = [patientfname, patientlname, month, day, year, j1fname, j1lname, j2fname, j2lname]

        User.items.add(appoint)

        return redirect('personschedule')

    return render(request, "appointment.html")


class personschedule(TemplateView):
    template_name = 'personschedule.html'
    def post(self, request):
        days = []
        #days = [[surgery1, surgery2]], [surgery1, surgery2], [wendesday]...]
        #surgeries = []
        #month1 = 
        #day1 = 
        #year1 = 
        #month2 = 
        #day2 = 
        #year2 = 
        list1 = ["January", "March", "May", "July", "August", "October", "December"]
        list2 = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        days.append([])
        while month1 != month2 and year1 != year2 and day1 != day2:
            day1 += 1
            if day1 == 32:
                day1 = 1
                if list2.index(month1)+1 == 11:
                    year1 += 1
                    month1 = list2[0]
                else:
                    month1 = list2[list2.index(month1)+1]
            elif month1 not in list1 and day1 == 31:
                day1 = 1
                month1 = list2[list2.index(month1)+1]
            elif month1 == "February" and day1 == 30:
                day1 = 1
                month1 = list2[2]
            elif month1 == "February" and day1 == 29:
                if year1 % 4 == 0:
                    if year1 % 400 == 0:
                        pass
                    elif year1 % 100 == 0:
                        day1 = 1
                        month1 = list2[2]
                else:
                    day1 = 1
                    month1 = list2[2]
            days.append([])
        for x in days:
            #iterate across objects to make it days a 2d list here
            pass
        days_string = f''
        for x in days:
            #year = 
            #month = 
            #day = 
            dayofweek = datetime.datetime(year, month, day).weekday()
            if dayofweek == 0:
                dayofweek = "Monday"
            elif dayofweek == 1:
                dayofweek = "Tuesday"
            elif dayofweek == 2:
                dayofweek = "Wednesday"
            elif dayofweek == 3:
                dayofweek = "Thursday"
            elif dayofweek == 4:
                dayofweek = "Friday"
            elif dayofweek == 5:
                dayofweek = "Saturday"
            elif dayofweek == 6:
                dayofweek = "Sunday"
            appointments = f'<ul>'
            for y in x:
                #timestart = 
                #timeend = 
                #name = 
                appointments += f'<li class="cd-schedule__event"><a data-start="{timestart}" data-end="{timeend}"  data-content="event-sample" data-event="event-2" href = #0> <em class="cd-schedule__name">{name}</em></a></li>'
            appointments += '</ul>' 
            day_string = f'<li class="cd-schedule__group"><div class="cd-schedule__top-info"><span>{dayofweek}</span></div></li>'
            days_string += day_string
            
        schedule_string = f'<div class = "cd-schedule__events"><ul id = "days">{days_string}</ul></div>'
        return render(request, self.template_name, {schedule_string: schedule_string})

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