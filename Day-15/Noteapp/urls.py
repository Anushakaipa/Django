from django.urls import path
from Noteapp import views
from django.contrib.auth import views as ad
urlpatterns=[

path('',views.home,name="hm"),
path('about/',views.about,name="abt"),
path('contact/',views.contact,name="con"),
path('lg/',ad.LoginView.as_view(template_name='htc/login.html'),name="log"),
path('rg/',views.regi,name="rge"),
path('ds/',views.dashboard,name="dsh"),
path('lgo/',ad.LogoutView.as_view(template_name='htc/logout.html'),name="logo"),
]