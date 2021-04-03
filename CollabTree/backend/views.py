from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from backend.forms import UserCreation
import smtplib, ssl
import random
from backend.models import UserAttribs
from django.contrib.auth.models import User, Permission
from django import forms


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
    if request.method == "POST" and request.FILES.get('image'):
        user_object = UserAttribs.objects.get(user = request.user)
        user_object.user_image = request.FILES.get('image')
        print(user_object.user_image)
        user_object.save()
        user_skills = str(user_object.skills)
        # print('Printing: '+str(user_skills))
        user_skills = user_skills.split(',')
        while ('' in user_skills):
            user_skills.remove('')
        # print(user_skills)
        skills = user_skills
        color_list = []
        skill_colors = dict()
        list_color_pair = []
        for _ in range(len(skills)):
            random_number = random.randint(0,16777215)
            hex_number = str(hex(random_number))
            hex_number =hex_number[2:]
            color_list.append(hex_number)
            # skill_colors[skills[_]] = hex_number
            skill_colors['ski'] = skills[_]
            skill_colors['col'] = hex_number
            list_color_pair.append({'ski': skills[_], 'col': hex_number})
        # print(list_color_pair) 

        full_name = user_object.full_name
        phone = user_object.phone_number
        mobile = user_object.mobile_number
        address = user_object.address
        website = user_object.website

        return render(request, 'User Profile/profile.html', {'user_object':user_object ,'website':website, 'skills': list_color_pair, 'name': full_name, 'phone': phone, 'mobile': mobile, 'address': address })


    elif request.method == "POST" and (request.POST.get('website')):
        user_object = UserAttribs.objects.get(user = request.user)
        user_object.website = request.POST['website']
        user_object.save()
        user_skills = str(user_object.skills)
        # print('Printing: '+str(user_skills))
        user_skills = user_skills.split(',')
        while ('' in user_skills):
            user_skills.remove('')
        # print(user_skills)
        skills = user_skills
        color_list = []
        skill_colors = dict()
        list_color_pair = []
        for _ in range(len(skills)):
            random_number = random.randint(0,16777215)
            hex_number = str(hex(random_number))
            hex_number =hex_number[2:]
            color_list.append(hex_number)
            # skill_colors[skills[_]] = hex_number
            skill_colors['ski'] = skills[_]
            skill_colors['col'] = hex_number
            list_color_pair.append({'ski': skills[_], 'col': hex_number})
        # print(list_color_pair) 

        full_name = user_object.full_name
        phone = user_object.phone_number
        mobile = user_object.mobile_number
        address = user_object.address
        website = user_object.website
        print(website)

        return render(request, 'User Profile/profile.html', {'user_object':user_object,'website':website, 'skills': list_color_pair, 'name': full_name, 'phone': phone, 'mobile': mobile, 'address': address})

    elif request.method == "GET":
        user_object = UserAttribs.objects.get(user=request.user)
        user_skills = str(user_object.skills)
        print('Printing: '+str(user_skills))
        user_skills = user_skills.split(',')
        while ('' in user_skills):
            user_skills.remove('')
        print(user_skills)
        skills = user_skills
        color_list = []
        skill_colors = dict()
        list_color_pair = []
        for _ in range(len(skills)):
            random_number = random.randint(0,16777215)
            hex_number = str(hex(random_number))
            hex_number =hex_number[2:]
            color_list.append(hex_number)
            # skill_colors[skills[_]] = hex_number
            skill_colors['ski'] = skills[_]
            skill_colors['col'] = hex_number
            list_color_pair.append({'ski': skills[_], 'col': hex_number})
        print(list_color_pair) 

        full_name = user_object.full_name
        phone = user_object.phone_number
        mobile = user_object.mobile_number
        address = user_object.address
        website = user_object.website



        return render(request, 'User Profile/profile.html', {'user_object':user_object,'skills': list_color_pair,'website': website, 'name': full_name, 'phone': phone, 'mobile': mobile, 'address': address})
        # if user_skills[0] != '':
        #     user_skills = set(user_skills)
        #     return render(request, 'User Profile/profile.html', {'skills':user_skills})
        # else:
        #     print('Entered else')
        #     return render(request, 'User Profile/profile.html')
    elif request.method == "POST":
        print("Initial Request.POST: "+request.POST['skills'])
        skills = request.POST['skills']
        full_name = request.POST['name']
        mobile = request.POST['mobile']
        phone = request.POST['phone']
        address = request.POST['address']
        print(skills, full_name, mobile, phone, address)
        user_skills = UserAttribs.objects.get(user=request.user).skills


        updated_skills = UserAttribs.objects.get(user=request.user)
        if full_name!= '':
            updated_skills.full_name = full_name
        if phone!= '':
            updated_skills.phone_number = phone
        if mobile!= '':
            updated_skills.mobile_number = mobile
        if address!= '':
            updated_skills.address = address
        if skills!='':
            skills = skills+','+updated_skills.skills
            skills = skills.lower()
            skills = skills.split(',')
            skills = [s.strip() for s in skills]

            while ('' in skills):
                skills.remove('')
            skills = set(skills)                
            print(skills)
            updated_skills.skills = ','.join(skills)
        elif skills =='':
            skills = updated_skills.skills.lower()
            skills = skills.split(',')
            skills = [s.strip() for s in skills]

            while ('' in skills):
                skills.remove('')
            skills = set(skills)
        
        skills = list(skills)



   
        # skills = str(skills).lower()
        color_list = []
        skill_colors = dict()
        list_color_pair = []
        for _ in range(len(skills)):
            random_number = random.randint(0,16777215)
            hex_number = str(hex(random_number))
            hex_number =hex_number[2:]
            color_list.append(hex_number)
            # skill_colors[skills[_]] = hex_number
            skill_colors['ski'] = skills[_]
            skill_colors['col'] = hex_number
            list_color_pair.append({'ski': skills[_], 'col': hex_number})
        print(list_color_pair) 


        

        # skills = set(skills)

        updated_skills.save()
        full_name = updated_skills.full_name
        phone = updated_skills.phone_number
        mobile = updated_skills.mobile_number
        address = updated_skills.address
        website = updated_skills.website
        # updated_skills.skill = str(skills)
        # updated_skills.save()
        # print("Saved in model: "+str(updated_skills.skills))
        # request.POST = request.POST.copy()
        # request.POST['skills'] = ''
        return render(request, 'User Profile/profile.html', {'user_object':updated_skills,'skills': list_color_pair,'website':website, 'name': full_name, 'phone': phone, 'mobile': mobile, 'address': address})
        


def sign_up(request):
    global user
    global signup_form
    if request.method == "POST":
        form = UserCreation(request.POST)
        if form.is_valid:
            signup_form = form
            if request.POST['password1'] != request.POST['password2']:
                print("Passwords didn't match")
                return HttpResponse("<h1>Passwords didn't match</h1>")
                
                # raise forms.ValidationError("Your passwords didn't match!")
                # return render(request , 'Index Page/index.html', {"form": UserCreation, "message": "Passwords did not match!"})
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
        return render(request, "Registration/otp_form.html",{'message' : "  "})
    if request.method=="POST":
        otp = request.POST['otp']
        if otp==str(pin):
            # print(otp==pin)
            # return redirect(reverse("dashboard"))
            user = signup_form.save()
            new_user = UserAttribs(user=user)
            new_user.phone_number = 'Empty!'
            new_user.mobile_number = 'Empty!'
            new_user.full_name = 'Empty!'
            new_user.address = 'Empty!'
            new_user.save()
            login(request, user)
            return redirect(reverse("dashboard"))

            # request.method = "POST"
            # return redirect('signup')
        else:
            return render(request, "Registration/otp_form.html", {'message' : "Wrong OTP"}) 

def dashboard(request):
    print(request.user.username)
    # if request.user.is_authenticated and request.user.username != 'admin':
    if request.user.is_authenticated:
        return render(request, 'After Login/home.html')
    else:
        return HttpResponse('<h1>Please Login</h1>')
def blog(request):
    return render(request, 'Blog Section/blog.html')