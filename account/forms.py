import re
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.forms import EmailField, ModelForm, ValidationError
from django.db import models
from django.contrib.auth.hashers import check_password

class SigninForm(AuthenticationForm):
    class Meta:
        model = Profile
        fields = [
            'email',
            'password',
        ]

    def clean(self):
        email = self.cleaned_data.get('username')
        input_password = self.cleaned_data.get('password')
        find_user = Profile.objects.filter(email=email)
        print(email)
        hashed_password = find_user.get(email=email).password
        
        if not re.fullmatch(r'[\w\d\_\-]+@[A-z]+\.[A-z]+', email):
            raise ValidationError('잘못된 이메일 형식입니다.')
        if not find_user.exists():
            raise ValidationError('없는 회원 정보입니다.')
        if not check_password(input_password, hashed_password):
            raise ValidationError('회원정보가 일치하지 않습니다. 이메일과 비밀번호를 확인하세요.')
            
        return self.cleaned_data

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