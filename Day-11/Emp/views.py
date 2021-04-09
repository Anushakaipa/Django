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

def registration(ry):
	if ry.method=="POST":
		na=ry.POST['a']
		em=ry.POST['b']
		pas=ry.POST['c']
		Age=ry.POST['g']
		d={'us':na,'eml':em,'p':pas,'ag':Age}
		return render(ry,'html/details.html',d)
	return render(ry,'html/registration.html')