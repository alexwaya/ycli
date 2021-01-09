from django.contrib import admin
from .models import Workshop, Application

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

class ApplicationAdmin(admin.ModelAdmin):
	pass

#admin.site.register(Post, PostAdmin)
#admin.site.register(Program, ProgramAdmin)
admin.site.register(Application, ApplicationAdmin)
