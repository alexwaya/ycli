from django.contrib import admin
from .models import Program, Application

# class PostAdmin(admin.ModelAdmin):
#     pass

class ProgramAdmin(admin.ModelAdmin):
    list_display = [

    		'title',
    		'location',
    		'date_from',
    		'date_to',
        	'created_at', 
    ]

class ApplicationAdmin(admin.ModelAdmin):
	pass

#admin.site.register(Post, PostAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Application, ApplicationAdmin)
