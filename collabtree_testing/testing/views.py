from django.shortcuts import render, redirect
from django.http import HttpResponse
from testing.form import UserCreation
from django.urls import reverse
from django.contrib.auth import login
import smtplib, ssl
import random

user = 0
pin = 0


# Create your views here.
def index(request):
    return render(request, 'Index Page/index.html')
def login_form(request):
    return render(request, 'registration/login.html')
def dashboard(request):
    return render(request, "After Login/home.html")
def otp_verification(request):
    # s = smtplib.SMTP('smtp.gmail.com', 587)
    # s.starttls()
    # s.login("collabtree.team@gmail.com", "collabtree")
    # message = "Subject: {}\n\n{}".format("OTP", "Hello, User!")
    # s.sendmail("collabtree.team@gmail.com", email, message)
    # s.quit()
    return render('otp_verification')
def signup(request):
    if request.method == "GET":
        return render(request, "registration/Sign_Up.html", {"form" : UserCreation})
    elif request.method == "POST":
        form = UserCreation(request.POST)
        if form.is_valid():
            global user
            user = form.save()
            # print(form.cleaned_data['job_title'])
            request.session['email'] = form.cleaned_data['email']
            # login(request, user)
            return redirect('otp_verification')
            # def inner():
            #     login(request, user)
            #     return redirect(reverse("dashboard"))

            # return redirect('profile_display')
        #     login(request, user)
        #     return redirect(reverse("dashboard"))
        # else:
        #     return redirect(reverse("signup"))
def profile_display(request):
    return render(request, "User Profile/profile.html")

def otp_verification(request):
    global pin
    if request.method == "GET":
        email = request.session.get('email')
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        pin = random.randint(10000, 99999)
        s.login("collabtree.team@gmail.com", "collabtree")
        message = "Subject:{}\n\n{}".format("OTP", pin)
        s.sendmail("collabtree.team@gmail.com",email, message)
        s.quit()
        return render(request, "registration/otp_form.html")
    if request.method=="POST":
        otp = request.POST['otp']
        if otp==str(pin):
            # print(otp==pin)
            # return redirect(reverse("dashboard"))
            login(request, user)
            return redirect(reverse("dashboard"))

            # request.method = "POST"
            # return redirect('signup')
        else:
            return render(request, "registration/otp_form.html") 



    # user = form.save()
    # login(request, user)
    # print(request.method)
    
    # return redirect(reverse("dashboard"))




