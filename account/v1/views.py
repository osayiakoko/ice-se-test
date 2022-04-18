from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import update_last_login
from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenViewBase
from drf_yasg.utils import swagger_auto_schema

from .serializers import (
    ChangePasswordSerializer,
    LoginSerializer, 
    RefreshTokenSerializer,
    TokenSerializer, 
    UserSerializer,
    UserTokenSerializer
)

User = get_user_model()


class LoginView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    @swagger_auto_schema(responses={200: UserTokenSerializer})
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.data.get("email")
            password = serializer.data.get("password")

            user = authenticate(username=email, password=password)

            if user and user.is_active:
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token

                update_last_login(None, user)

                user_token_ser = UserTokenSerializer({
                    'refresh_token': str(refresh),
                    'access_token': str(access_token),
                    'user': UserSerializer(user).data
                })

                return Response(user_token_ser.data)
            return Response({"detail": "Invalid login credentials"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(GenericAPIView):
    serializer_class = ChangePasswordSerializer

    @swagger_auto_schema(responses={200: TokenSerializer})
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            password = serializer.data.get('current_password')
            user = authenticate(username=request.user.email, password=password)

            if user:
                data = serializer.update(user, serializer.data)
                return Response(data, status=status.HTTP_200_OK)

            return Response({'details': 'Incorrect password'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(name='post', decorator=swagger_auto_schema(
    responses={200: TokenSerializer}
))
class RefreshTokenView(TokenViewBase):
    """
    Takes a refresh type JSON web token and returns an access type JSON web
    token if the refresh token is valid.
    """
    permission_classes = [AllowAny]
    serializer_class = RefreshTokenSerializer
