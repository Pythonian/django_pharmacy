from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login/',
         auth_views.LoginView.as_view(
             redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/administrator/',
         views.AdministratorSignUpView.as_view(), name='administrator_signup'),
    path('signup/pharmacist/',
         views.PharmacistSignUpView.as_view(), name='pharmacist_signup'),
    path('administrator/', views.administrator_dashboard, name='administrator_dashboard'),
    path('', views.home, name='home'),
]
