from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from services.users_client import UserService

# Create your views here.
class RegisterView(TemplateView):
    template_name = 'users/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template'] = self.template_name
        return context

    def post(self, request, *args, **kwargs):
        response = UserService.register_user(request.POST)
        if response:
            return HttpResponse("Signup succesful")
            # return redirect('login')
        return render(request, self.template_name)
    

class LoginView(TemplateView):
    template_name = "users/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.template_name
        return context
    
    def post(self, request, *args, **kwargs):
        response = UserService.login_user(request.POST)
        if response.status_code==200:
            data = response.json()
            print(data)
            request.session['auth_token'] = data['token']
            request.session['role'] = data['role']

            if data['role']=='customer':
                return redirect('user-dashboard')
            elif data['role']=='seller':
                return redirect('seller-dashboard')
            elif data['role']=='admin':
                return redirect('admin-dashboard')
            
        return render(request, self.template_name)
    

class UserDashboardView(TemplateView):
    template_name = 'users/dashboard.html'


class SellerDashboardView(TemplateView):
    template_name = 'sellers/dashboard.html'


class AdminDashboard(TemplateView):
    template_name = 'admin/dashboard.html'