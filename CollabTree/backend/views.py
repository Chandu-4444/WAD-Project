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
from django.contrib.auth.models import User
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail

user = 0
pin = 0
signup_form = {}

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
            skill_colors['ski'] = skills[_]
            skill_colors['col'] = hex_number
            list_color_pair.append({'ski': skills[_], 'col': hex_number})
        full_name = user_object.full_name
        phone = user_object.phone_number
        mobile = user_object.mobile_number
        address = user_object.address
        website = user_object.website

        return render(request, 'User Profile/profile.html', {'user_display': user_object,'user_object':user_object ,'website':website, 'skills': list_color_pair, 'name': full_name, 'phone': phone, 'mobile': mobile, 'address': address, 'assigned_projects': user_object.assigned_project.all() })


    elif request.method == "POST" and (request.POST.get('website') or request.POST.get('github') or request.POST.get('twitter') or request.POST.get('instagram') or request.POST.get('facebook')):
        user_object = UserAttribs.objects.get(user = request.user)
        if request.POST['website']!="":
            user_object.website = request.POST['website']
        if request.POST['github']: 
            user_object.github = request.POST['github']
        if request.POST['twitter']:
            user_object.twitter = request.POST['twitter']
        if request.POST['instagram']:
            user_object.instagram = request.POST['instagram']
        if request.POST['facebook']:
            user_object.facebook = request.POST['facebook']
        user_object.save()
        user_skills = str(user_object.skills)
        user_skills = user_skills.split(',')
        while ('' in user_skills):
            user_skills.remove('')
        skills = user_skills
        color_list = []
        skill_colors = dict()
        list_color_pair = []
        for _ in range(len(skills)):
            random_number = random.randint(0,16777215)
            hex_number = str(hex(random_number))
            hex_number =hex_number[2:]
            color_list.append(hex_number)
            skill_colors['ski'] = skills[_]
            skill_colors['col'] = hex_number
            list_color_pair.append({'ski': skills[_], 'col': hex_number})

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



   
        color_list = []
        skill_colors = dict()
        list_color_pair = []
        for _ in range(len(skills)):
            random_number = random.randint(0,16777215)
            hex_number = str(hex(random_number))
            hex_number =hex_number[2:]
            color_list.append(hex_number)
            skill_colors['ski'] = skills[_]
            skill_colors['col'] = hex_number
            list_color_pair.append({'ski': skills[_], 'col': hex_number})
        print(list_color_pair) 


        


        updated_skills.save()
        full_name = updated_skills.full_name
        phone = updated_skills.phone_number
        mobile = updated_skills.mobile_number
        address = updated_skills.address
        website = updated_skills.website
        return render(request, 'User Profile/profile.html', {'user_display':updated_skills,'user_object':updated_skills,'skills': list_color_pair,'website':website, 'name': full_name, 'phone': phone, 'mobile': mobile, 'address': address, 'assigned_projects': UserAttribs.objects.get(user=request.user).assigned_project.all()})
        


def sign_up(request):
    global user
    global signup_form
    if request.method == "POST":
        form = UserCreation(request.POST)
        if form.is_valid:
            signup_form = form
            request.session['email'] = request.POST['email']
            request.session.modified = True
            request.session['username'] = request.POST['username']
            request.session.modified = True
            request.session['password'] = request.POST['password1']
            request.session.modified = True
            user_objects = User.objects.all()
            
            for user_obj in user_objects:
                print("Username: ",user_obj.username, "Resuested username: ", request.POST['username'])
                if user_obj.username == request.POST['username']:
                    return HttpResponse("<h1>Username is already taken! Please select another username</h1>")
            return redirect('otp_verification')

        else:
            return render(request, 'Index Page/index.html', {"form":UserCreation})


    else:
        return render(request, 'Index Page/index.html', {"form":UserCreation})
    
def otp_verification(request):
    global pin
    global signup_form
    if request.method == "GET" :
        email = request.session.get('email')
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        pin = random.randint(10000, 99999)
        # s.login("collabtree.team@gmail.com", "CollabTree1234")
        # message = "Subject:{}\n\n{}".format("OTP", pin)
        # s.sendmail("collabtree.team@gmail.com",email, message)
        # s.quit()
        email_from = settings.EMAIL_HOST_USER
        pin = f'{pin}'
        recipient_list = [request.session.get('email'),]
        send_mail("OTP", pin, email_from, recipient_list)
        return render(request, "Registration/otp_form.html", {'message': ' '})
    if request.method=="POST":
        otp = request.POST['otp']
        print(type(signup_form))
        if otp==str(pin):
            print("signup_form = ",signup_form)
            print('Username = ',request.session.get('username'))
            user = User.objects.create_user(request.session.get('username'), request.session.get('email'), request.session.get('password'))
            user.save()
            new_user = UserAttribs(user=user)
            new_user.worth = 300
            new_user.phone_number = 'Empty!'
            new_user.mobile_number = 'Empty!'
            new_user.full_name = 'Empty!'
            new_user.save()
            login(request, user)
            return redirect(reverse("dashboard"))
        else:
            email = request.session.get('email')
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            pin = random.randint(10000, 99999)
            s.login("collabtree.team@gmail.com", "CollabTree1234")
            message = "Subject:{}\n\n{}".format("OTP", pin)
            s.sendmail("collabtree.team@gmail.com",email, message)
            s.quit()
            return render(request, "Registration/otp_form.html", {'message': 'Wrong OTP'}) 

my_search = ""
category = False

def dashboard(request):
    global my_search
    global category
    user_object = UserAttribs(user = request.user)
    store=""
    messages = []
    f = open("messages_data.txt","r")
    for line in f:
        line = str(line)[:-1]
        a = line.split(",")
        if a[0]==user_object.user.username and a[2]=='1':
            proj_obj = Project.objects.get(title=a[1])
            messages.append({'message': f"{a[0]} you have been accepted for {a[1]} project.", 'proj_id':proj_obj.id})
            x = list(line)
            x[-1]='0'
            store+="".join(x)+"\n"
        else:
            store+=str(line)+"\n"
    print(messages)
    f = open("messages_data.txt","w")
    f.write(store)
    f.close()
    # messages.info(request, "Info Message")


    # if request.user.is_authenticated and request.user.username != 'admin':
    if request.user.is_authenticated:
        
        if request.method == "GET" and request.GET.get('filter'):
            if category:
                items_list = []
                for i in Project.objects.all():
                    if i.category==my_search and i.status=="posted":
                        items_list.append(i)
            else:
                items_list = Project.objects.filter( Q(title__icontains=my_search, status="posted") | Q(description__icontains = my_search), Q(status="posted") ) 
                items_list = set(items_list)
                for project in Project.objects.filter(status="posted"):
                    for tag in project.tags_requirement.all():
                        if str(tag) == my_search:
                            items_list.add(project)
                            break
            if request.GET.get('filter') == 'latest':
                project_objects = sorted(items_list,key = lambda x : -x.id)
            elif request.GET.get('filter') == 'stipend':
                project_objects = sorted(items_list,key = lambda x : -x.stipend)
            elif request.GET.get('filter') == 'duration':
                project_objects = sorted(items_list,key = lambda x : -x.duration)
            # elif request.GET.get('filter') is 'latest':
            elif request.GET.get('filter') == 'relavent':
                project_objects = set()
                my_skills = UserAttribs.objects.get(user=request.user).skills
                my_skills = my_skills.split(",")
                print(my_skills)
                for project in items_list:    
                    for tag in project.tags_requirement.all():
                        if str(tag) in my_skills:
                            project_objects.add(project)
                            break
            else:
                project_objects = Project.objects.filter(status="posted")
            return render(request, 'After Login/home.html', {"project_objects" : project_objects, "flag":"true", "curr_user": UserAttribs.objects.get(user=request.user), 'message':'', 'search_message': request.GET.get('filter'), 'messages':messages })

        elif request.method == "GET" and not request.GET.get('search_input') and not request.GET.get('category_search_input'):
            my_search = ""
            category = False
            print(request.GET.get('filter'))
            if request.GET.get('filter') == 'latest':
                print("latest")
                project_objects = Project.objects.filter(status="posted").order_by('-id')
            elif request.GET.get('filter') == 'stipend':
                print("stipend")
                project_objects = Project.objects.filter(status="posted").order_by('-stipend')
            elif request.GET.get('filter') == 'duration':
                print("duration")
                project_objects = Project.objects.filter(status="posted").order_by('-duration')
            # elif request.GET.get('filter') is 'latest':
            elif request.GET.get('filter') == 'relavent':
                project_objects = set()
                my_skills = UserAttribs.objects.get(user=request.user).skills
                my_skills = my_skills.split(",")
                print(my_skills)
                for project in Project.objects.filter(status="posted"):    
                    for tag in project.tags_requirement.all():
                        if str(tag) in my_skills:
                            project_objects.add(project)
                            break
            else:
                print("default")
                project_objects = Project.objects.filter(status="posted")
             
            # for project in project_objects:
            #     print(project.applied_users.all())
            #     if project.applied_users.all()
            # print("I'm in GET")
            return render(request, 'After Login/home.html', {"project_objects" : project_objects, "flag":"true", "curr_user": UserAttribs.objects.get(user=request.user), 'message':'', 'search_message': request.GET.get('filter'), 'messages':messages })

        elif request.method=="POST" and request.POST.get("a1") and request.POST.get("a2"): # For manipulating when user applies for project by answering questions
            question_obj = Project_Question.objects.create(Q1 = request.POST["a1"])
            question_obj.Q2 = request.POST["a2"]
            question_obj.resume = request.FILES["resume"]
            question_obj.project_id = Project.objects.get(id=request.POST["project_title"])
            project_objects = Project.objects.all()
            user_obj = UserAttribs.objects.get(user=request.user)
            question_obj.answered_user = user_obj
            question_obj.project_title =  Project.objects.get(id=request.POST["project_title"]).title
            proj_obj = Project.objects.get(id=request.POST["project_title"])
            proj_obj.applied_users.add(user_obj)
            proj_obj.project_questions = question_obj
            user_obj.save()
            proj_obj.save()
            question_obj.save()
            return redirect(reverse("dashboard"))
        elif request.method == "POST" and request.POST.get("project_title"): # For displaying question form when user wants to apply for a project
            proj_obj = Project.objects.get(id = request.POST['project_title'])
            # print("I'm Here!")
            
            return render(request, 'questions.html', {"project_id" : proj_obj.id,"project" : proj_obj})
        elif request.method == "GET" and request.GET.get('search_input'):
            objects_set = set()
            items_list = Project.objects.filter( Q(title__icontains=request.GET.get('search_input'), status="posted") | Q(description__icontains = request.GET.get('search_input')), Q(status="posted") ) 
            items_list = set(items_list)
            for project in Project.objects.filter(status="posted"):
                for tag in project.tags_requirement.all():
                    print(tag,request.GET.get('search_input'))
                    if str(tag) == request.GET.get('search_input'):
                        # print("DONE")
                        items_list.add(project)
                        break
                    # else:   
            my_search = request.GET.get('search_input')
            category = False
                        # print("NO")
            # objects_set.add(items_list)
            # items_list = Project.objects.filter(description__icontains=request.GET.get('search_input'), status="posted" )
            # objects_set.add(items_list)
            # print(items_list)
            return render(request, 'After Login/home.html', {'project_objects': items_list, "curr_user": UserAttribs.objects.get(user=request.user), 'message': request.GET.get('search_input'), 'search_message': request.GET.get('search_input'), 'messages':messages})
        elif request.method == "GET" and request.GET.get('category_search_input'):
            objects_set = set()
            # items_list = Project.objects.filter( Q(title__icontains=request.GET.get('category_search_input'), status="posted") | Q(description__icontains = request.GET.get('category_search_input')), Q(status="posted") | Q(category = request.GET.get('category_search_input')), Q(status="posted") ) 
            a = []
            for i in Project.objects.all():
                if i.category==request.GET.get('category_search_input') and i.status=="posted":
                    a.append(i)
            my_search = request.GET.get('category_search_input')
            category = True
            # objects_set.add(items_list)
            # items_list = Project.objects.filter(description__icontains=request.GET.get('search_input'), status="posted" )
            # objects_set.add(items_list)
            # print("HEy")
            # print(request.GET.get('category_search_input'))
            # print(items_list)
            return render(request, 'After Login/home.html', {'project_objects': a, "curr_user": UserAttribs.objects.get(user=request.user), 'message': request.GET.get('category_search_input'), 'search_message': request.GET.get('category_search_input'), 'messages':messages})
            

    else:
        return HttpResponse('<h1>Please Login</h1>')

def blog(request):
    if request.method == "GET" and request.GET.get('search_input'):
        objects_set = set()
        items_list = Blog.objects.filter( Q(title__icontains=request.GET.get('search_input')) | Q(body__icontains = request.GET.get('search_input'))) 
        items_list = set(items_list)
        for blog in Blog.objects.all():
            for tag in blog.tags.all():
                if str(tag)==request.GET.get("search_input"):
                    items_list.add(blog)
                    break
        # objects_set.add(items_list)
        # items_list = Project.objects.filter(description__icontains=request.GET.get('search_input'), status="posted" )
        # objects_set.add(items_list)
        
        return render(request, 'Blog Section/blog.html', {'blog_objects': items_list, "curr_user": UserAttribs.objects.get(user=request.user), 'message': request.GET.get('search_input'), 'messages':messages})
    else:
        blog_objects = Blog.objects.all().order_by('-date_time')
        # blog_objects = blog_objects[:9]
        # print(blog_objects)
        # for i in blog_objects:
        #     print(i.tags.all())
        return render(request, 'Blog Section/blog.html', {"blog_objects" : blog_objects})

def new_blog(request):
    if request.method == "GET":
        return render(request,'Blog Section/new_blog.html')
    elif request.method == "POST" and request.POST.get('title') and request.POST.get('body') and request.POST.get("tags"):
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
    else:
        return HttpResponse("<h1>Invalid Fields/Empty Fields detected!</h1>")

def my_projects(request, message=None):
    project_objects = Project.objects.all()
    project_list=[]
    for project in project_objects:
        if project.owner == UserAttribs.objects.get(user=request.user):
            # print(project.id)
            # proj_obj = Project.objects.get(id=project.id)
            applied_users = project.applied_users.all()
            # print("Applied users"+str(applied_users))
            project_list.append({'project':project,'applied_users':applied_users})
    # print(project_list)
    # print(project_list)
    return render(request, 'My Projects/myProjects.html' ,{'project_list': project_list})

def project_form(request):
    if request.method == "GET":
        user_obj = UserAttribs.objects.get(user=request.user)
        return render(request,'My Projects/project_form.html', {'user_obj': user_obj})
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
        project_object.status = "posted"
        project_object.category = request.POST['category']
        tags = request.POST['tags']
        for tag in tags.split(','):
            print(type(tag))
            project_object.tags_requirement.add(tag.lower())
        print(project_object.tags_requirement)
        owner_object.worth-=stipend
        project_object.save()
        owner_object.save()
        return redirect(reverse("dashboard"))
        
def assign_user(request, id, proj_id):
    print("In assign_user")
    user_obj = UserAttribs.objects.get(id=id)
    proj_obj = Project.objects.get(id=proj_id)

    proj_obj.assigned_user = user_obj
    proj_obj.status="assigned"
    user_obj.assigned_project.add(proj_obj)
    f = open("messages_data.txt","a")
    f.write(str(user_obj.user.username)+","+str(proj_obj.title)+","+str(1)+"\n")
    f.close()     
    print(user_obj.assigned_project.all())
    proj_obj.save()
    return redirect(reverse("my_projects"))


def view_user(request, id=None, proj_id=None):
    question_objs = Project_Question.objects.all()
    print(question_objs)
    for q_obj in question_objs:
        if q_obj.answered_user:
            if proj_id==q_obj.project_id.id and q_obj.answered_user.id==id:
                # print("q_obj.answered_user: ", q_obj.answered_user.id, q_obj.Q1, q_obj.Q2, q_obj.project_id, q_obj.project_title, proj_id)
                return render(request, "My Projects/view_user.html", {'q_user_obj':q_obj})

def mark_complete(request, user_id, project_id):
    if request.method == "GET":
        project_obj = Project.objects.get(id=project_id)

        return render(request, "My Projects/review.html", {'proj_obj': project_obj})
    else:
        rating = request.POST['rating']
        review = request.POST['review']
        print("User_id = ",user_id,"Project_id = ",project_id)
        user_obj = UserAttribs.objects.get(id = user_id)
        project_obj = Project.objects.get(id=project_id)
        project_obj.status = "complete"
        project_obj.project_rating = rating
        project_obj.review = review
        print("User Object = ",user_obj)
        if user_obj.worth is None:
            user_obj.worth = 0
            user_obj.save()
        user_obj.worth += project_obj.stipend
        print("Worth = ",user_obj.worth)
        # curr_user = UserAttribs.objects.get(user=request.user)
        # curr_user.worth -= project_obj.stipend
        user_obj.save()
        # curr_user.save()
        project_obj.status = 'completed'
        project_obj.save()
        return redirect(reverse("my_projects"))
def view_project(request, proj_id):
    proj_obj = Project.objects.get(id = proj_id)
    return render(request, 'My Projects/project_info.html', {'project': proj_obj, "curr_user": UserAttribs.objects.get(user=request.user)})

def view_blog(request, blog_id):
    blog_obj = Blog.objects.get(id=blog_id)
    return render(request, 'Blog Section/view_blog.html', {'blog': blog_obj})
def like_blog(request, blog_id):
    blog_obj = Blog.objects.get(id=blog_id)
    blog_obj.likes += 1
    blog_obj.save()
    return render(request, 'Blog Section/view_blog.html', {'blog': blog_obj})
def dislike_blog(request, blog_id):
    blog_obj = Blog.objects.get(id=blog_id)
    blog_obj.dislikes += 1
    blog_obj.save()
    return render(request, 'Blog Section/view_blog.html', {'blog': blog_obj})
def my_blogs(request):
    user_obj = UserAttribs.objects.get(user = request.user)
    blog_objs = Blog.objects.filter(author = user_obj)
    return render(request, 'Blog Section/my_blogs.html', {'blog_objects': blog_objs})
def delete_blog(request, blog_id):
    user_obj = UserAttribs.objects.get(user = request.user)
    Blog.objects.filter(id=blog_id).delete()
    blog_objs = Blog.objects.filter(author = user_obj)
    return render(request, 'Blog Section/my_blogs.html', {'blog_objects': blog_objs})

def edit_blog(request, blog_id):
    if request.method == "GET":
        blog_obj = Blog.objects.get(id=blog_id)
        tags = ""
        for tag in blog_obj.tags.all():
            tags = tags+','+ str(tag)
        return render(request, 'Blog Section/edit_blog.html', {'blog_obj': blog_obj, 'tags': tags})
    else:
        blog_obj = Blog.objects.get(id=blog_id)
        blog_obj.title = request.POST['title']
        blog_obj.body = request.POST['body']
        if request.FILES.get('cover_image'):
            blog_obj.cover_image = request.FILES['cover_image']
        tags = request.POST['tags']
        for tag in tags.split(','):
            blog_obj.tags.add(tag)
        blog_obj.save()
        return render(request, 'Blog Section/view_blog.html', {'blog': blog_obj})
        


        