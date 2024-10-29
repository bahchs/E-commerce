from django.urls import path
from .views import CustomerAPI,LoginAPI,logout_view
urlpatterns = [
    path('', CustomerAPI.as_view()),
    path('login/', LoginAPI.as_view(), name='login_user'),
    path('logout/', logout_view, name='logout_user'),
]