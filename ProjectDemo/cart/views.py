from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Cart,CartItem
from product.models import Variation
from .serializers import CartItemSerializer
from user.models import CustomerUser

# Create your views here.
def Index(request):
    return render(request, 'homeshop/cart.html')

class AddToCartView(View):
    def post(self, request, variation_id):
        if request.user.is_anonymous:
            return redirect('login_user')
        quantity=1
        cart, created= Cart.objects.get_or_create(user=request.user)
        
        variation = get_object_or_404(Variation, id=variation_id)

        cart_item, item_created = CartItem.objects.get_or_create(
            cart=cart,
            item=variation,
            defaults={'quantity': quantity}
        )

        if not item_created:
            cart_item.quantity += quantity
            cart_item.save()
        
        return redirect('index')