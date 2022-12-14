from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = (
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
                    'pet_date_of_birth',
                    'is_admin',
                    'is_active',
                    'is_superuser',
                )
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password')}),
        ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':
                (
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
                    'pet_date_of_birth',
                    'password1',
                    'password2'
                )}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)