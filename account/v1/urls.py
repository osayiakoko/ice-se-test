from django.urls import path

from account.v1 import views


app_name = 'v1'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
    path('refresh-token/', views.RefreshTokenView.as_view(), name='refresh-token'),
]
