from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    org_name     = models.CharField(max_length=30, default="Organization", help_text='Organization Name.')
    
    #company contact details
    org_email		= 	models.CharField(max_length=100)
    org_phone		= 	models.CharField(max_length=100)
    org_website		= 	models.CharField(max_length=100)
    org_address		= 	models.CharField(max_length=100)
    org_city		= 	models.CharField(max_length=100)
    org_country		= 	models.CharField(max_length=100)

    #Primary Contact Person
    person_name 		= models.CharField(max_length=100)
    person_org_title	= 	models.CharField(max_length=100, default="Director")
    person_email		= 	models.CharField(max_length=100)
    person_phone		= 	models.CharField(max_length=100, default="0712345067")

    #Number of staff in your organization.
    staff_no	= 	models.CharField(max_length=100)

    #Organization type
    org_type	= 	models.CharField(max_length=100)

    #What is your organization's mission statement
    mission		= 	models.TextField(max_length=100)

    #What is your organization's main area of focus? 
    area_of_focus	= models.CharField(max_length=100)

    #categories 		= models.CharField(max_length=20, default="Kitui")
    date_joined    	= models.DateTimeField(verbose_name="date Joined", auto_now_add=True)

    def __str__(self):
        return self.org_name


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('CustomUser', on_delete=models.CASCADE)