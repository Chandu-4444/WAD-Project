from backend.models import UserAttribs
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserCreation(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

        