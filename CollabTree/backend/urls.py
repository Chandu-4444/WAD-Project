from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name = "index"),
    path('accounts/', include("django.contrib.auth.urls")),
    path('signup/', views.sign_up, name = 'signup'),
    path('profile/', views.profile, name = 'profile'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('otp_verification/', views.otp_verification, name="otp_verification"),

]