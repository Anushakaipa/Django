from django.shortcuts import render,redirect
from django.http import HttpResponse
from Emp.models import UsrRg,NewData
from Emp.forms import UsregForm,UserUpdate,NewUsrForm

# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(re):
	return render(re,'html/about.html')

def contact(rt):
	return render(rt,'html/contact.html')

def login(er):
	return render(er,'html/login.html')

def management(request):
	return render(request,'html/management.html')

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
		#data2=UsrRg.objects.all()
		if len(un)!=0:
			data=UsrRg.objects.create(Username=un,password=pas,email=em,age=Age)
		#return render(request,'html/actions.html',{'info':data2})
	data2=UsrRg.objects.all()
	return render(request,'html/actions.html',{'info':data2})

def deletedata(req,id):
	data=UsrRg.objects.get(id=id)
	data.delete()
	return redirect('/cr')

def dform(request):
	if request.method=="POST":
		e=UsregForm(request.POST)
		if e.is_valid():
			q=e.save()
			y=NewData.objects.create(pid_id=q.id)
			return redirect('/tb')
			#return HttpResponse("User Created Successfully")
	e=UsregForm()
	return render(request,'html/dyform.html',{'tu':e})

def tab(hj):
	data=UsrRg.objects.all()
	return render(hj,'html/tab.html',{'info':data})

def delete(red,id):
	data=UsrRg.objects.get(id=id)
	if red.method=="POST":
		data.delete()
		return redirect('/tb')
	return render(red,'html/userdelete.html',{'sd':data})

# def useredit(df,id):
# 	data=UsrRg.objects.get(id=id)
# 	if df.method=="POST":
# 		data.Username=df.POST['Username']
# 		data.email=df.POST['Email']
# 		data.password=df.POST['password']
# 		data.age=df.POST['Age']
# 		data.save()
# 		return HttpResponse("Data Saved")
# 	return render(df,'html/useredit.html',{'info':data})

# def userupdate(up,si):
# 	a=UsrRg.objects.get(id=si)
# 	if up.method=="POST":
# 		d=UsregForm(up.POST,instance=a)
# 		if d.is_valid():
# 			d.save()
# 			return redirect('/tb')
# 	d=UsregForm(instance=a)
# 	return render(up,'html/updateuser.html',{'us':d})

def userupdate(up,si):
	a=UsrRg.objects.get(id=si)
	y=NewData.objects.get(pid_id=si)
	if up.method=="POST":
		d=UserUpdate(up.POST,instance=a)
		k=NewUsrForm(up.POST,instance=y)
		if d.is_valid() and k.is_valid():
			d.save()
			k.save()
			return redirect('/tb')
	d=UserUpdate(instance=a)
	k=NewUsrForm(instance=y)

	return render(up,'html/updateuser.html',{'us':d,'nt':k})

def userinfo(ty,uname):
	p=UsrRg.objects.get(Username=uname)
	h=NewData.objects.get(pid_id=p.id)
	return render(ty,'html/newinfo.html',{'y':p,'yu':h})

