from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *



# Register your models here.
class AccountAdmin(UserAdmin):
    list_display=('EmailAddress','FirstName', 'LastName','Userrole','is_active','is_admin','date_modified')
    search_fields=('EmailAddress',)
    readonly_fields=('UserID','date_joined',)

    filter_horizontal=()
    list_filter=()
    fieldsets=()
    ordering = ('EmailAddress',)


admin.site.site_header = "Users_AdminPage"
admin.site.register(CustomUser,AccountAdmin)

