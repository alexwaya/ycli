from django.contrib import admin
from .models import Donation

class DonationAdmin(admin.ModelAdmin):
	list_display = [

    		'fname', 
        	'lname',
        	'email', 
        	'phone', 
        	'type_of_donation', 
        	'amount', 

    ]


admin.site.register(Donation, DonationAdmin)