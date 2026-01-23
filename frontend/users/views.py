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