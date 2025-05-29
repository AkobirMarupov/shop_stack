from django.urls import path

from accaunts.api_endpoints import (
    SeeionLoginAPIView,
    SessionLogoutAPIView,
    CartItemsListAPIView,
    CartItemsCreateAPIView,
    CartItemsUpdateAPIView,
    CartItemsDeleteAPIView
)

urlpatterns = [
    path('login/', SeeionLoginAPIView.as_view(), name="login-session"),
    path('logout/', SessionLogoutAPIView.as_view(), name="logout-session"),
    path('cart/', CartItemsListAPIView.as_view(), name="cart-items"),
    path('cart/cartitems/create/', CartItemsCreateAPIView.as_view(), name="cart-items-create"),
    path('cart/cartitems/<int:pk>/update/', CartItemsUpdateAPIView.as_view(), name="cart-items-update"),
    path('cart/cartitems/<int:pk>/delete/', CartItemsDeleteAPIView.as_view(), name="cart-items-delete"),
]