from django.urls import path, include
from .views import RegistroView, HomeView
urlpatterns = [   
    path('',HomeView.as_view(), name='home'),
    path('registro', RegistroView.as_view(), name='registro'),
]