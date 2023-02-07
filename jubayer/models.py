from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    desc = models.TextField(null=True)