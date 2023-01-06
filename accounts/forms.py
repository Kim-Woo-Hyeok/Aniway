from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'name',
            'university',
            'department',
            'gender',
            'phone',
            'date_of_birth',
            'pet_name',
            'pet_gender',
            'pet_breed',
            'pet_weight',
            'pet_neuter',
            'pet_date_of_birth'
        )
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        password1 = self.cleaned_data.get("password1")
        name = self.cleaned_data.get("name")
        university = self.cleaned_data.get("university")
        department = self.cleaned_data.get("department")
        gender = self.cleaned_data.get("gender")
        phone = self.cleaned_data.get("phone")
        date_of_birth = self.cleaned_data.get("date_of_birth")
        pet_name = self.cleaned_data.get("pet_name")
        pet_gender = self.cleaned_data.get("pet_gender")
        pet_breed = self.cleaned_data.get("pet_breed")
        pet_weight = self.cleaned_data.get("pet_weight")
        pet_neuter = self.cleaned_data.get("pet_neuter")
        pet_date_of_birth = self.cleaned_data.get("pet_date_of_birth")
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.email = email
            user.name = name
            user.university = university
            user.department = department
            user.gender = gender
            user.phone = phone
            user.date_of_birth = date_of_birth
            user.pet_name = pet_name
            user.pet_gender = pet_gender
            user.pet_breed = pet_breed
            user.pet_weight = pet_weight
            user.pet_neuter = pet_neuter
            user.pet_date_of_birth = pet_date_of_birth
            user.set_password(password1)
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'date_of_birth',
                  'is_active', 'is_admin', 'is_superuser')

    def clean_password(self):
        return self.initial["password"]


