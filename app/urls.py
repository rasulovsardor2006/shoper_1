from django.contrib import admin
from django.urls import path, include

from app.views import index, product_details, shop_view, shopping_cart, contact, checkout, create_product, \
    update_product, login_view, logout_view, register_view, ForgotPasswordView

urlpatterns = [
    path('', index, name='index'),
    path('product-details/<int:product_id>', product_details, name='shop-details'),
    path('shop/', shop_view, name='shop'),
    path('shopping-cart/', shopping_cart, name='shopping-cart'),
    path('contact/', contact, name='contact'),
    path('checkout/', checkout, name='checkout'),

    path('create-product/', create_product, name='create-product'),
    path('update-product/<int:product_id>', update_product, name='update-product'),

    #auth
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password')
]
