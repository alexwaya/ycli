from django.db import models

# class Category(models.Model):
#     name = models.CharField(max_length=20)

#     class Meta:
#         verbose_name = "Event Name"

#     def __str__(self):
#         return self.name

class Workshop(models.Model):
	
	title = models.CharField(max_length=255)
	location = models.CharField(max_length=255)
	date_from = models.DateTimeField()
	date_to = models.DateTimeField()
	photo = models.ImageField(upload_to='images/', default='attach photo')
	description = models.TextField()

	created_at = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Our Workshop"



class Application(models.Model):
	workshop = models.ForeignKey(Workshop, related_name='workshops', on_delete=models.CASCADE)

	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)

	country = models.CharField(max_length=255)

	# content = models.TextField()
	# experience = models.TextField()

	#created_by = models.ForeignKey(CustomUser, related_name='applications', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "Workshop Registration"



class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Workshop', on_delete=models.CASCADE)