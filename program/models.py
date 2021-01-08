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
	title = models.CharField(max_length=255)
	location = models.CharField(max_length=255)
	date_from = models.DateTimeField()
	date_to = models.DateTimeField()
	photo = models.ImageField(upload_to='images/', default='attach photo')
	description = models.TextField()

	categories = models.CharField(choices=PROGRAM_TYPES, max_length=255, default='Kitui')

	created_by = models.ForeignKey(CustomUser, related_name='programs', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	changed_at = models.DateTimeField(auto_now=True)


class Application(models.Model):
	program = models.ForeignKey(Program, related_name='applications', on_delete=models.CASCADE)

	content = models.TextField()
	experience = models.TextField()

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