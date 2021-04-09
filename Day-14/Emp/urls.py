from django.urls import path
from Emp import views
urlpatterns=[
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('con/',views.contact,name="con"),
	path('log/',views.login,name="lg"),
	path('reg/',views.registration,name="rg"),
	path('cr/',views.crud,name="crud"),
	path('del/<str:id>',views.deletedata,name="delete"),
	path('df/',views.dform,name="dff"),
	path('tb/',views.tab,name="tab"),
	path('delete/<int:id>',views.delete,name="del"),
	#path('uedit/<int:id>',views.useredit,name="useredit"),
	path('e/<int:si>/',views.userupdate,name="ue"),
	path('ui/<str:uname>/',views.userinfo,name="uin"),
]