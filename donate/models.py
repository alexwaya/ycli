from django.db import models

# Create your models here.
class Donation(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    phone = models.CharField(max_length=100)
    type_of_donation = models.CharField(max_length=100)
    amount = models.CharField(max_length=50,default='$100')
    comments = models.TextField(max_length=1024, blank=True)

    def __str__(self):
        return self.fname