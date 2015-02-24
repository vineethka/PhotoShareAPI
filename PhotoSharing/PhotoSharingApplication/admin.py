from django.contrib import admin
from PhotoSharingApplication.models import Categories


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'image', 'created_at', 'updated_at']
    search_fields = ['name']
    list_display = ('name', 'image_link')


admin.site.register(Categories, CategoryAdmin)
