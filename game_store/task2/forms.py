# task5/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegister(forms.Form):
    username = forms.CharField(
        label="Введите логин",
        max_length=30,
        widget=forms.TextInput(attrs={'placeholder': 'Логин'})
    )
    password = forms.CharField(
        label="Введите пароль",
        min_length=8,
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'})
    )
    repeat_password = forms.CharField(
        label="Повторите пароль",
        min_length=8,
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'})
    )
    age = forms.IntegerField(
        label="Введите свой возраст",
        min_value=0,
        max_value=999,
        widget=forms.NumberInput(attrs={'placeholder': 'Возраст'})
    )


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Электронная почта")
    age = forms.IntegerField(
        label="Введите свой возраст",
        min_value=0,
        max_value=999,
        widget=forms.NumberInput(attrs={'placeholder': 'Возраст'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'age', 'password1', 'password2']
