from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name = "index"),
    path('accounts/', include("django.contrib.auth.urls")),
    path('signup/', views.sign_up, name = 'signup'),
    path('profile/', views.profile, name = 'profile'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('otp_verification/', views.otp_verification, name="otp_verification"),
    path('blogs/', views.blog, name="blogs")

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)