from django.shortcuts import render,redirect
from Noteapp.forms import UsForm
# Create your views here.
def home(request):
	return render(request,'htc/home.html')

def about(de):
	return render(de,'htc/about.html')

def contact(dg):
	return render(dg,'htc/contact.html')

def regi(request):
	if request.method=="POST":
		p=UsForm(request.POST)
		if p.is_valid():
			p.save()
			return redirect('/lg')
	p=UsForm()
	return render(request,'htc/register.html',{'u':p})

def dashboard(request):
	return render(request,'htc/dashboard.html')