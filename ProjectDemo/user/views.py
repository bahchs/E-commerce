from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomerUser
from .serializers import CustomerSerializer,LoginSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from django.contrib.auth import logout

# Create your views here.


class CustomerAPI(APIView):
    def get(self,request):
        queryset = CustomerUser.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response({
            "status": True,
            "data": serializer.data
        })
    
    def post(self,request):
        data=request.data
        serializer=CustomerSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                "status": False,
                "data": serializer.errors
            })
        validated_data= serializer.validated_data
        user = CustomerUser(**validated_data)
        password = validated_data.get('password')
        if password:
            user.set_password(password)
        user.save()
        created_user=CustomerSerializer(user)
        return Response(data=created_user.data, status=status.HTTP_200_OK)
        

    

class LoginAPI(APIView):
    def get(self, request):
        return render(request, 'homeshop/login.html')
    
    def post(self, request):
        data=request.data
        serializer = LoginSerializer(data=data)
        if not serializer.is_valid():
            return Response({
            "status": False,
            "data": serializer.errors
        })
        username=serializer.data['username']
        password=serializer.data['password']
        user_obj=authenticate(username=username, password=password)
        if user_obj:
            token, _ =Token.objects.get_or_create(user=user_obj)
            login(request, user_obj)
            return redirect('index')
        
        return render(request, 'homeshop/login.html', {
            "error": "Invalid username or password"
        })
    

def logout_view(request):
    logout(request)
    return redirect('login_user')