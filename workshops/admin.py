from django.contrib import admin
from .models import Workshop

class WorkshopAdmin(admin.ModelAdmin):
    pass

# class CategoryAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Workshop, WorkshopAdmin)
#admin.site.register(Category, CategoryAdmin)