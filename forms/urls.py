from django.urls import path 
from .views import custom_create_view

urlpatterns=[
    path('',custom_create_view,name='createview')
]
