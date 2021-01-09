from django.contrib import admin
from .models import Program, Application


class ProgramAdmin(admin.ModelAdmin):
    list_display = [

    		'title',
    		'location',
    		'date_from',
    		'date_to',
        	'created_at', 
    ]

class ApplicationAdmin(admin.ModelAdmin):
    list_display = [

		'full_name',
		'company',

		'email',
		'website',
    	'country',

    	'city',
]


admin.site.register(Program, ProgramAdmin)
admin.site.register(Application, ApplicationAdmin)
