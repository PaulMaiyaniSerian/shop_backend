from django.shortcuts import render
from rest_framework import generics
from core.serializers import ProductSerializer

from . import mpesa

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.
class MpesaPaymentView(generics.GenericAPIView):
    '''
    Get some of  the products from a category default(16)
    todo set max of (16)
    '''

    serializer_class = ProductSerializer

    def post(self, request):
        data = request.data
        phone = data.get("phone")
        amount = data.get("amount")

        print(phone, amount)
        mpesa.stk_push(phone, amount)
        return Response( status=status.HTTP_200_OK)


class MpesaWebHook(generics.GenericAPIView):
    serializer_class = ProductSerializer

    def post(self, request):
        print(request.data)

        return Response( status=status.HTTP_200_OK)

