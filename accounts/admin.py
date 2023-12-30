from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# newspaperappadmin
# newspaperappadmin@gmail.com
# newspaperappadmin12345

# testuser3
# Testuser1234512345 # new Testuser5432154321 # Testuser31234512345

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff', ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )
    add_fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
