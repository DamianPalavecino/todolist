from django.urls import path, include
from .views import RegistroView, HomeView, cerrar_sesion, loginView
urlpatterns = [   
    path('',HomeView.as_view(), name='home'),
    path('registro', RegistroView.as_view(), name='registro'),
    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion'),
    path('login', loginView, name='login'),

]