from django.urls import path
from Emp import views
urlpatterns=[
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('con/',views.contact,name="con"),
	path('log/',views.login,name="lg"),
	path('reg/',views.registration,name="rg"),
]