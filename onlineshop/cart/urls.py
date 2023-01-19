from django.urls import path

from cart import views

urlpatterns=[
    path('', views.cart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('deduct_cart/<int:product_id>/<int:cart_item_id>/', views.deduct_cart, name='deduct_cart'),
    path('delete_cart/<int:product_id>/<int:cart_item_id>/', views.delete_cart, name='delete_cart'),
]