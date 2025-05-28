from django.urls import path
from accaunts.api_endpoints.logautsession.views import SessionLogoutAPIView
from accaunts.api_endpoints.loginsession.views import SeeionLoginAPIView

from accaunts.api_endpoints.CartItem.CartItemList.views import *


urlpatterns = [
    path('login/', SeeionLoginAPIView.as_view(), name="login-session"),
    path('logout/', SessionLogoutAPIView.as_view(), name="logout-session"),
    
    path('cart/', CartItemsListAPIView.as_view(), name='cart-list'),

]