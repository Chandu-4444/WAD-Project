from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name = "index"),
    path('accounts/', include("django.contrib.auth.urls")),
    path('signup/', views.sign_up, name = 'signup'),
    path('profile/<int:id>', views.profile, name = 'profile'),
    path('assign_user/<int:id>/<int:proj_id>', views.assign_user, name = 'assign_user'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('otp_verification/', views.otp_verification, name="otp_verification"),
    path('blogs/', views.blog, name="blogs"),
    path('new_blog',views.new_blog, name="new_blog"),
    path('my_projects',views.my_projects, name='my_projects'),
    path('project_form',views.project_form, name='project_form'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)