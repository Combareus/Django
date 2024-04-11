from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import RequestContext
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from core.models import Time, Employee, Surgeon, Cleaner, Patient, Surgery, Schedule
import datetime


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
        start = request.POST['StartTime']
        end = request.POST['EndTime']

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
        timeperiod = Time(timestart=start, timeend=end)

        j1 = Surgeon(fullName=j1fname + " " + j1lname, exp="Jr", qualifications="Q1")
        j1.save()
        j1.availability.add(Time.objects.get(id=1))

        j2 = Surgeon(fullName=j2fname + " " + j2lname, exp="Jr", qualifications="Q2")
        j2.save()
        j2.availability.add(Time.objects.get(id=1))

        c = Cleaner(fullName=cleanerfname + " " + cleanerlname)
        c.save()
        c.availability.set(Time.objects.get(id=1))

        patient = Patient(fullName=patientfname + " " + patientlname)
        patient.save()

        surgery = Surgery.objects.create(patient=patient, time_period=timeperiod, cleaners=c)
        surgery.save()
        surgery.surgeons.add([j1, j2])


        User.items.add(appoint)

        return redirect('personschedule')

    return render(request, "appointment.html")


class personschedule(TemplateView):
    template_name = 'personschedule.html'
    def post(self, request):
        '''
        View function displays calls template to display schedule
        Input:
            request (HTML request)
        Output:
            render() (HTML file): note 
        '''
        days = [[]]
        
        surgeries = list(Surgery.objects.all())
        earliest_surgery = Surgery.objects.earliest('time_period__timestart')
        latest_surgery = Surgery.objects.latest('time_period__timestart')
        
        patient = earliest_surgery.patient
        patientname = patient.full_name 
        #patient name

        month1 = earliest_surgery.timestart.month #retruns 1,2,3,...,12
        day1 = earliest_surgery.timestart.day #returns int
        year1 = earliest_surgery.timestart.year #returns 2024
        month2 = latest_surgery.timestart.month
        day2 = latest_surgery.timestart.day
        year2 = latest_surgery.timestart.year
        allsurgeries = get_surgeries(earliest_surgery.timestart, latest_surgery.timestart) #gets the surgeries to be displayed from date_1 to date_2, which are datetime() objects
        
        list1 = [1, 3, 5, 7, 8, 10, 12]
        list2 = [x for x in range(1, 13)]
        daytracker = []
        while month1 != month2 and year1 != year2 and day1 != day2:
            daytracker.append([month1, day1, year1])
            day1 += 1
            if day1 == 32:
                day1 = 1
                if list2.index(month1)+1 == 11:
                    year1 += 1
                    month1 = 1
                else:
                    month1 += 1
            elif month1 not in list1 and day1 == 31:
                day1 = 1
                month1 += 1
            elif month1 == 2 and day1 == 30:
                day1 = 1
                month1 = 3
            elif month1 == 2 and day1 == 29:
                if year1 % 4 == 0:
                    if year1 % 400 == 0:
                        pass
                    elif year1 % 100 == 0:
                        day1 = 1
                        month1 = 3
                else:
                    day1 = 1
                    month1 = 3
            days.append([])
        daytracker.append([month2, day2, year2])
        #days is now [[],[],[],[], ...]
        #daytracker is now [[firstday], [secondday], ...]

        #fills days
        for x in allsurgeries:
            month = x.timestart.month
            day = x.timestart.day
            year = x.timestart.year
            ind = daytracker.index([month, day, year])
            days[ind].append(x)
        
        #fills days_string
        days_string = f''
        for x in range(len(days)):
            year = daytracker[x][2]
            month = daytracker[x][0]
            day = daytracker[x][1]
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
            for y in days[x]:
                timestart = f"{y.timestart.hour}:{y.timestart.minute}"
                timeend = f"{y.timestart.hour}:{y.timestart.minute}"

                patient = earliest_surgery.patient
                patientname = patient.full_name 
                name = f"Surgery for {patientname}"
                appointments += f'<li class="cd-schedule__event"><a data-start="{timestart}" data-end="{timeend}"  data-content="event-sample" data-event="event-2" href = #0> <em class="cd-schedule__name">{name}</em></a></li>'
            appointments += '</ul>' 
            day_string = f'<li class="cd-schedule__group"><div class="cd-schedule__top-info"><span>{dayofweek}</span></div></li>'
            days_string += day_string
        
        #the big string :)
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

def get_surgeries(date_1, date_2):
	'''
	Returns all surgery objects with a start date between date_1 and date_2
	date_1, date_2 - date objects, ex: datetime.now().date()
	'''
	surgeries = Surgery.objects.all()
	filtered_surgeries = []
	for surgery in surgeries:
		if surgery.date() >= date_1 and surgery.date() <= date_2:
			filtered_surgeries.append(surgery)
	return filtered_surgeries