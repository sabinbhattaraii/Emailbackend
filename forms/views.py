from django.shortcuts import render
from .forms import CustomUserForm
from .models import CustomUser

from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.

def custom_create_view(request):
    form = CustomUserForm(request.POST,request.FILES )
    if form.is_valid():
        name = form.cleaned_data['Name']
        message = form.cleaned_data['Message']
        age = form.cleaned_data['Age']
        email_from = settings.EMAIL_HOST_USER
        video = request.FILES['Video']
        recipient_list = form.cleaned_data['Email']
        
        email_message = f"{message} \n Your age is {age}"

        mail = EmailMessage(name,email_message,email_from,[recipient_list])
        mail.attach(video.name,video.read(),video.content_type)
        mail.send()

        form.save()
    context = {
        'form':form
    }
    return render(request,'user_create.html',context)
