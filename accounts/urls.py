from django.urls import path
from .views import DashboardView, RegisterView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'), # Dashboard
    path('register/', RegisterView.as_view(), name='register'), # Register
]
