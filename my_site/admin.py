from django.contrib import admin
from .models import ProjectImages, ProfileImages, PosterImages, ContactForm

# Register your models here.
admin.site.register(ProfileImages)
admin.site.register(ProjectImages)
admin.site.register(PosterImages)
admin.site.register(ContactForm)
