from django.urls import path
from .views import *

urlpatterns = [
    path('register/', User1RegistrationView.as_view(), name='user1_register'),
    path('verify/', User1VerificationView.as_view(), name='user1_verify'),
    path('login/', User1LoginView.as_view(), name='user1_login'),
    path('reset-password/', ResetPasswordAPIView.as_view(), name='reset_password'),

    path('categories/', CategoryAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryAPIView.as_view(), name='category-detail'),

    path('products/', ProductAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductAPIView.as_view(), name='product-detail'),

    path('posters/', PosterAPIView.as_view(), name='poster-list'),
    path('posters/<int:pk>/', PosterAPIView.as_view(), name='poster-detail'),

    #path('check-promocode/', CheckPromocodeView.as_view(), name='check-promocode'),

]


