from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = ("id", "email", "name", "profile_image", "profile_views", "is_staff", "is_active") 
    list_filter = ("is_staff", "is_active") 
    search_fields = ("email", "name")  
    ordering = ("id",)
    readonly_fields = ("profile_views",)  

    fieldsets = (
        ("اطلاعات اصلی", {"fields": ("email", "name", "password")}),
        ("اطلاعات پروفایل", {"fields": ("bio", "avatar", "profile_views")}),
        ("دسترسی‌ها", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        ("ایجاد کاربر جدید", {
            "classes": ("wide",),
            "fields": ("email", "name", "password1", "password2"),
        }),
    )

    def profile_image(self, obj):
        """ نمایش عکس پروفایل در لیست کاربران """
        if obj.avatar:
            return format_html('<img src="{}" width="50" style="border-radius: 50%;" />'.format(obj.avatar.url))
        return "بدون عکس"

    profile_image.short_description = "عکس پروفایل"

admin.site.register(User, UserAdmin)
