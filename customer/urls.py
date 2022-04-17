from django.urls import include, path


app_name = 'customer'

urlpatterns = [
    path('v1/', include('customer.v1.urls')),
]
