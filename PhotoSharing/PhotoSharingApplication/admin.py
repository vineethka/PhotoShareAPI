from django.contrib import admin
from PhotoSharingApplication.models import Categories


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name', 'image']}),
        ('Date information', {'fields': ['created_at', 'updated_at']}),
    ]
    search_fields = ['name']
    list_filter = ['created_at']
    list_display = ('name', 'image_link')


admin.site.register(Categories, CategoryAdmin)
