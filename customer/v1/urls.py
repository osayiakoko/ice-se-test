from rest_framework import routers

from . import views


app_name = 'v1'

router = routers.SimpleRouter()
router.register(r'customers', views.CustomerViewSet)
router.register(r'payments', views.CustomerPaymentViewSet)

urlpatterns = router.urls
