from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views import View

# Create your views here.
class LoginView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            redirect('/')
        else:
            form = AuthenticationForm()
            context = {'form': form}
            return render(request, 'accounts/login.html', context)
    
    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        return render(request, 'accounts/login.html', {'form': form})

class RegisterView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            redirect('/')
        else:
            form = UserCreationForm()
            context = {'form': form}
            return render(request, 'accounts/register.html', context)
    
    def post(self, request, *args, **kwargs):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            print('Hello world!!')
            return redirect('/accounts/login')
        return render(request, 'accounts/register.html', {'form': form})

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return redirect('/accounts/login')
