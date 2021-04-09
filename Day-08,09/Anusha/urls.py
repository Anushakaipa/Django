from django.urls import path
from Anusha import views

urlpatterns=[
	path('rt/',views.house,name='home'),
	path('demo/',views.chk),
	path('home/',views.HomePage),
	path('lg/',views.login),
	path('rg/',views.reg,name="register"),
	path('',views.bthm),
	path('about/',views.about,name='about'),
	path('contact/',views.contact,name='contact'),
	path('reg/',views.register),
	path('mag/',views.management,name='management'),
]
