from django.urls import path
from . import views

urlpatterns = [
    path('', views.mail, name='mail'),
]


