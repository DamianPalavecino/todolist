from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

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
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, 'registro.html', {'form':form})
                    
def cerrar_sesion(request):
    logout(request)
    return redirect('home')


def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            passw = form.cleaned_data.get('password')
            usuario = authenticate(username=nombre_usuario, password=passw)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                messages.error(request, 'El usuario no es válido!')    
        else:
            messages.error(request, 'El usuario no es válido!')    
    form=AuthenticationForm
    return render(request, 'login.html', {'form':form})
