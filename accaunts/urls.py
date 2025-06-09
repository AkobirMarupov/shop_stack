from django.urls import path

from accaunts.api_endpoints import (
    SeeionLoginAPIView, SessionLogoutAPIView,
    CartItemsListAPIView, CartItemsCreateAPIView, 
    CartItemsUpdateAPIView, CartItemsDeleteAPIView,
    PasswordResetAPIView, PasswordResetConfirmAPIView,
    ProfileDeleteAPIView, ProfileUpdateAPIView,
    RegisterUserAPIView, RegisterConfirmAPIView
)

urlpatterns = [
    path('login/', SeeionLoginAPIView.as_view(), name="login-session"),
    path('logout/', SessionLogoutAPIView.as_view(), name="logout-session"),
    path('cart/', CartItemsListAPIView.as_view(), name="cart-items"),
    path('cart/cartitems/create/', CartItemsCreateAPIView.as_view(), name="cart-items-create"),
    path('cart/cartitems/<int:pk>/update/', CartItemsUpdateAPIView.as_view(), name="cart-items-update"),
    path('cart/cartitems/<int:pk>/delete/', CartItemsDeleteAPIView.as_view(), name="cart-items-delete"),

    path('prifile/<int:pk>/update/', ProfileUpdateAPIView.as_view(), name="profile-update"),
    path('prifile/<int:pk>/delete/', ProfileDeleteAPIView.as_view(), name="profile-delete"),

    path('password-reset/request/', PasswordResetAPIView.as_view(), name='password-reset'),
    path('password-reset/confirm/', PasswordResetConfirmAPIView.as_view(), name='passwor-reset-confirm'),

    path('register/user/', RegisterUserAPIView.as_view(), name='register-user'),
    path('register/confirm', RegisterConfirmAPIView.as_view(), name='register-confirm')
    
]