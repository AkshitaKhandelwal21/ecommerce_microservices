from django.contrib import admin
from auths.models import Users

# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    model = Users
    list_display = ['email', 'username', 'is_staff']
    fieldsets = [
        (
            'Personal', {
                "fields": ['first_name', 'last_name', 'email', 'phone', 'roles']
            }
        ),
        (
            'Additional', {
                "fields": ['is_staff', 'is_active', 'is_superuser', 'date_joined']
            }
        ),
    ]


admin.site.register(Users, UsersAdmin)