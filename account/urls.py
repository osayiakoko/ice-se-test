from django.urls import path
from django.urls.conf import include

app_name = 'account'

urlpatterns = [
    path('v1/account/', include('account.v1.urls')),
]
