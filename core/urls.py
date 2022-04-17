
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .views import root_redirect


app_name = "doc"

schema_view = get_schema_view(
    openapi.Info(
        title="ICE customers's transactions Dasboard API",
        default_version='v1',
        description="""
            This is a SE test project for [ICE commercial power](https://icecommpower.com/) written with Django Rest Framework.
            The `swagger-ui` view can be found [here](/swagger).
            The `ReDoc` view can be found [here](/redoc).
            You can log in using the pre-existing `admin@gmail.com` user with password `Pa$$0000`.
        """,
        terms_of_service="https://icecommpower.com/",
        contact=openapi.Contact(email="osayiakoko@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', root_redirect),
]
