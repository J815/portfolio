from django.shortcuts import render
from jubayer.models import Contact
# Create your views her
def contact(request):
     if request.method =='POST':
          name= request.POST['name']
          email= request.POST['email']
          desc= request.POST['desc']
          ins = Contact(name=name, email=email, desc=desc)
          ins.save()
     return render(request, 'contact.html')
def skills(request):
     return render(request, 'skills.html')
def about(request):
    return render(request, 'about.html')
def home(request):
    return render(request, 'home.html')