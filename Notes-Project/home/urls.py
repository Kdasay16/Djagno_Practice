from django.urls import path

from . import views

# we made this file so that we can more dynamically add these routes to smartnotes/url.py
urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('login', views.LoginInterfaceView.as_view(), name="login"),
    path('logout', views.LogoutInterfaceView.as_view(), name="logout"),
    path('signup', views.SignupView.as_view(), name="signup"),
]