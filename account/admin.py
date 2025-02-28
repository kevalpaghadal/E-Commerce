from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name' , 'last_name' ,'username' , 'last_login', 'is_active' , 'join_date')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login' ,'join_date')
    ordering = ('-join_date',)


    filter_horizontal = ()
    list_filter = () 
    fieldsets = () # this is user for readonly 

admin.site.register(Account, AccountAdmin)