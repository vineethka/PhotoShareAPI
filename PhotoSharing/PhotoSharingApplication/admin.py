from django.contrib import admin
from PhotoSharingApplication.models import Categories, Pictures


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'image']}),
    ]
    search_fields = ['name']
    list_filter = ['created_at']
    list_display = ('name', 'image_src', 'created_at', 'updated_at')
    change_list_template = "admin/change_list_filter_sidebar.html"
    change_list_filter_template = "admin/filter_listing.html"


class PictureAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'image']}),
        ('Belongs to',       {'fields': ['user', 'category']}),

    ]
    search_fields = ['name', 'category__name', 'user__user__username']
    list_filter = ['created_at', 'category__name', 'user__user__username']
    list_display = ('name', 'thumb_image_src', 'category', 'user', 'created_at', 'updated_at')
    # change_list_template = "admin/change_list_filter_sidebar.html"
    # change_list_filter_template = "admin/filter_listing.html"



admin.site.register(Categories, CategoryAdmin)
admin.site.register(Pictures, PictureAdmin)

