from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_form, name="login"),
    path('signup/', views.signup, name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('profile/', views.profile_display, name='profile_display'),
    path('otp_verification/', views.otp_verification, name="otp_verification"),
]