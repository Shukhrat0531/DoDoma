from django.urls import path
from .views import User1RegistrationView, User1VerificationView,User1LoginView

urlpatterns = [
    path('register/', User1RegistrationView.as_view(), name='user1_register'),
    path('verify/', User1VerificationView.as_view(), name='user1_verify'),
    path('login/', User1LoginView.as_view(), name='user1_login'),
]
