from django.contrib import admin
from .models import Workshop

class WorkshopAdmin(admin.ModelAdmin):
    list_display = [

    		'title',
    		'location',
    		'date_from',
    		'date_to',
        	'created_at', 
    ]

# class CategoryAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Workshop, WorkshopAdmin)
#admin.site.register(Category, CategoryAdmin)