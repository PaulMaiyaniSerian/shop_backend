from django.urls import path
from . import views

urlpatterns = [
    path('api/mpesa/pay', views.MpesaPaymentView.as_view(), name="mpesa_payment"),
    path('api/mpesa/pay/webhook', views.MpesaWebHook.as_view(), name="mpesa_webhook"),

]