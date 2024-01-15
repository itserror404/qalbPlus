import userentry
from userentry.forms import Signupf, Loginf
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from userentry.models import User
from .TPfind import *
from .models import Tptestnew, Appointment, CurrentUser
from userentry.models import User
import datetime

# function to generate list of start-end times for TP
def timelist(start, end):
    timearray = []
    delta = datetime.timedelta(minutes=30)
    start = datetime.datetime.strptime( start, '%H:%M' )
    end = datetime.datetime.strptime( end, '%H:%M' )
    t = start
    while t <= end :
        timearray.append( datetime.datetime.strftime( t, '%H:%M'))
        t += delta
    return ','.join(timearray)

def home(request):
	return render(request, "main/home.html", {})

def admin(request):
	return render(request, "admin", {})

def patient(request):
	return render(request, "main/patientprofile.html", {})

def tp(request):
	return render(request, "main/tpprofile.html", {})

def registeruser(request):
	return render(request, "main/registeruser.html", {})

def log_in(request):
	template_name = "login.html"
	form = Loginf(request.POST or None)
	display = None
	if request.method == 'POST':
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			queryuser = CurrentUser.objects.all()
			currentuser = queryuser[0]
			currentuser.email = user.email
			currentuser.name = user.name
			currentuser.save()

			if user is not None and user.is_admin:
				login(request, user)
				return redirect('admin')
			elif user is not None and user.is_patient:
				login(request,user)
				return redirect('search-TP')
			elif user is not None and user.is_tp:
				login(request, user)
				return redirect('view-Appointmentstp')
			else:
				display = 'Invalid password/username'
		else:
			display = 'Form cannot be validated'
	return render(request, 'main/login.html', {'form': form, 'msg': display})


def registerPatient(request):
	template_name = "registerPatient.html"
	display = None
	if request.method == 'POST':
		form = Signupf(request.POST)
		if form.is_valid():
			user = form.save()
			display = 'Account is Created'
			return redirect('log_in')
		else:
			display = 'Error in the Form, re-apply'
	else:
		form = Signupf()
	return render(request, 'main/registerPatient.html', {'form': form, 'msg': display})

def registerTP(request):
	template_name = "registerTP.html"
	display = None
	if request.method == 'POST':
		form = Signupf(request.POST)
		if form.is_valid():
			user = form.save()
			display = 'Account is Created'
			user.available_times1= timelist(user.starttime, user.endtime)
			user.available_times2 = timelist(user.starttime, user.endtime)
			user.available_times3 = timelist(user.starttime, user.endtime)
			user.available_times4 = timelist(user.starttime, user.endtime)
			user.available_times5 = timelist(user.starttime, user.endtime)
			user.save()
			return redirect('log_in')
		else:
			display = 'Error in the Form, re-apply'
	else:
		form = Signupf()
	return render(request, 'main/registerTP.html', {'form': form, 'msg': display})


def searchTP(request):
	if request.method == "POST":
		#takes user to proper books appointment page for a specific TP
		if request.POST.get("item1", None):
			# print("ITEM 1 was selected")
			tpemail = request.POST.get("item1", None)
			return render(request, "main/BookAppointment.html", {'tpemail': tpemail})
		elif request.POST.get("item2", None):
			# print("ITEM 2 was selected")
			tpemail = request.POST.get("item2", None)
			return render(request, "main/BookAppointment.html", {'tpemail': tpemail})
		elif request.POST.get("item3", None):
			# print("ITEM 3 was selected")
			tpemail = request.POST.get("item3", None)
			return render(request, "main/BookAppointment.html", {'tpemail': tpemail})
		elif request.POST.get("item4", None):
			# print("ITEM 4 was selected")
			tpemail = request.POST.get("item4", None)
			return render(request, "main/BookAppointment.html", {'tpemail': tpemail})
		elif request.POST.get("item5", None):
			# print("ITEM 5 was selected")
			tpemail = request.POST.get("item5", None)
			return render(request, "main/BookAppointment.html", {'tpemail': tpemail})
		else:
			origin = request.POST['origin']
			insurancecheck = request.POST.get('insurancecheck', False)
			specialtycheck = request.POST['choices-single-default']
			# print(insurancecheck) #for testing
			# print(specialtycheck) #for testing
			queryuser = CurrentUser.objects.all()
			patient = User.objects.get(email=queryuser[0].email, is_patient=1)
			insurancematch = patient.insurancedetails
			# print(insurancematch) #for testing
			results = findTP(origin,specialtycheck,insurancematch,insurancecheck)

			return render(request, "main/SearchTP.html", {'origin':origin, 'results':results})
	else:
		return render(request, "main/SearchTP.html", {})

def viewAppointment(request):
	if request.method == "POST":
		queryuser = CurrentUser.objects.all()
		patient = queryuser[0]
		results = Appointment.objects.filter(patientemail=patient.email) #gets the appointments linked with the currentuser
		return render(request, "main/ViewAppointments.html", {'results':results})
	else:
		queryuser = CurrentUser.objects.all()
		# print(queryuser)
		patient = queryuser[0]
		results = Appointment.objects.filter(patientemail=patient.email)
		return render(request, "main/ViewAppointments.html", {'results': results})

def viewAppointmentTP(request):
	if request.method == "POST":
		queryuser = CurrentUser.objects.all()
		tp = queryuser[0]
		results = Appointment.objects.filter(tpemail=tp.email)  #gets the appointments linked with the currentuser
		return render(request, "main/ViewAppointmentstp.html", {'results':results})
	else:
		queryuser = CurrentUser.objects.all()
		tp = queryuser[0]
		results = Appointment.objects.filter(tpemail=tp.email) #gets the appointments linked with the currentuser
		return render(request, "main/ViewAppointmentstp.html", {'results': results})
def bookAppointment(request):
	if request.method == "POST":
		#books the proper appointment slot
		if request.POST.get("Mon-book", None):
			# print("Monday time was selected")
			bookingtime = request.POST.get("Mon-book", None)
			tpemail = request.POST['emailholder']
			usermessage = updateAppointment(bookingtime,tpemail,1)
			return render(request, "main/BookAppointment.html", {'tpemail': tpemail, 'usermessage':usermessage})
		elif request.POST.get("Tue-book", None):
			# print("Tuesday time was selected")
			bookingtime = request.POST.get("Tue-book", None)
			tpemail = request.POST['emailholder']
			usermessage = updateAppointment(bookingtime, tpemail, 2)
			return render(request, "main/BookAppointment.html", {'tpemail': tpemail, 'usermessage': usermessage})
		elif request.POST.get("Wed-book", None):
			# print("Wednesday time was selected")
			bookingtime = request.POST.get("Wed-book", None)
			tpemail = request.POST['emailholder']
			usermessage = updateAppointment(bookingtime, tpemail, 3)
			return render(request, "main/BookAppointment.html", {'tpemail': tpemail, 'usermessage': usermessage})
		elif request.POST.get("Thurs-book", None):
			# print("Thursday time was selected")
			bookingtime = request.POST.get("Thurs-book", None)
			tpemail = request.POST['emailholder']
			usermessage = updateAppointment(bookingtime, tpemail, 4)
			return render(request, "main/BookAppointment.html", {'tpemail': tpemail, 'usermessage': usermessage})
		elif request.POST.get("Fri-book", None):
			# print("Friday time was selected")
			bookingtime = request.POST.get("Fri-book", None)
			tpemail = request.POST['emailholder']
			usermessage = updateAppointment(bookingtime, tpemail, 5)
			return render(request, "main/BookAppointment.html", {'tpemail': tpemail, 'usermessage': usermessage})
		else:
			#loads the appointment times for the treatment provider
			tpemail = request.POST['emailholder']
			tpbook = User.objects.filter(email=tpemail).filter(is_tp=1)

			mondaystring = tpbook[0].available_times1
			tuesdaystring = tpbook[0].available_times2
			wednesdaystring = tpbook[0].available_times3
			thursdaystring = tpbook[0].available_times4
			fridaystring = tpbook[0].available_times5

			mon_list = mondaystring.split(',')
			tue_list = tuesdaystring.split(',')
			wed_list = wednesdaystring.split(',')
			thurs_list = thursdaystring.split(',')
			fri_list = fridaystring.split(',')

			print(mon_list)


			return render(request, "main/BookAppointment.html", {'mon_list':mon_list, 'tue_list':tue_list, 'wed_list':wed_list, 'thurs_list':thurs_list, 'fri_list':fri_list, 'tpemail': tpemail})

	else:

		return render(request, "main/BookAppointment.html", {})


#called to update the appointment timings of the treatment provider
def updateAppointment(bookingtime, tpemail, availabletimesx):
	tpbook = User.objects.filter(email=tpemail).filter(is_tp=1) #gets the Tp who the appointment was booked with
	alertmessage = ""
	if availabletimesx == 1:
		timestring = tpbook[0].available_times1
		timelist = timestring.split(',')
		newtimestring = ""
		#removes the booked appointment from the available times
		for time in timelist:
			if time != bookingtime:
				newtimestring = newtimestring + time + ","
		newtimestring = newtimestring[:-1]
		tpbookupdate = User.objects.get(email=tpemail, is_tp=1)
		# print(tpbookupdate)

		tpbookupdate.available_times1 = newtimestring
		tpbookupdate.save() #new times are updated on the database
		queryuser = CurrentUser.objects.all()
		patient = queryuser[0]
		newappointment = Appointment(tpemail=tpemail, tpname=tpbookupdate.name,patientemail=patient.email, patientname=patient.name,time=bookingtime,day="Monday")
		newappointment.save() #appointment details saved on database
		alertmessage = "Your appointment is booked for Monday "+ bookingtime + " with " + tpbookupdate.name
	elif availabletimesx == 2:
		timestring = tpbook[0].available_times2
		timelist = timestring.split(',')
		newtimestring = ""
		for time in timelist:
			if time != bookingtime:
				newtimestring = newtimestring + time + ","
		newtimestring = newtimestring[:-1]
		tpbookupdate = User.objects.get(email=tpemail, is_tp=1)

		tpbookupdate.available_times2 = newtimestring
		tpbookupdate.save()
		queryuser = CurrentUser.objects.all()
		patient = queryuser[0]
		newappointment = Appointment(tpemail=tpemail, tpname=tpbookupdate.name, patientemail=patient.email, patientname=patient.name, time=bookingtime, day="Tuesday")
		newappointment.save()
		alertmessage = "Your appointment is booked for Tuesday " + bookingtime + " with " + tpbookupdate.name
	elif availabletimesx == 3:
		timestring = tpbook[0].available_times3
		timelist = timestring.split(',')
		newtimestring = ""
		for time in timelist:
			if time != bookingtime:
				newtimestring = newtimestring + time + ","
		newtimestring = newtimestring[:-1]
		tpbookupdate = User.objects.get(email=tpemail, is_tp=1)

		tpbookupdate.available_times3 = newtimestring
		tpbookupdate.save()
		queryuser = CurrentUser.objects.all()
		patient = queryuser[0]
		newappointment = Appointment(tpemail=tpemail, tpname=tpbookupdate.name, patientemail=patient.email, patientname=patient.name, time=bookingtime, day="Wednesday")
		newappointment.save()
		alertmessage = "Your appointment is booked for Wednesday " + bookingtime + " with " + tpbookupdate.name
	elif availabletimesx == 4:
		timestring = tpbook[0].available_times4
		timelist = timestring.split(',')
		newtimestring = ""
		for time in timelist:
			if time != bookingtime:
				newtimestring = newtimestring + time + ","
		newtimestring = newtimestring[:-1]
		tpbookupdate = User.objects.get(email=tpemail, is_tp=1)

		tpbookupdate.available_times4 = newtimestring
		tpbookupdate.save()
		queryuser = CurrentUser.objects.all()
		patient = queryuser[0]
		newappointment = Appointment(tpemail=tpemail, tpname=tpbookupdate.name, patientemail=patient.email, patientname=patient.name, time=bookingtime, day="Thursday")
		newappointment.save()
		alertmessage = "Your appointment is booked for Thursday " + bookingtime + " with " + tpbookupdate.name
	elif availabletimesx == 5:
		timestring = tpbook[0].available_times5
		timelist = timestring.split(',')
		newtimestring = ""
		for time in timelist:
			if time != bookingtime:
				newtimestring = newtimestring + time + ","
		newtimestring = newtimestring[:-1]
		tpbookupdate = User.objects.get(email=tpemail, is_tp=1)

		tpbookupdate.available_times5 = newtimestring
		tpbookupdate.save()
		queryuser = CurrentUser.objects.all()
		patient = queryuser[0]
		newappointment = Appointment(tpemail=tpemail, tpname=tpbookupdate.name, patientemail=patient.email,patientname=patient.name, time=bookingtime, day="Friday")
		newappointment.save()
		alertmessage = "Your appointment is booked for Friday " + bookingtime + " with " + tpbookupdate.name
	return alertmessage

