from django.shortcuts import render, redirect
from .models import Content, Gallery, Home_galley
from .forms import ContactForm

from django.core.mail import EmailMessage, send_mail
# from django.shortcuts import get_object_or_404
# from django.http import HttpResponse
# from django.contrib import messages
# Create your views here.

def site_content(request):
    contents = Content.objects.all()
    home_gallery = Home_galley.objects.all()
    context = {'contents':contents, 'home_gallery':home_gallery}
    
    return render(request, 'index.html', context)

def gallery_content(request):
    gallery = Gallery.objects.all()

    return render(request, 'gallery.html', {'gallery':gallery})

def about(request):
    contents = Content.objects.all()
    return render(request, 'about.html', {'contents':contents})

def services(request):
    contents = Content.objects.all()
    return render(request, 'services.html', {'contents':contents})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

           

        #     EmailMessage(
        #        'Contact Form Submission from {}'.format(name)+". Subject: "+subject,
        #        message,
        #        'email@infohridayam.com', # Send from (your website)
        #        ['email@infohridayam.com', 'rohitaswchoudhary@gmail.com'], # Send to (your admin email)
        #        [],
        #        reply_to=[email] # Email from the form to get back to
        #    ).send()
            return render(request, 'success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)

def success(request):
    return render(request, 'index.html')

