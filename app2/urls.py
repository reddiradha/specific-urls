from app2.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('first/',first,name='first'),
    path('second/',second,name='second'),
]