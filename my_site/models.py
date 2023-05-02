from django.db import models

# Create your models here.
class ProfileImages(models.Model):
    profile_images = models.ImageField(upload_to='profile_image')
    
class ProjectImages(models.Model):
    project_images = models.ImageField(upload_to='project_images')
    description = models.TextField(db_column='About', null=True)
    title = models.CharField(max_length=100, blank=True)

class PosterImages(models.Model):
    poster_images = models.ImageField(upload_to='poster_images')

class ContactForm(models.Model):
    name = models.CharField(max_length=100, blank=False)
    subject = models.CharField(max_length=150, blank=False)
    Email = models.EmailField(max_length=100, blank=False)
    message = models.TextField(max_length=1200, blank=False)

