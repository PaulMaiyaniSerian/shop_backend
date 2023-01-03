from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


from .serializers import RegisterSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# open api
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

import time
# Create your views here.
class UserRegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    
    def post(self, request):
        # time.sleep(5)
        data = request.data

        serializer = RegisterSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['is_superuser'] = user.is_superuser
        token['is_seller'] = user.is_superuser
        token['is_staff'] = user.is_superuser
        token['email'] = user.email


        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer