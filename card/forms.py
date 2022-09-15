from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")


# class Card(forms.Form):
#     user = forms.EmailField(max_length=50)
#     name = forms.CharField(max_length=50)
#     name_color = forms.CharField(max_length=50)
#     content1 = forms.CharField(max_length=50)
#     content2 = forms.CharField(max_length=50)
#     business_name = forms.CharField(max_length=50)
#     profile_img = forms.ImageField(max_length=50)
#     business_name_color = forms.CharField(max_length=50)
#     content1_color = forms.CharField(max_length=50)
#     content2_color = forms.CharField(max_length=50)
#
#     class Meta:
#         model = User
#         fields = ("user", "name", "name_color", "content1")
#



