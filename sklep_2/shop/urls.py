from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'shop'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('search/', views.search, name='search'),
    path('detail/<str:slug>/<int:seconds>/<int:hours>', views.detail, name='detail'),
    path('', views.main, name='main'),
]
