from django.urls import path,include
urlpatterns = [
    path('', include('product.urls')),
    path('user/', include('user.urls')),
    path('cart/', include('cart.urls')),
]