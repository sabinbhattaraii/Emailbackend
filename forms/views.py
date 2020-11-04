from django.shortcuts import render
from .forms import CustomUserForm
from .models import CustomUser

# Create your views here.

def custom_create_view(request):
    form = CustomUserForm(request.POST,request.FILES )
    if form.is_valid():
        form.save()
        
    context = {
        'form':form
    }
    return render(request,'user_create.html',context)