from django.db import models
# Create your models here.
"""
Classes for scheduling, employees (including surgeons, cleaner), patients.
Time, Employee, Surgeon, Cleaner, Patient, Surgery, Schedule
Progress: 
1/24/2024 - Classes for people created and initialized Lines: 180
1/30/2024 - Classes for schedule created, some validation done Lines: 309
2/06/2024 - Occupy and Conflict functions created Lines: 385
2/06/2024 to 2/22/2024 - minor levels of cooking Lines: 417
2/28/2024 - Changed intializes, added strings for all Lines: 447
4/07 - Changed the class styling to have Django fields from regular python properties
"""
class Time(models.Model):
	timestart = models.DateTimeField()
	timeend = models.DateTimeField()
	def __str__(self):
		return f"Start: {self.timestart} End: {self.timeend}"
	def conflict(self, timeobject):
		"""
		Determines if there is a conflict with another time object
		Attributes
			self (time)
			timeobject (time)
		Returns
			True - There is a conflict
			False - There is no conflict
		"""
		if self.timestart < timeobject.timeend and self.timeend > timeobject.timestart:
			return True
		else:
			return False

class Employee(models.Model):
	# def __init__(self, fullName, assignments, availability, *args, **kwargs):
	# 	"""
	# 	Initializes class
	# 	Attributes
	# 		fullName (str): fullname of person
	# 		Availability (2d lists with ints) - [[timestart, timeend], ...] - time open
	# 		Assignments (2d lists with ints) - [[timestart, timeend, patient], ...] - their assignments
	# 		sched (3d list with ints (7x_)) - [[[timestart, timeend], [timestart, timeend], [timestart, timeend], ...]*7] list of regular times available throughout week 
	# 	"""
	# 	super().__init__(*args, **kwargs)
	# 	self._fullName = fullName
	# 	self._availability = availability
	# 	self._assignments = assignments

	fullName = models.CharField(max_length=100)
	availability = models.ManyToManyField(Time, related_name='available_employees')
	sched = models.ManyToManyField(Time, related_name='scheduled_employees')

	def __str__(self):
		"""
		String (representation of employee)
		"""
		return f"Type: Employee \nName: {self._fullName}\n\n"
	# @property 
	# def fullName(self):
	# 	"""Getter for fullName"""
	# 	return self._fullName

	# @property 
	# def availability(self):
	# 	"""Getter for availability"""
	# 	return self._availability

	# @property 
	# def assignments(self):
	# 	"""Getter for availability"""
	# 	return self._assignments

	# @fullName.setter
	# def fullName(self, n):
	# 	"""
	# 	Setter for fullName
	# 	Attributes
	# 			self (person)
	# 			n (str) - name that needs validation
	# 	"""
	# 	while not (isinstance(n, str) and len(n) > 0):
	# 			n = input("Invalid name, try again: ")
	# 	self._fullName = n

	# @availability.setter
	# def availability(self, avail):
	# 	"""
	# 	Setter for availability
	# 	Attributes
	# 			self (person)
	# 			avail (2d list)
	# 	"""
	# 	self._availability = avail

	# @assignments.setter
	# def assignments(self, assign):
	# 	"""
	# 	Setter for availability
	# 	Attributes
	# 			self (person)
	# 			avail (2d list)
	# 	"""
	# 	self._assignments = assign

		
	# def conflict(self, timestart, timeend):
	# 	"""
	# 	Determines if employee is available from timestart to timeend
	# 	Attributes
	# 		Self (person)
	# 		timestart (1d list of ints: [year, month, day, hour, minute])
	# 		timeend (1d list of ints: [year, month, day, hour, minute])

	# 	Returns
	# 		False - There is a conflict
	# 		index - index of availability in self._availability 
	# 	"""
	# 	for x in self._availability:
	# 		#if the day of the conflict is less than the day of we're checking, break (availability is ordered (i hope))
	# 		if timestart[2] < x[2]:
	# 			break
				
	# 		#if the start of shift is less than the start of assignment
	# 		if timestart[0] >= x[0] and timestart[1] >= x[1] and timestart[2] >= x[2] and timestart[3] >= x[3] and timestart[4] >= x[4]:

	# 			#if the end of the assignment is less than the end of shift
	# 			if timeend[0] <= x[5] and timeend[1] <= x[6] and timeend[2] <= x[7] and timeend[3] <= x[8] and timeend[4] <= x[9]:
					
	# 				#we found an open slot
	# 				return self._availability.index(x)
	# 	return False
		
	# def assign(self, timestart, timeend):
	# 	"""
	# 	Give assignment to person and change their availability and assignments
	# 	Attributes
	# 		Self (person)
	# 		timestart (1d list of ints) - start of assignment
	# 		timeend (1d list of ints) - end of assignment

	# 	Returns
	# 		True - Operation could be done
	# 		False - Operation could not be done
	# 	"""
	# 	#store res of the conflict operation
	# 	res = self.conflict(timestart, timeend)
	# 	if res == False:
	# 		#Assignment could not be assigned
	# 		return False
	# 	else:
	# 		#create a new timeslot for them
	# 		temp = []
	# 		for x in range(5):
	# 			temp.append(timeend[x])
	# 		for x in range(5, 10):
	# 			temp.append(self._availability[res][x])
	# 			#change the available timeslot so they are unavailable at that time
	# 			self._availability[res][x] = timestart[x-5]
	# 		#add temp to availability
	# 		self._availability.insert(res+1, temp)
			
	# 		return True


class Surgeon(Employee):
	# def __init__(self, fullName, assignments, availability, exp, qualifications):
	# 	"""
	# 	Initializes class
	# 	Attributes
	# 		fullName (str): fullname of person
	# 		assigments (2d list of ints): time periods of assigment 
	# 		availability (2d list of ints): availability of surgeon
	# 		Qualifications (list of strings): list of genre of surgeries surgeon can perform
	# 		exp (str): Senior or Junior ("Sr" or "Jr")
	# 	"""
	# 	super(Employee, self).__init__()
	# 	self._fullName = fullName
	# 	self._assignments = assignments
	# 	self._availability = availability
	# 	self._qualifications = qualifications
	# 	self._exp = exp
	
	qualifications = models.CharField(max_length=100)
	exp = models.CharField(max_length=2)


	def __str__(self):
		"""
		String (for testing printing)
		"""
		return f"Surgeon Name: {self.fullName} \nExperience: {self.exp}\n\n"
	# def test(self):
	# 	"""
	# 	(for testing printing)
	# 	"""
	# 	return f"Type: Surgeon \nName: {self._fullName} \nExperience: {self._exp}\n\n"
	# @property
	# def qualifications(self):
	# 	"""Getter for qualifications"""
	# 	return self._qualifications

	# @property
	# def exp(self):
	# 	"""Getter for exp"""
	# 	return self._exp

	# @qualifications.setter
	# def qualifications(self, quals):
	# 	"""
	# 	Setter for qualifications
	# 	Attributes
	# 		self (Surgeon)
	# 		qual (list)
	# 	"""
	# 	self._qualifications = quals

	# @exp.setter
	# def exp(self, title):
	# 	"""
	# 	Setter for exp
	# 	Attributes
	# 		self (surgeon)
	# 		title (str)
	# 	"""
	# 	self._exp = title

	def qualcheck(self, type, title):
		if title == "Sr":
			if self.exp == "Jr":
				return False
		if type not in self.qualifications:
			return False
		return True

		
	def assignsurgeon(self, type, title, timestart, timeend):
		"""
		Give assignment to surgeon and change their availability and assignments
		Note: This is DIFFERENT than assigning a regular employee
		Attributes
			Self (surgeon)
			type - Surgery type
			title - title required (jr or sr)
			timestart (1d list of ints) - start of assignment
			timeend (1d list of ints) - end of assignment

		Returns
			True - Operation could be done
			False - Operation could not be done
		"""
		#if the surgeon does not have the necessary credentials
		if self.qualcheck(self, type, title) == False:
			return False
		else:
			#otherwise assign - this doesnt necessarily return True, if there is a conflict it will return False in self.conflict()
			self.assign(self, timestart, timeend)
			return True
	

class Cleaner(Employee):
	# def __init__(self, fullName, assignments = [], availability = []):
	# 	"""
	# 	Initializes class
	# 	Attributes
	# 		fullName (str): fullname of person
	# 		Availability (2d lists with ints) - [[timestart, timeend], ...] 
	# 	"""
	# 	super(Employee, self).__init__()
	# 	self._fullName = fullName
	# 	self._assignments = assignments
	# 	self._availability = availability
		
	def __str__(self):
		"""
		String (for testing printing)
		"""
		return f"Cleaner Name: {self.fullName}\n"

class Patient(models.Model):
	# def __init__(self, fullName, conditionType, severity, admissionDate, status, *args, **kwargs):
	# 	"""
	# 	Initializes class
	# 	Attributes
	# 		fullName (str): fullname of person
	# 		conditionType (str): type of surgery needed
	# 		severity (int): severity on a scale of 1 to 100
	# 		admissionDate (list of int): DD, MM, YYYY
	# 		status (string): "unscheduled" or "scheduled"
	# 	"""
	# 	super(models.Model, self).__init__(self, *args, **kwargs)
	# 	self._fullName = fullName
	# 	self._conditionType = conditionType
	# 	self._severity = severity
	# 	self._admissionDate = admissionDate
	# 	self._status = status
	fullName = models.CharField(max_length=255)
	condition_type = models.CharField(max_length=255, null=True)
	severity = models.CharField(max_length=255, null=True)
	admission_date = models.DateField(null=True)
	status = models.CharField(max_length=255, null=True)

	def __str__(self):
		"""
		String (for testing printing)
		"""
		return f"Patient Name: {self.fullName} \nCondition Type: {self.condition_type} \nSeverity: {self.severity}\n\n"

	# @property 
	# def fullName(self):
	# 	"""Getter for fullName"""
	# 	return self._fullName

	# @property
	# def conditionType(self):
	# 	"""Getter for conditionType"""
	# 	return self._conditionType

	# @property
	# def severity(self):
	# 	"""Getter for severity"""
	# 	return self._severity
	
	# @property
	# def admissionDate(self):
	# 	"""Getter for AdmissionType"""
	# 	return self._admissionDate

	# @property
	# def status(self):
	# 	"""Getter for status"""
	# 	return self._status

	# @fullName.setter
	# def fullName(self, n):
	# 	"""
	# 	Setter for fullName
	# 	Attributes
	# 		self (person)
	# 		n (str) - name that needs validation
	# 	"""
	# 	while not (isinstance(n, str) and len(n) > 0):
	# 			n = input("Invalid name, try again: ")
	# 	self._fullName = n

	# @conditionType.setter
	# def conditionType(self, type):
	# 	"""
	# 	Setter for conditionType
	# 	Attributes
	# 		self (patient)
	# 		type (str)
	# """
	# 	self._conditionType = type

	# @severity.setter
	# def severity(self, n):
	# 	"""
	# 	Setter for severity
	# 	Attributes
	# 		self (patient)
	# 		n (int)
	# 	"""
	# 	self._severity = n

	# @admissionDate.setter
	# def admissionDate(self, n):
	# 	"""
	# 	Setter for admissionDate
	# 	Attributes
	# 		self (patient)
	# 		n (list)
	# 	"""
	# 	self._admissionDate = n

	# @status.setter
	# def status (self, status):
	# 	"""
	# 	Setter for status
	# 	Attributes
	# 		self (patient)
	# 		status (status)
	# 	"""
	# 	self._status = status
 
class Surgery(models.Model):
	"""
	Class for a specific Surgery
	Attributes
		surgeons
		cleaners
		patient
		time
	"""
	surgeons = models.ManyToManyField(Surgeon)
	cleaners = models.ManyToManyField(Cleaner)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	time_period = models.ForeignKey(Time, on_delete=models.CASCADE) 
	def date(self):
		'''
		Returns date of surgery
		'''
		return self.time_period.timestart.date()

	def __str__(self):
		s1 = ''
		s2 = ''
		for surgeon in self.surgeons.all():
			s1 += str(surgeon) 
		for cleaner in self.cleaners.all():
			s2 += str(cleaner) 
		return f"Surgeons:\n {s1} \nCleaners: \n{s2} \nPatient: \n{self.patient} {self.time_period}\n\n"
	



class Schedule(models.Model):
	# def __init__(self, year, month, day, hour = 0, minute = 0, surgeries = [], *args, **kwargs):
	# 	"""
	# 	Initializes class
	# 	Attributes
	# 		year (int)
	# 		month (int)
	# 		day (int)
	# 		hour (int)
	# 		minute (int)
	# 		surgeries (3d list) [[[surgeons], [cleaners], patient, [time]], [], ...]
	# 	"""
	# 	super(models.Model, self).__init__(self, *args, **kwargs)
	# 	self._year = year
	# 	self._month = month
	# 	self._day = day
	# 	self._hour = hour
	# 	self._minute = minute
	# 	self._surgeries = surgeries

	# 	self.year = year
	# 	self.month = month
	# 	self.day = day
	# 	self.hour = hour
	# 	self.minute = minute
	# 	self.surgeries = surgeries
	# year = models.IntegerField()
	# month = models.IntegerField()
	# day = models.IntegerField()
	# hour = models.IntegerField(default=0)
	# minute = models.IntegerField(default=0)
	time = models.DateTimeField()
	surgeries = models.ManyToManyField(Surgery)

	# @property
	# def year(self):
	# 	"""Getter for year"""
	# 	return self._year

	# @property
	# def month(self):
	# 	"""Getter for month"""
	# 	return self._month

	# @property
	# def day(self):
	# 	"""Getter for day"""
	# 	return self._day

	# @property
	# def hour(self):
	# 	"""Getter for hour"""
	# 	return self._hour

	# @property
	# def minute(self):
	# 	"""Getter for minute"""
	# 	return self._minute
	
	# @property
	# def surgeries(self):
	# 	"""Getter for surgeries"""
	# 	return self._surgeries

	# @year.setter
	# def year(self, year):
	# 	"""
	# 	Setter for year
	# 	Attributes
	# 			self (schedule)
	# 			year (int)
	# 	"""
	# 	while not year.isdigit():
	# 		self.raiseerror()
	# 	self._year = int(year)

	# @month.setter
	# def month(self, month):
	# 	"""
	# 	Setter for month
	# 	Attributes
	# 			self (schedule)
	# 			month (int)
	# 	"""
	# 	while not month.isdigit() or month < 1 or month > 12:
	# 		self.raiseerror()
	# 	self._month = month

	# @day.setter
	# def day(self, day, month, year):
	# 	"""
	# 	Setter for day
	# 	Attributes
	# 			self (schedule)
	# 			day (int)
	# 			month (int)
	# 			year (int)
	# 	"""
	# 	if not day.isdigit() or day < 1 or day > 31:
	# 		self.raiseerror()
	# 	elif month not in [1, 3, 5, 7, 8, 10, 12] and day == 31:
	# 		self.raiseerror()
	# 	elif month == 2 and day == 30:
	# 		self.raiseerror()
	# 	if day == 29 and month == 2:
	# 		if year % 4 == 0:
	# 			if year % 400 == 0:
	# 				pass
	# 			elif year % 100 == 0:
	# 				self.raiseerror()
	# 		else:
	# 			self.raiseerror()
	# 	self._day = day

	# @hour.setter
	# def hour(self, hour):
	# 	"""
	# 	Setter for hour
	# 	Attributes
	# 			self (schedule)
	# 			hour (int)
	# 	"""
	# 	if not hour.isdigit() or hour < 0 or hour > 23:
	# 		self.raiseerror()
	# 	self._hour = hour

	# @minute.setter
	# def minute(self, minute):
	# 	"""
	# 	Setter for minute
	# 	Attributes
	# 			self (schedule)
	# 			minute (int)
	# 	"""
	# 	if not minute.isdigit() or minute < 0 or minute > 59:
	# 		self.raiseerror()
	# 	self._minute = minute
		
	# @surgeries.setter
	# def surgeries(self, x):
	# 	"""
	# 	Setter for surgeries
	# 	no, of course I don't want to do the validation (im lazy and the code will fail because of this)
	# 	"""
	# 	self._surgeries = x

	# def raiseerror(self):
	# 	"""
	# 	Raises an error in case of an incorrect input
	# 	"""
	# 	#this is left purposely blank until the display is created
	# 	return True