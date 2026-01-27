from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('user_dashboard/', views.UserDashboardView.as_view(), name='user-dashboard'),
    path('seller_dashboard/', views.UserDashboardView.as_view(), name='seller-dashboard'),
    path('admin_dashboard/', views.UserDashboardView.as_view(), name='admin-dashboard'),
]