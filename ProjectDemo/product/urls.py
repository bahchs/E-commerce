from django.urls import path
from .views import GetCategoryAPI,GetProductAPI,index,viewShop,viewItem
urlpatterns = [
    path('', index, name='index'),
    path('shop/', viewShop, name='shop'),
    path('item/<int:id>/',viewItem, name='item_view'),
    path('category/', GetCategoryAPI.as_view(), name='get_category'),
    path('category/<int:id>/', GetCategoryAPI.as_view(), name='up_dl_category'),
    path('items/', GetProductAPI.as_view(), name='get_items'),
    path('items/<int:id>/', GetProductAPI.as_view(), name='up_dl_items')
]