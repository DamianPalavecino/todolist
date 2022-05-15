from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class HomeView(TemplateView):
    template_name ='home.html'
    
class RegistroView(View):   

    def get(self, request):
        form = UserCreationForm
        return render(request, 'registro.html', {'form':form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('home')