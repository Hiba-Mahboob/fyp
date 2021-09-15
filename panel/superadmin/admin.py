from django.contrib import admin
from .models import User
from .forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model=User
    add_form=UserCreationForm

    fieldsets=(
        *UserAdmin.fieldsets,
        (
            'User role',
            {
                'fields':(
                    'is_student',
                    'is_super_admin',
                    'is_member'
                )
            }
        )
    )

# Register your models here.
admin.site.register(User, CustomUserAdmin)