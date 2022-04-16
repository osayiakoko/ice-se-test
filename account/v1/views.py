from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import update_last_login

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenViewBase

from .serializers import (
    ChangePasswordSerializer, 
    LoginSerializer, 
    RefreshTokenSerializer, 
    UserSerializer
)

User = get_user_model()


class LoginView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.data.get("email")
            password = serializer.data.get("password")

            user = authenticate(username=email, password=password)

            if user and user.is_active:
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token

                user_serializer = UserSerializer(user)
                update_last_login(None, user)

                return Response({
                    'refresh_token': str(refresh),
                    'access_token': str(access_token),
                    'user': user_serializer.data
                })
            return Response({"detail": "Invalid login credentials"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(GenericAPIView):
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            password = serializer.data.get('current_password')
            user = authenticate(username=request.user.email, password=password)

            if user:
                serializer.update(user, serializer.data)

                refresh = RefreshToken.for_user(user)
                data = {
                    'access_token': str(refresh.access_token),
                    'refresh_token': str(refresh),
                }
                return Response(data, status=status.HTTP_200_OK)
            return Response({'details': 'Incorrect password'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RefreshTokenView(TokenViewBase):
    """
    Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.
    """
    permission_classes = [AllowAny]
    serializer_class = RefreshTokenSerializer
