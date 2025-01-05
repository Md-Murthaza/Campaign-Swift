from django.shortcuts import render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializer , UserProfileSerializer , UserNotificationSerializer
from .models import UserNotification
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
# Create your views here.


#=== User Register API ==#

@api_view(['POST'])
def user_register(request):
    if request.method == "POST":
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User registered sucessfully!"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



#== User Login API ==#

@api_view(['POST'])

def user_login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')


        if not email or not password:
            return Response({"message":" Email and Password  are required! "},status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request,email=email,password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access_token':str(refresh.access_token),
                'refresh_token':str(refresh)},status=status.HTTP_200_OK)

        return Response({"error": "Invalid email or password " },status=status.HTTP_401_UNAUTHORIZED)


#== User Profile API ==#

@api_view(['GET'])
@permission_classes([IsAuthenticated])

def get_user_profile(request):
    user_profile = request.user.userprofile
    serializer = UserProfileSerializer(user_profile)
    return Response(serializer.data,status=status.HTTP_200_OK)

#== Update userprofile api ==#

@api_view(['PUT'])
@permission_classes([IsAuthenticated])

def update_user_profile(request):
    user_profile = request.user.userprofile
    serializer = UserProfileSerializer(user_profile,data=request.data,partial=True)

    if serilaizer.is_valid():
        serilaizer.save()
        return Response(serilaizer.data , status=status.HTTP_200_OK)
    
    return Response(serilaizer.errors ,status=status.HTTP_400_BAD_REQUEST)


