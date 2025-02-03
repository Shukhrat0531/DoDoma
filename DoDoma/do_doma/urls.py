from django.urls import path
from .views import *
<<<<<<< HEAD

=======
>>>>>>> 274b6c11b1d54012fd32391c7427f00c53afc678

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

    path('carts/', CartAPIView.as_view(), name='cart-list'),
    path('carts/<int:pk>/', CartAPIView.as_view(), name='cart-detail'),

    #path('check-promocode/', CheckPromocodeView.as_view(), name='check-promocode'),

]


