from django.db import models

# Create your models here.
class Index(models.Model):
    name =  models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    paddress = models.CharField(max_length=200, null=True, blank=True)  
    tempaddr = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    social_media = models.CharField(max_length=200, null=True, blank=True)
    about = models.TextField(max_length=500, null=True, blank=True)
    skills = models.TextField(max_length=500, null=True, blank=True)
    experience = models.TextField(max_length=500, null=True, blank=True)
    awards = models.TextField(max_length=500, null=True, blank=True)
    interest = models.TextField(max_length=500, null=True, blank=True)
 
    def __str__(self):
        return self.name