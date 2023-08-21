from django.contrib.auth import views as authentication_views
from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', authentication_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/add', views.profile_add, name='profile_add'),
    path('profile/seller/<int:id>', views.profile_seller, name='profile_seller'),
]
