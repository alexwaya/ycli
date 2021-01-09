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


class ApplicationAdmin(admin.ModelAdmin):
		    list_display = [

		'name',
		'email',
		
		'phone',
		'country',
		
]


admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Application, ApplicationAdmin)
