from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomAuthenticationForm
from .models import UserStatistics
from django.contrib.auth.decorators import login_required

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




#Личный кабинет
@login_required
def user_dashboard(request):
    if request.user.is_authenticated:
        try:
            user_statistics = UserStatistics.objects.get(user=request.user)
        except UserStatistics.DoesNotExist:
            user_statistics = None
    else:
        user_statistics = None

    context = {
        'user': request.user,
        'user_statistics': user_statistics,
    }
    return render(request, 'home_user_dashboard.html', context)