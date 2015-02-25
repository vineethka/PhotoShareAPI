from django.contrib import admin
from PhotoSharingApplication.models import Categories, Pictures


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'image']}),
        ('Date information', {'fields': ['created_at', 'updated_at']}),
    ]
    search_fields = ['name']
    list_filter = ['created_at']
    list_display = ('name', 'image_src')

class PictureAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'image', 'category']}),
        ('Date information', {'fields': ['created_at', 'updated_at']}),
    ]
    search_fields = ['name']
    list_filter = ['created_at']
    list_display = ('name', 'thumb_image_src')



admin.site.register(Categories, CategoryAdmin)
admin.site.register(Pictures, PictureAdmin)

