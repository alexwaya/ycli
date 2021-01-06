from django.db import models

# class Category(models.Model):
#     name = models.CharField(max_length=20)

#     class Meta:
#         verbose_name = "Event Name"

#     def __str__(self):
#         return self.name

class Event(models.Model):
	
	photo = models.ImageField(upload_to='images/', default='attach photo')
	title = models.CharField(max_length=1024, verbose_name = "Event's Name")
	#categories = models.ManyToManyField('Category', related_name='posts', verbose_name = "Event Name")
	description = models.TextField()

	created_on = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Our Event"

    #categories = models.ManyToManyField('NewsCategory', related_name='posts', verbose_name = "County")


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Event', on_delete=models.CASCADE)