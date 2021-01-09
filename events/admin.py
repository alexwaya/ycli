from django.contrib import admin
from .models import Event, Application

class EventAdmin(admin.ModelAdmin):
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


admin.site.register(Event, EventAdmin)
admin.site.register(Application, ApplicationAdmin)
