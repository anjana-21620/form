from.views import *
from django.urls import path

urlpatterns = [

 path('contact/', contact_view, name='contact'),
 path('contact-list/',contact_list,name='contact_list'),
  
]