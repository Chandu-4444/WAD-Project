from django.core.checks import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from backend.forms import UserCreation
import smtplib, ssl
import random
from django.contrib import messages
from backend.models import UserAttribs, Blog, Project, Project_Question
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
                project_objects = Project.objects.all()
                # return render(request, 'After Login/home.html', {"project_objects" : project_objects })
                return redirect(reverse('dashboard'))
            else:
                return HttpResponse('<h1>Wrong</h1>')
        else:
            return HttpResponse('<h1>Username cannot be empty</h1>')
# def profile_name(request, id):
#     user_obj = UserAttribs.objects.get(id = id)
#     print(user_obj)
#     return HttpResponse("<h1>Hello {{ user_obj }} </h1>")


def profile(request, id=None):
    current_user = UserAttribs.objects.get(user = request.user)
    if id:
        # return HttpResponse('<h1>Hello, {} {}</h1>'.format(id, UserAttribs.objects.get(id=id).user.username))
        # user_display_obj = UserAttribs.objects.get(id=id)
        user_object = UserAttribs.objects.get(id=id)
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
        return render(request, 'User Profile/profile_to_display.html', {'user_display': user_object,'user_object':user_object,'skills': list_color_pair,'website': website, 'name': full_name, 'phone': phone, 'mobile': mobile, 'address': address, 'assigned_projects': user_object.assigned_project.all()})

        # return render(request, 'User Profile/profile.html', {'user_object':user_display_obj, 'user_display': current_user })
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

        return render(request, 'User Profile/profile.html', {'user_display': user_object,'user_object':user_object ,'website':website, 'skills': list_color_pair, 'name': full_name, 'phone': phone, 'mobile': mobile, 'address': address, 'assigned_projects': user_object.assigned_project.all() })


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

        return render(request, 'User Profile/profile.html', {'user_display': user_object,'user_object':user_object,'website':website, 'skills': list_color_pair, 'name': full_name, 'phone': phone, 'mobile': mobile, 'address': address, 'assigned_projects': user_object.assigned_project.all()})

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



        return render(request, 'User Profile/profile.html', {'user_display': user_object,'user_object':user_object,'skills': list_color_pair,'website': website, 'name': full_name, 'phone': phone, 'mobile': mobile, 'address': address, 'assigned_projects': user_object.assigned_project.all()})
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
        return render(request, 'User Profile/profile.html', {'user_display':updated_skills,'user_object':updated_skills,'skills': list_color_pair,'website':website, 'name': full_name, 'phone': phone, 'mobile': mobile, 'address': address, 'assigned_projects': user_object.assigned_project.all()})
        


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
    user_object = UserAttribs(user = request.user)
    store=""
    f = open("messages_data.txt","r")
    for line in f:
        line = str(line)[:-1]
        a = line.split(",")
        print(a)
        if a[0]==user_object.user.username and a[2]=='1':
            print("Yes")
            messages.success(request, f"{a[0]} you have been accepted for {a[1]} project.")
            x = list(line)
            x[-1]='0'
            store+="".join(x)+"\n"
        else:
            store+=str(line)+"\n"
    f = open("messages_data.txt","w")
    f.write(store)
    f.close()
    # messages.info(request, "Info Message")


    # if request.user.is_authenticated and request.user.username != 'admin':
    if request.user.is_authenticated:
        if request.method == "GET":
            project_objects = Project.objects.all()
            # for i in project_objects:
            #     try:
            #         print(i.title,i.applied_users.all())
            #     except :
            #         print("Error")
            return render(request, 'After Login/home.html', {"project_objects" : project_objects })
        elif request.method=="POST" and request.POST.get("a1") and request.POST.get("a2"):
            question_obj = Project_Question.objects.create(Q1 = request.POST["a1"])
            question_obj.Q2 = request.POST["a2"]
            question_obj.project_title = Project.objects.get(id=request.POST["project_title"]).title
            question_obj.save()
            project_objects = Project.objects.all()
            
            # project_object = Project.objects.get(title = request.POST["project_title"])
            # project_object.applied_candidates += UserAttribs.objects.get(user=request.user)
            # project_object.save()
            user_obj = UserAttribs.objects.get(user=request.user)
            proj_obj = Project.objects.get(id=request.POST["project_title"])
            proj_obj.applied_users.add(user_obj)
            proj_obj.project_questions = question_obj
            user_obj.save()
            proj_obj.save()

            return HttpResponse("Succesfully Applied!")
        elif request.method == "POST" and request.POST.get("project_title"):
            proj_obj = Project.objects.get(id = request.POST['project_title'])

            
            return render(request, 'questions.html', {"project_id" : proj_obj.id})
        

    else:
        return HttpResponse('<h1>Please Login</h1>')

def blog(request):
    blog_objects = Blog.objects.all().order_by('-date_time')
    blog_objects = blog_objects[:9]
    # print(blog_objects)
    # for i in blog_objects:
    #     print(i.tags.all())
    return render(request, 'Blog Section/blog.html', {"blog_objects" : blog_objects})

def new_blog(request):
    if request.method == "GET":
        return render(request,'Blog Section/new_blog.html')
    elif request.method == "POST":
        title = request.POST["title"]
        body = request.POST["body"]
        user_object = UserAttribs.objects.get(user=request.user)
        blog_object = Blog.objects.create(author=user_object)
        blog_object.title = title
        blog_object.body = body
        blog_object.cover_image = request.FILES["cover_image"]
        tags = request.POST['tags']
        for tag in tags.split(','):
            blog_object.tags.add(tag)
        print(blog_object.tags)
        blog_object.save()
        
        return redirect(reverse("blogs"))

def my_projects(request):
    project_objects = Project.objects.all()
    project_list=[]
    for project in project_objects:
        if project.owner == UserAttribs.objects.get(user=request.user):
            print(project.id)
            # proj_obj = Project.objects.get(id=project.id)
            applied_users = project.applied_users.all()
            # print("Applied users"+str(applied_users))
            project_list.append({'project':project,'applied_users':applied_users})


            

    # print(project_list)
    print(project_list)
    return render(request, 'My Projects/myProjects.html' ,{'project_list': project_list})

def project_form(request):
    if request.method == "GET":
        return render(request,'My Projects/project_form.html')
    elif request.method == 'POST':
        title = request.POST["title"]
        description = request.POST["description"]
        duration = int(request.POST["duration"])
        stipend = int(request.POST["stipend"])

        owner_object = UserAttribs.objects.get(user=request.user)
        project_object = Project.objects.create(owner=owner_object)
        project_object.title = title
        project_object.description = description
        project_object.duration = duration
        project_object.stipend = stipend
        tags = request.POST['tags']
        for tag in tags.split(','):
            project_object.tags_requirement.add(tag)
        print(project_object.tags_requirement)
        project_object.save()
        
        return redirect(reverse("dashboard"))
        
def assign_user(request, id, proj_id):
    print("In assign_user")
    user_obj = UserAttribs.objects.get(id=id)
    proj_obj = Project.objects.get(id=proj_id)

    proj_obj.assigned_user = user_obj
    user_obj.assigned_project.add(proj_obj)
    f = open("messages_data.txt","a")
    f.write(str(user_obj.user.username)+","+str(proj_obj.title)+","+str(1)+"\n")
    f.close()     
    print(user_obj.assigned_project.all())
    proj_obj.save()
    return redirect(reverse("my_projects"))


