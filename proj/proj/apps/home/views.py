from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomAuthenticationForm

# Create your views here.
def main(request):
    return render(request, 'home_index.html')







# Авторизация
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home:main')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'home_login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home:login')
