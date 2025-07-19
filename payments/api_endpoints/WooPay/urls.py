from django.urls import path

from payments.api_endpoints.WooPay.CreateTransaction.views import (
    WooPayCreateTransactionAPIView
)
from payments.api_endpoints.WooPay.PerformTransaction.views import WooPayPerformTransactionAPIView

urlpatterns = [
    path(
        "CreateTransaction/",
        WooPayCreateTransactionAPIView.as_view(),
        name="WooPayCreateTransaction",
    ),
    path(
        "PerformTransaction/",
        WooPayPerformTransactionAPIView.as_view(),
        name="WooPayPerformTransaction",
    ),
]