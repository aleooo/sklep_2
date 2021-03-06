from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from . import views

app_name = 'shop'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('shop:password_change_done')), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('shop:password_reset_done')), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('shop:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('register/', views.Register.as_view(), name='register'),
    path('account/', views.account, name='account'),
    path('account/<str:type>/', views.account, name='account_data'),
    path('detail/<str:slug>/<int:seconds>/<int:hours>/<int:id>/', views.Detail.as_view(), name='detail'),
    path('list/category/<str:category>/', views.List.as_view(), name='list_category'),
    path('list/search/<str:search>/', views.List.as_view(), name='list_search'),
    path('list/', views.List.as_view(), name='list'),
    path('search/', views.search, name='search'),
    path('', views.Main.as_view(), name='main'),
]
