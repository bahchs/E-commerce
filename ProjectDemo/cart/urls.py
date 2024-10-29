from django.urls import path
from .views import Index,AddToCartView
urlpatterns = [
    path('',Index ,name='cart'),
    path('add-to-cart/<int:variation_id>/', AddToCartView.as_view(), name="add_to_cart"),

]