from .models import Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.forms import ModelForm
from django.db import models

class SigninForm(AuthenticationForm):
    class Meta:
        model = Profile
        fields = [
            'email',
            'password',
        ]
        
class SignupForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = [
            'username',
            'last_name',
            'first_name',
            'email',
            'password1',
            'password2',
            'bio',
        ]