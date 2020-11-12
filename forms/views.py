from django.shortcuts import render
from .forms import CustomUserForm
from .models import CustomUser

from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings

from PIL import Image
from io import BytesIO

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter,A4


# Create your views here.
"""def createPDF(request,data):
    buffer=BytesIO()
    c =canvas.Canvas(buffer, pagesize=A4)
    c.drawString(100,800,data)
    c.drawString
    c.showPage()
    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    return pdf"""

def custom_create_view(request):
    form = CustomUserForm(request.POST,request.FILES )
    if form.is_valid():
        name = form.cleaned_data['Name']
        message = form.cleaned_data['Message']
        age = form.cleaned_data['Age']
        phone = form.cleaned_data['Phone']
        email_from = settings.EMAIL_HOST_USER
        video = request.FILES['Video']
        recipient_list = form.cleaned_data['Email']

        buffer=BytesIO()
        c =canvas.Canvas(buffer, pagesize=A4)
        c.drawString(100,800,"Participant Details:")
        c.drawString(100,785,f"Name : {name}")
        c.drawString(100,770,f"Age : {age}")
        c.drawString(100,755,f"Phone : {phone}")
        c.drawString(100,740,f"Email : {recipient_list}")
        c.showPage()
        c.save()
        pdf = buffer.getvalue()
        buffer.close()
        
        email_message = f"Your name is {name} \n {message} \n Your age is {age} \n Your phone number is {phone}"

        mail = EmailMessage(name,email_message,email_from,[recipient_list])

        mail.attach('form_submition.pdf',pdf,'application/pdf')

        mail.attach(video.name,video.read(),video.content_type)
        mail.send()

    context = {
        'form':form
    }
    return render(request,'user_create.html',context)
