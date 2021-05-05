from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# from backend.models import UserAttribs



class UserAttribs(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    worth = models.IntegerField(blank=True, null=True, default='0')
    job_title = models.CharField(max_length=100, blank=True)
    skills = models.CharField(max_length=1000,blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    mobile_number = models.CharField(max_length=12,blank=True)
    full_name = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    website = models.URLField(max_length=100, blank=True)
    github = models.CharField(max_length=200, blank=True)
    twitter = models.CharField(max_length=200, blank=True)
    instagram = models.CharField(max_length=200, blank=True)
    facebook = models.CharField(max_length=200, blank=True)
    user_image = models.ImageField(upload_to="images" ,blank=True)
    assigned_project = models.ManyToManyField('Project', blank=True, null=True)
    # applied_projects = models.ForeignKey('Project', on_delete = models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.user.username

    
class Blog(models.Model):
    title = models.CharField(max_length=100,blank=True)
    body = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to="blog_images", blank=True) 
    author = models.ForeignKey(UserAttribs, on_delete = models.CASCADE, blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title


class Project_Question(models.Model):
    answered_user = models.ForeignKey(UserAttribs, on_delete = models.CASCADE, blank=True, null=True)
    project_id = models.ForeignKey("Project", on_delete=models.CASCADE,null=True, blank=True)
    project_title = models.CharField(max_length=200,blank=True)
    resume = models.FileField(upload_to="resumes",blank=True)
    Q1 = models.TextField(blank=True)
    Q2 = models.TextField(blank=True)
    def __str__(self):
        return self.project_title

class Project(models.Model):
    category = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=200,blank=True)
    description = models.TextField(max_length=400,blank=True)
    owner = models.ForeignKey(UserAttribs, on_delete = models.CASCADE, related_name="owner")
    duration = models.IntegerField(blank=True, null=True)
    assigned_user = models.ForeignKey(UserAttribs, on_delete = models.CASCADE, related_name="assigned_user", null=True, blank=True)
    stipend = models.IntegerField(blank=True, null=True)
    applied_users = models.ManyToManyField(UserAttribs,  null=True, blank=True)
    tags_requirement = TaggableManager()
    project_questions = models.OneToOneField(Project_Question,on_delete=models.CASCADE,null=True, blank=True)
    project_rating = models.FloatField(blank=True, default=0)
    review = models.TextField(blank=True)
    def __str__(self):
        return self.title


