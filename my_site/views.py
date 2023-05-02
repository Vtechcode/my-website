from django.shortcuts import render
from .models import ProfileImages, ProjectImages, PosterImages, ContactForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        customer_contact = ContactForm(name=name, subject=subject, Email=email, message=message)
        customer_contact.save()


    profile = ProfileImages.objects.all
    projects = ProjectImages.objects.all
    posters = PosterImages.objects.all
    items = [profile, projects, posters]
    return render(request, 'index.html', {'display':items})