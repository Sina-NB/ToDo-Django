from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views import View
from .forms import CustomAuthenticationForm


# Create your views here.
class LoginView(View):
    """
    Login class based view. this view accepts 'get' and 'post' methods.
    """

    def get(self, request, *args, **kwargs):
        """
        The 'get' method is implemented in this function.
        """
        if request.user.is_authenticated:
            return redirect("/")
        else:
            form = AuthenticationForm()
            context = {"form": form}
            return render(request, "accounts/login.html", context)

    def post(self, request, *args, **kwargs):
        """
        The 'post' method is implemented in this function.
        """
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            remember_me = form.cleaned_data.get("remember_me")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if remember_me:
                    request.session.set_expiry(1209600)
                else:
                    request.session.set_expiry(0)
                login(request, user)
                return redirect("/")
        return render(request, "accounts/login.html", {"form": form})


class RegisterView(View):
    """
    Register class based view. this view accepts 'get' and 'post' methods.
    """

    def get(self, request, *args, **kwargs):
        """
        The 'get' method is implemented in this function.
        """
        if request.user.is_authenticated:
            return redirect("/")
        else:
            form = UserCreationForm()
            context = {"form": form}
            return render(request, "accounts/register.html", context)

    def post(self, request, *args, **kwargs):
        """
        The 'post' method is implemented in this function.
        """
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login")
        return render(request, "accounts/register.html", {"form": form})


class LogoutView(View):
    """
    Logout class based view. this view accepts only 'get' method.
    """

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        """
        The 'get' method is implemented in this function.
        """
        logout(request)
        return redirect("/accounts/login")
