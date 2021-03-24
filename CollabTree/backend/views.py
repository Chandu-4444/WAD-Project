from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from backend.forms import UserCreation
import smtplib, ssl
import random
from backend.models import UserAttribs
from django.contrib.auth.models import User, Permission

user = 0
pin = 0
signup_form = 0

# Create your views here.

def index(request):
    if request.method=="GET":
        print("Inside GET")
        return render(request, 'Index Page/index.html', {"form":UserCreation})
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'After Login/home.html')
            else:
                return HttpResponse('<h1>Wrong</h1>')
        else:
            return HttpResponse('<h1>Username cannot be empty</h1>')

def profile(request):
    if request.method == "GET":
        user_skills = UserAttribs.objects.get(user=request.user).skills
        user_skills = str(user_skills)
        print('Printing: '+str(user_skills))
        user_skills = user_skills.split(',')
        print(user_skills)
        if user_skills[0] != '':
            
            print("entered if")
            return render(request, 'User Profile/profile.html', {'skills':user_skills})
        else:
            print('Entered else')
            return render(request, 'User Profile/profile.html')
    elif request.method == "POST":
        skills = request.POST['skills']
        user_skills = UserAttribs.objects.get(user=request.user).skills
        if skills == '':
            return render(request, 'User Profile/profile.html', {'skills': user_skills.split(',')})

        print(skills)
        print(type(skills))
        
        print(user_skills)
        print(type(user_skills))
        if user_skills != '':
            skills = skills+',' + str(user_skills)
        else:
            skills = skills+','

        updated_skills = UserAttribs.objects.get(user=request.user)
        updated_skills.skills = skills
        updated_skills.save()
        skills = str(updated_skills.skills)
        skills = skills.split(',')
        print(skills)
        return render(request, 'User Profile/profile.html', {'skills': skills})
        


def sign_up(request):
    global user
    global signup_form
    if request.method == "POST":
        form = UserCreation(request.POST)
        if form.is_valid:
            signup_form = form
            # login(request, user)
            # return redirect("dashboard")
            request.session['email'] = request.POST['email']
            # login(request, user)
            return redirect('otp_verification')
        else:
            return render(request, 'Index Page/index.html', {"form":UserCreation})


    else:
        return render(request, 'Index Page/index.html', {"form":UserCreation})
    
def otp_verification(request):
    global pin
    if request.method == "GET":
        email = request.session.get('email')
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        pin = random.randint(10000, 99999)
        s.login("collabtree.team@gmail.com", "CollabTree1234")
        message = "Subject:{}\n\n{}".format("OTP", pin)
        s.sendmail("collabtree.team@gmail.com",email, message)
        s.quit()
        return render(request, "Registration/otp_form.html")
    if request.method=="POST":
        otp = request.POST['otp']
        if otp==str(pin):
            # print(otp==pin)
            # return redirect(reverse("dashboard"))
            user = signup_form.save()
            new_user = UserAttribs(user=user)
            new_user.save()
            login(request, user)
            return redirect(reverse("dashboard"))

            # request.method = "POST"
            # return redirect('signup')
        else:
            return render(request, "Registration/otp_form.html") 

def dashboard(request):
    print(request.user.username)
    if request.user.is_authenticated and request.user.username != 'admin':
        return render(request, 'After Login/home.html')
    else:
        return HttpResponse('<h1>Please Login</h1>')
