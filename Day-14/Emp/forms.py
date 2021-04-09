from Emp.models import UsrRg,NewData
from django import forms

class UsregForm(forms.ModelForm):
	class Meta:
		model=UsrRg
		fields=['Username','email','password']
		widgets={
		"Username":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter UserName","required":True,}),
		"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter Email","required":True,}),
		"password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter password","required":True,}),
		#"age":forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter Age", "required"=True}),

		}

class UserUpdate(forms.ModelForm):
	class Meta:
		model=UsrRg
		fields=['Username','email','age']
		widgets={
		"Username":forms.TextInput(attrs={"class":"form-control","placeholder":"Update your UserName","required":True,}),
		"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Update your Email","required":True,}),
		"age":forms.NumberInput(attrs={"class":"form-control","placeholder":"Update your Age", "required":True}),
		}

class NewUsrForm(forms.ModelForm):
	class Meta:
		model=NewData
		fields=['mobile','gender']
		widgets={
		"mobile":forms.TextInput(attrs={"class":"form-control","placeholder":"Update Phone Number","required":True,"max":10}),
		"gender":forms.Select(attrs={"class":"form-control","placeholder":"Enter","required":True}),
		}
