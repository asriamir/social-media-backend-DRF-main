from django.contrib import admin
from .models import Post
from django.utils.html import format_html

class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "short_content", "image_tag", "created_at") 
    list_filter = ("created_at", "user")  
    search_fields = ("content", "user__email")  
    ordering = ("-created_at",)  
    readonly_fields = ("created_at",)  
    
    def short_content(self, obj):
        """ نمایش کوتاه‌شده‌ی محتوای پست """
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
    short_content.short_description = "محتوا"

    def image_tag(self, obj):
        """ نمایش تصویر پست در پنل ادمین """
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:5px;" />', obj.image.url)
        return "بدون تصویر"
    image_tag.short_description = "تصویر"

admin.site.register(Post, PostAdmin)
