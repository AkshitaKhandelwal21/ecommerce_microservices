from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('user_dashboard/', views.UserDashboardView.as_view(), name='user-dashboard'),
    path('seller_dashboard/', views.SellerDashboardView.as_view(), name='seller-dashboard'),
    path('admin_dashboard/', views.AdminDashboard.as_view(), name='admin-dashboard'),
    path('choose_account/', views.SellerOrUserAccountView.as_view(), name='choose-account'),
]