from django.db import models
from django.contrib.auth.models import User

class UserAttribs(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    job_title = models.CharField(max_length=100, blank=True)
    skills = models.CharField(max_length=1000,blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    mobile_number = models.CharField(max_length=12,blank=True)
    full_name = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    website = models.URLField(max_length=100, blank=True)
    user_image = models.ImageField(upload_to="images" ,blank=True)
    def __str__(self):
        return self.user.username
    
class Blog(models.Model):
    title = models.CharField(max_length=100,blank=True)
    body = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to="blog_images", blank=True) 
    author = models.ForeignKey(UserAttribs, on_delete = models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200,blank=True)
    description = models.TextField(max_length=400,blank=True)
    owner = models.ForeignKey(UserAttribs, on_delete = models.CASCADE, related_name="owner")
    duration = models.IntegerField(blank=True)
    assigned_user = models.OneToOneField(UserAttribs, on_delete = models.CASCADE, related_name="assigned_user", null=True, blank=True)
    stipend = models.IntegerField(blank=True)
    def __str__(self):
        return self.title



