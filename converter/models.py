from django.db import models
from django import forms

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class UploadCSV(models.Model):
    csv_file_name = models.CharField(max_length=256)
    sql_file_name = models.CharField(max_length=256)
    document = models.FileField(upload_to='upload/')
