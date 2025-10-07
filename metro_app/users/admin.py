from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'address', 'photo')
    search_fields = ('full_name', 'email')
    list_filter = ('full_name',)
    fields = ('full_name', 'email', 'address', 'photo')
    list_per_page = 20
