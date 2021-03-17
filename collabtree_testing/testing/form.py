from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserCreation(UserCreationForm):
    job_title = forms.CharField(max_length=100, required=True)
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', 'job_title')