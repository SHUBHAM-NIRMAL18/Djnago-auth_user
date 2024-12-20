from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy


# Create your views here.
# View for Dashboard
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/dashboard.html'


# User Register View
class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm # Built-in Register form
    success_url = reverse_lazy('login') # Redirect to login page after register

