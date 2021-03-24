from django.db import models
from django.contrib.auth.models import User

class UserAttribs(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    job_title = models.CharField(max_length=100, blank=True)
    skills = models.CharField(max_length=1000,blank=True)

    def __str__(self):
        return self.user.username

