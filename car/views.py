from rest_framework import viewsets
from .serializers import *
from .models import *

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
