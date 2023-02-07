from django.urls import path
from . import views

urlpatterns = [
     path('contact.html', views.contact),
     path('skills.html', views.skills),
     path('about.html', views.about),
    path('', views.index),
   

]
