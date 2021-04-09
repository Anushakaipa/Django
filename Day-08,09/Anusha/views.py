from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def house(request):
	return HttpResponse("<h1 style='color:white;background-color:red;text-align:center'>Welcome to Home Page</h1>")

def chk(request):
	return HttpResponse("<script>alert('Hi Good Afternoon, Enter correct password')</script><h2>Welcome</h2>")

def HomePage(request):
	return render(request,'Anu/HomePage.html')

def login(re):
	return render(re,'Anu/login.html')

def reg(rt):
	return render(rt,'Anu/registered.html')

def bthm(qe):
	return render(qe,'Anu/bthome.html')

def about(er):
	return render(er,'Anu/about.html')

def contact(rt):
	return render(rt,'Anu/contact.html')

def register(ty):
	return render(ty,'Anu/registeration.html')

def management(ti):
	return render(ti,'Anu/management.html')