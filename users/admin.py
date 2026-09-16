from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'first_name',
        'middle_name',
        'last_name',
        'email',
        'mobile',
        'address',
        'created_at',
        'updated_at',
    ]


admin.site.register(User, UserAdmin)