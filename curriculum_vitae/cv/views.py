from email import message
from django.shortcuts import redirect, render
from .models import Index
from django.http.response import HttpResponse
from django.contrib.auth import login, authenticate #add this
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect('home')
        else: 
            return redirect('login')

    return render(request, 'cv/login.html')





# @login_required
def home(request):
    # message= "HELLO"
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        paddress = request.POST['paddress']
        tempaddr = request.POST['tempaddr']
        social_media = request.POST['social_media']
        about = request.POST['about']
        skills = request.POST['skills']
        experience = request.POST['experience']
        awards = request.POST['awards']
        interest = request.POST['interest']

        cv = Index(name=name,email=email,paddress=paddress,tempaddr=tempaddr,social_media=social_media,about=about,skills=skills,experience=experience,awards=awards,interest=interest)

        cv.save()
        
    return render(request, 'cv/index.html')

    # return HttpResponse(message)




