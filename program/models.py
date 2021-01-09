from accounts.models import CustomUser
from django.db import models

# from tinymce.models import HTMLField

PROGRAM_TYPES = [

    ('Youth Programs for organizations', 'Youth Programs for organizations'),

    ('Capacity Building for youth Networks and Movements', 'Capacity Building for youth Networks and Movements'),
    
    ('Youth for Culture and Heritage', 'Youth for Culture and Heritage'),
    
    ('YCLI Mentorship Program', 'YCLI Mentorship Program'),

    ('Leadership Training Programs', 'Leadership Training Programs'),

    ]


class Program(models.Model):
	title = models.CharField(max_length=255, verbose_name = "Name of Program")
	location = models.CharField(max_length=255)
	date_from = models.DateTimeField()
	date_to = models.DateTimeField()
	photo = models.ImageField(upload_to='images/', default='attach photo')
	description = models.TextField()

	categories = models.CharField(choices=PROGRAM_TYPES, max_length=255, default='Kitui')

	#created_by = models.ForeignKey(CustomUser, related_name='programs', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	changed_at = models.DateTimeField(auto_now=True)


class Application(models.Model):
	program = models.ForeignKey(Program, related_name='applications', on_delete=models.CASCADE)

	full_name = models.CharField(max_length=255, verbose_name = "Full Name")
	company = models.CharField(max_length=255, verbose_name = "Company Name")
	email = models.CharField(max_length=255, verbose_name = "Email Address")
	website = models.CharField(max_length=255, verbose_name = "Website Link")

	country = models.CharField(max_length=255, verbose_name = "Country")
	city = models.CharField(max_length=255,verbose_name = "City/Region/State")

	description = models.TextField(verbose_name = "Description of your youth programs")
	importance = models.TextField(verbose_name = "Why is the program you are applying for important to you?")

	photo = models.ImageField(upload_to='images/', default='attach photo')

	created_by = models.ForeignKey(CustomUser, related_name='applications', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	#changed_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    #categories = models.CharField(max_length=20, default="cat")


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)