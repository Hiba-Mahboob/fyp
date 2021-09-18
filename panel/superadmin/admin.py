from django.contrib import admin
from .models import DeptUni, User, QueryHistory
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
                    'is_member',
                    'is_university',
                    'is_department'
                )
            }
        )
    )

# Register your models here.
admin.site.register(User, CustomUserAdmin)
admin.site.register(QueryHistory)
admin.site.register(DeptUni)