from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import RequestContext
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from core.models import Time, Employee, Surgeon, Cleaner, Patient, Surgery, Schedule
import datetime
from django.utils import timezone
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required


# Create your views here.
# view function: request -> response (request handler)
def get_surgery_info(request):
    surgery_id = request.GET.get('id')
    try:
        surgery = Surgery.objects.get(id=surgery_id)
        return JsonResponse({'patient': surgery.patient.fullName, 'time': surgery.time_period.timestart, 'info': surgery.info})
    except Surgery.DoesNotExist:
        return JsonResponse({'error': 'Surgery doesn\'t exist'})
    
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
class delete(TemplateView):
    template_name = 'delete.html'
    def post(self, request):
        surgery_id = request.POST['ID']
        try:
            surgery = Surgery.objects.get(id=surgery_id)
            surgery.delete()
            return redirect('personschedule')
        except Surgery.DoesNotExist:
            messages.error(request, "Error: Surgery with this ID does not exist.")
            return redirect('delete')
class appointment(TemplateView):
    template_name = 'appointment.html'
    
    def post(self, request):
        patientfname = request.POST['fname']
        patientlname = request.POST['lname']
        cleanerfname = request.POST['cfname']
        cleanerlname = request.POST['clname']
        jfname = request.POST['jfname']
        jlname = request.POST['jlname']
        sfname = request.POST['sfname']
        slname = request.POST['slname']

        
        month = datetime.datetime.strptime(request.POST['Month'], "%B").month #converts month string into int
        day = int(request.POST['Day'])
        year = int(request.POST['Year'])
        start = request.POST['StartTime']
        end = request.POST['EndTime']
        start_str = f"{day}-{month}-{year} {start}" #converts date and time into string
        #converts string into datetime object of the surgery start time
        start_obj = datetime.datetime.strptime(start_str, '%d-%m-%Y %H:%M') 
        end_str = f"{day}-{month}-{year} {end}" #converts date and time into string
        #converts string into datetime object of the surgery start time
        end_obj = datetime.datetime.strptime(end_str, '%d-%m-%Y %H:%M') 
        timeperiod = Time(timestart=timezone.make_aware(start_obj), timeend=timezone.make_aware(end_obj)) 
        
        
        list1 = [1, 3, 5, 7, 8, 10, 12]

        if month not in list1 and day >= 31:
            messages.error(request, "Day Error: Invalid Date.")
            return redirect('appointment')
        elif month == 2 and day >= 30:
            messages.error(request, "Day Error: Invalid Date.")
            return redirect('appointment')
        elif month == 2 and day == 29:
            if year % 4 == 0:
                if year % 400 == 0:
                    pass
                elif year % 100 == 0:
                    messages.error(request, "Day Error: Invalid Date.")
                    return redirect('appointment')
            else:
                messages.error(request, "Day Error: Invalid Date.")
                return redirect('appointment')
        
        

        try:
            earliest_surgery = Surgery.objects.earliest('time_period__timestart')
            latest_surgery = Surgery.objects.latest('time_period__timestart')
        except Surgery.DoesNotExist:
            earliest_surgery = None
            latest_surgery = None
        if earliest_surgery is not None and latest_surgery is not None:
            allsurgeries = get_surgeries(earliest_surgery.time_period.timestart.date(), latest_surgery.time_period.timestart.date()) #gets the surgeries to be displayed from date_1 to date_2, which are datetime() objects
            for x in allsurgeries:
                if x.time_period.timestart < timeperiod.timeend and timeperiod.timeend < x.time_period.timeend:
                    messages.error(request, "Time error: Overlap Detected")
                    return redirect('appointment')
                elif x.time_period.timestart < timeperiod.timestart and timeperiod.timestart < x.time_period.timeend:
                    messages.error(request, "Time error: Overlap Detected")
                    return redirect('appointment')
                elif timeperiod.timestart < x.time_period.timestart and x.time_period.timestart < timeperiod.timeend:
                    messages.error(request, "Time error: Overlap Detected")
                    return redirect('appointment')
                elif timeperiod.timestart < x.time_period.timeend and x.time_period.timeend < timeperiod.timeend:
                    messages.error(request, "Time error: Overlap Detected")
                    return redirect('appointment')
            if timeperiod.timestart > timeperiod.timeend:
                messages.error(request, "Time error: Overlap Detected")
                return redirect('appointment')
               
        timeperiod.save()
    
        j = Surgeon(fullName=jfname + " " + jlname, exp="Jr", qualifications="Qualified")
        j.save()
        j.availability.add(Time.objects.get(id=1))

        s = Surgeon(fullName=sfname + " " + slname, exp="Jr", qualifications="Qualified")
        s.save()
        s.availability.add(Time.objects.get(id=1))

        c = Cleaner(fullName=cleanerfname + " " + cleanerlname)
        c.save()
        c.availability.add(Time.objects.get(id=1))

        patient = Patient(fullName=patientfname + " " + patientlname)
        patient.save()

        surgery = Surgery.objects.create(patient=patient, time_period=timeperiod)
        surgery.save()
        surgery.surgeons.add(j)
        surgery.surgeons.add(s)
        surgery.cleaners.add(c) 
        
        print(surgery)



        return redirect('personschedule')

def followups(request):

    if request.method == "POST":
        patientfname = request.POST['fname']
        patientlname = request.POST['lname']
        surgfname = request.POST['surgfname']
        surglname = request.POST['surglname']
    
        month = datetime.datetime.strptime(request.POST['Month'], "%B").month #converts month string into int
        day = int(request.POST['Day'])
        year = int(request.POST['Year'])
        start = request.POST['StartTime']
        end = request.POST['EndTime']
        info = 'No notes for checkup'

        start_str = f"{day}-{month}-{year} {start}" #converts date and time into string
        #converts string into datetime object of the surgery start time
        start_obj = datetime.datetime.strptime(start_str, '%d-%m-%Y %H:%M') 
        end_str = f"{day}-{month}-{year} {end}" #converts date and time into string
        #converts string into datetime object of the surgery start time
        end_obj = datetime.datetime.strptime(end_str, '%d-%m-%Y %H:%M') 
        timeperiod = Time(timestart=timezone.make_aware(start_obj), timeend=timezone.make_aware(end_obj))
        timeperiod.save()

        

        
        list1 = [1, 3, 5, 7, 8, 10, 12]

        if month not in list1 and day >= 31:
            messages.error(request, "Day Error: Invalid Date.")
            return redirect('appointment')
        elif month == 2 and day >= 30:
            messages.error(request, "Day Error: Invalid Date.")
            return redirect('appointment')
        elif month == 2 and day == 29:
            if year % 4 == 0:
                if year % 400 == 0:
                    pass
                elif year % 100 == 0:
                    messages.error(request, "Day Error: Invalid Date.")
                    return redirect('appointment')
            else:
                messages.error(request, "Day Error: Invalid Date.")
                return redirect('appointment')      

        surg = Surgeon(fullName=surgfname + " " + surglname, exp="Jr", qualifications="Q2")
        surg.save()
        surg.availability.add(Time.objects.get(id=1))


        patient = Patient(fullName=patientfname + " " + patientlname)
        patient.save()

        surgery = Surgery.objects.create(patient=patient, time_period=timeperiod, info=info)
        surgery.save()
        surgery.surgeons.add(surg)
        print(surgery)

        return redirect('personschedule')

    return render(request, "followups.html")


class personschedule(TemplateView):
    template_name = 'personschedule.html'
    template_2 = 'event-sample.html'
    def get(self, request):
        '''
        View function displays calls template to display schedule
        Input:
            request (HTML request)
        Output:
            render() (HTML file): note 
        '''
        days = [[]]
        

        surgeries = list(Surgery.objects.all())
        try:
            earliest_surgery = Surgery.objects.earliest('time_period__timestart')
            latest_surgery = Surgery.objects.latest('time_period__timestart')
        except Surgery.DoesNotExist:
            earliest_surgery = None
            latest_surgery = None
        if earliest_surgery is not None and latest_surgery is not None:
            allsurgeries = get_surgeries(earliest_surgery.time_period.timestart.date(), latest_surgery.time_period.timestart.date())
        else:
            allsurgeries = []


        """
        other option for display - displays earliest to latest - prob won't use this
        month1 = earliest_surgery.time_period.timestart.month #retruns 1,2,3,...,12
        day1 = earliest_surgery.time_period.timestart.day #returns int
        year1 = earliest_surgery.time_period.timestart.year #returns 2024
        month2 = latest_surgery.time_period.timestart.month
        day2 = latest_surgery.time_period.timestart.day
        year2 = latest_surgery.time_period.timestart.year
        """


        today = datetime.datetime.today()
        month1 = today.month
        day1 = today.day
        year1 = today.year
        month2 = today.month
        day2 = today.day
        year2 = today.year
        
        list1 = [1, 3, 5, 7, 8, 10, 12]
        list2 = [x for x in range(1, 13)]
        days = [] #list of surgery objects within seven days
        daytracker = []
        for _ in range(7):
            days.append([])
            daytracker.append([month2, day2, year2])
            day2 += 1
            if day2 == 32:
                day2 = 1
                if list2.index(month2) == 11:
                    year2 += 1
                    month2 = 1
                else:
                    month1 += 1
            elif month2 not in list1 and day2 == 31:
                day2 = 1
                month2 += 1
            elif month2 == 2 and day2 == 30:
                day2 = 1
                month2 = 3
            elif month2 == 2 and day2 == 29:
                if year2 % 4 == 0:
                    if year2 % 400 == 0:
                        pass
                    elif year2 % 100 == 0:
                        day2 = 1
                        month2 = 3
                else:
                    day2 = 1
                    month2 = 3
        daytracker.append([month2, day2, year2])
        
        teststring = f'{month1}{day1}{year1}'
        teststring2 = f'{month2}{day2}{year2}'
        result = request.GET.get('result', None)
        teststring3 = f'{result}'
        #days is now [[],[],[],[], ...]
        #daytracker is now [[firstday], [secondday], ...]

        #fills days
        for x in allsurgeries:
            month = x.time_period.timestart.month
            day = x.time_period.timestart.day
            year = x.time_period.timestart.year
            try:
                ind = daytracker.index([month, day, year])
                days[ind].append(x)
                teststring += f' {month}{day}{year}'
            except ValueError:
                #if its not in the list just pass and go next 
                continue 
        #fills days_string
        days_string = f''
        for x in range(7):

            #get the day of the week
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
                a = int(y.time_period.timestart.hour)
                if a < 10:
                    a = f"0{a}"
                b = int(y.time_period.timestart.minute)
                if b < 10:
                    b = f"0{b}"
                c = int(y.time_period.timeend.hour)
                if c < 10:
                    c = f"0{c}"
                d = int(y.time_period.timeend.minute)
                if d < 10:
                    d = f"0{d}"
                timestart = f"{a}:{b}"
                timeend = f"{c}:{d}"
                patient = y.patient
                patientname = patient.fullName 
                name = f"Surgery for {patientname}"
                appointments += f'<li class="cd-schedule__event"><a data-start="{timestart}" data-end="{timeend}"  data-content="event-sample" data-event="event-2" href = "event-sample.html"> <em class="cd-schedule__name">{name}</em></a></li>'
            appointments += '</ul>' 
            day_string = f'<li class="cd-schedule__group"><div class="cd-schedule__top-info"><span>{dayofweek}</span></div><ul>'
            day_string += appointments
            day_string += '</ul></li>'
            days_string += day_string
        
        #the big string :)
        schedule_string = f'<div class = "cd-schedule__events"><ul>{days_string}</ul></div>'
        print(schedule_string)
        return render(request, self.template_name,
                      {"schedule_string": schedule_string, 
                       "teststring":teststring, 
                       "teststring2":teststring2, 
                       "teststring3":teststring3, 
                       "day_string":day_string, 
                       "days_string":days_string,
                       "template_2":self.template_2}
                       )

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

class archive(TemplateView):
    template_name = 'archive.html'
    today = datetime.datetime.today()
    day = today.day
    month = today.month
    year = today.year
    def post(self, request):
        self.month = datetime.datetime.strptime(request.POST['Month'], "%B").month #converts month string into int
        self.day = int(request.POST['Day'])
        self.year = int(request.POST['Year'])
        return archive.get(self, request)

    def get(self, request):
        dayofweek = 0
        try:
            earliest_surgery = Surgery.objects.earliest('time_period__timestart')
            latest_surgery = Surgery.objects.latest('time_period__timestart')
        except Surgery.DoesNotExist:
            earliest_surgery = None
            latest_surgery = None
        if earliest_surgery is not None and latest_surgery is not None:
            allsurgeries = get_surgeries(earliest_surgery.time_period.timestart.date(), latest_surgery.time_period.timestart.date())
        else:
            allsurgeries = []
        display_surgeries = [] #list of surgery objects on the display date
        for x in allsurgeries:
            month = x.time_period.timestart.month
            day = x.time_period.timestart.day
            year = x.time_period.timestart.year
            if [month, day, year] == [self.month, self.day, self.year]:
                display_surgeries.append(x)
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
        days_string = f''        

        appointments = f'<ul>'
        for x in display_surgeries:
            a = int(x.time_period.timestart.hour)
            if a < 10:
                a = f"0{a}"
            b = int(x.time_period.timestart.minute)
            if b < 10:
                b = f"0{b}"
            c = int(x.time_period.timeend.hour)
            if c < 10:
                c = f"0{c}"
            d = int(x.time_period.timeend.minute)
            if d < 10:
                d = f"0{d}"
            timestart = f"{a}:{b}"
            timeend = f"{c}:{d}"
            patient = x.patient
            patientname = patient.fullName 
            name = f"Surgery for {patientname}"
            appointments += f'<li class="cd-schedule__event"><a data-start="{timestart}" data-end="{timeend}"  data-content="event-sample" data-event="event-2" href="event-sample.html"> <em class="cd-schedule__name">{name}</em></a></li>'
        appointments += '</ul>' 
        day_string = f'<li class="cd-schedule__group"><div class="cd-schedule__top-info"><span>{dayofweek}</span></div><ul>'
        day_string += appointments
        day_string += '</ul></li>'
        days_string += day_string
    
        #the big string :)
        #<li class="cd-schedule__group"><div class="cd-schedule__top-info"><span></span></div><ul></ul></li>
        schedule_string = f'<div class = "cd-schedule__events"><ul><li class="cd-schedule__group"><div class="cd-schedule__top-info"><span></span></div><ul></ul></li><li class="cd-schedule__group"><div class="cd-schedule__top-info"><span></span></div><ul></ul></li>{days_string}<li class="cd-schedule__group"><div class="cd-schedule__top-info"><span></span></div><ul></ul></li><li class="cd-schedule__group"><div class="cd-schedule__top-info"><span></span></div><ul></ul></li></ul></div>'
        title = f'All Surgeries for {self.day}/{self.month}/{self.year} (dd/mm/yyyy)'
        return render(request, self.template_name, {"schedule_string":schedule_string, "title":title})
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class eventsample(TemplateView):
    result = "lolol"
    def get(self, request):
        if is_ajax(request = request):
            self.result = request.GET.get('arr')
            data = {}
            return JsonResponse(data)
        else:
            print(request)
        return render(request, "event-sample.html", {'info':self.result})
#commentee
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