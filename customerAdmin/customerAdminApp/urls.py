from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('customer/<str:user_pk>/', views.customer, name="customer"),
    path('product/', views.product, name="product"),
    path('orderForm/', views.createOrder, name='create_order'),
    path('updateOrder/<str:user_id>/', views.updateOrder, name='update_order'),
    path('deleteOrder/<str:user_id>/', views.deleteOrder, name='delete_order'),
]
