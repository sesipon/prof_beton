from django import forms
from django.core.validators import RegexValidator

from .models import User

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password']
        labels = {'username': 'Имя пользователя', 'email': 'Эл.почта',
                  'phone_number': 'Номер телефона', 'password': 'Пароль'}

class UserLoginForm(forms.Form):
    phone_number = forms.CharField(label='Номер телефона', max_length=15) #r"^+?1?\d{8,15}$"
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

