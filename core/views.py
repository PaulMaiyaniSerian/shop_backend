from django.shortcuts import render, get_object_or_404, get_list_or_404

# Create your views here.
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


# serializer imports
from .serializers import (
    ProductSerializer,
    ProductCategorySerializer,
    ShoppingSessionSerializer,
    CartItemSerializer,
)

# model imports
from .models import (
    Product,
    ProductCategory,
    ShoppingSession,
    CartItem,
)

# product carousel and ProductCategoryIntro view

class CarouselProductsListView(generics.ListAPIView):
    '''
    Get all the products that are to be shown in a carousel
    '''
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_carousel=True)



class ProductCategoryIntroView(generics.GenericAPIView):
    '''
    Get some of  the products from a category default(16)
    todo set max of (16)
    '''

    serializer_class = ProductSerializer

    def get(self, request):
        category_name = request.query_params.get('category_name')
        print(category_name)
        category = get_object_or_404(ProductCategory, name=category_name)
        # query the filter_view
        products = Product.objects.filter(product_category=category)

        serializer = ProductSerializer(products,many=True, context={'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductCategoryListView(generics.ListAPIView):
    '''
    Get all the product categories
    '''

    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()


# Shopping session

class ShoppingSessionCreateView(generics.GenericAPIView):
    '''Creates A new Shopping session
    '''
    serializer_class = ShoppingSessionSerializer

    def post(self, request):
        data = request.data
        
        # check if payload has token
        user = request.user

        if not user.is_authenticated:
            user = None

        device_id = data.get('device_id')

        if not user:
            if device_id:
                # create shopping session with the device_id checking if it already exists
                try:
                    shopping_session = ShoppingSession.objects.get(device_id=device_id)
                except ShoppingSession.DoesNotExist:
                    shopping_session = None

                if shopping_session:
                    serializer = ShoppingSessionSerializer(shopping_session)
                    return Response(data=serializer.data, status=status.HTTP_200_OK)
                else:
                    # create the session
                    serializer = ShoppingSessionSerializer(data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
                    else:
                        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
            return Response(data={
                "error": "device_id, or logged in user required"
            }, status=status.HTTP_400_BAD_REQUEST)
                
        
        else:
            # update  shopping session with user
            try:
                shopping_session = ShoppingSession.objects.get(device_id=device_id)
            except ShoppingSession.DoesNotExist:
                shopping_session = None

            if shopping_session:
                shopping_session.user = user
                shopping_session.save()

                serializer = ShoppingSessionSerializer(shopping_session)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            
            else:
                # create new with user and device_id
                # check if it exists with that user 
                try:
                    shopping_session = ShoppingSession.objects.get(user=user)
                except ShoppingSession.DoesNotExist:
                    shopping_session = None

                if not shopping_session:
                    shopping_session = ShoppingSession.objects.create(user=user, device_id=device_id)
                    serializer = ShoppingSessionSerializer(shopping_session)
                    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(status=status.HTTP_200_OK)



            
            
# add to cart session
class AddToCartView(generics.GenericAPIView):
    serializer_class = CartItemSerializer

    def post(self, request):
        data = request.data

        product_id = data.get('product_id')

        device_id = data.get('device_id')

        qty = data.get("qty")

        user = request.user if request.user.is_authenticated else None

        product = Product.objects.get(id=product_id)

        # calculate Total
        total = product.price * int(qty)


        if user:
            # logged in users cart
            # query Shopping session of the user
            shopping_session = ShoppingSession.objects.get(user=user)
          

            # create cartItem
            cartItem = CartItem.objects.create(
                shopping_session=shopping_session,
                product = product_id,
                quantity = qty,
                total = total
            )

            serializer = CartItemSerializer(cartItem)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            # means not logged in so use device_id
            # query shopping session
            shopping_session = ShoppingSession.objects.get(device_id=device_id)

            # create cart item based on device_id
            cartItem = CartItem.objects.create(
                shopping_session=shopping_session,
                product = product_id,
                quantity = qty,
                total = total
            )

            serializer = CartItemSerializer(cartItem)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)



