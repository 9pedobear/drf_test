
from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter
from car.views import *

router = SimpleRouter()
router.register(r'car', CarViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += router.urls

