from django.shortcuts import redirect
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'


class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}

# This has been replaced with the HomeView class to make this a "class based view"
# def home(request):
#     # today is passed into the html file to be used there
#     return render(request, 'home/welcome.html', {'today': datetime.today()})


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/login'

# This has been replaced with the AuthorizedView class to make this a "class based view"
# login_required tells django the user must be logged in to view the page
# the parameter passed will redirect the user to the login screen
# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})
