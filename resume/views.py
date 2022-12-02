from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'resume/index.html')

def skills_projects(request):
    return render(request, 'resume/skills&projects.html')

def contact(request):
    if request.method == 'POST':
        new_message = Message(
            name = request.POST['name'],
            email = request.POST['email'],
            phone_number = request.POST['number'],
            description = request.POST['message'],
        )
        new_message.save()
        messages.success(request, "Message sent successfully!")
        return redirect('index')

    return render(request, 'resume/contact.html')

