from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(re):
	return render(re,'html/about.html')

def contact(rt):
	return render(rt,'html/contact.html')

def login(er):
	return render(er,'html/login.html')