from django.urls import path
from . import views


urlpatterns = [
    path('carousel_products', views.CarouselProductsListView.as_view(), name='carousel_products_list'),
    path('product_category_intro_view', views.ProductCategoryIntroView.as_view(), name='products_intro'),
    path('product_categories',views.ProductCategoryListView.as_view(), name="product_category" ),


    # cart and shopping_session
    path('shopping_session/create',views.ShoppingSessionCreateView.as_view(), name="shopping_session_create" ),
    path('shopping_session/cart_item/add',views.AddToCartView.as_view(), name="add_to_cart" ),


]