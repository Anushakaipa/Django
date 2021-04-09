from django.shortcuts import render,redirect
from Emp.models import UsrRg
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

def crud(request):
	if request.method=="POST":
		un=request.POST['name']
		pas=request.POST['pwd']
		em=request.POST['eml']
		Age=request.POST['age']
		data2=UsrRg.objects.all()
		if len(un)!=0:
			data=UsrRg.objects.create(Username=un,password=pas,email=em,age=Age)
		return render(request,'html/actions.html',{'info':data2})
	data2=UsrRg.objects.all()
	return render(request,'html/actions.html',{'info':data2})

def deletedata(req,id):
	data=UsrRg.objects.get(id=id)
	data.delete()
	return redirect('/cr')