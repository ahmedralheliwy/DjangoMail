from django.db import models

# Create your models here.
class MailModel(models.Model):
    to=models.EmailField(max_length=254,null=False,blank=False)   
    subject=models.CharField(max_length=100,null=False,blank=False)
    message=models.TextField(max_length=1000,null=False,blank=False)