from rest_framework import viewsets

from vehicle.models import Car
from vehicle.serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    """
    ViewSet-класс для вывода списка авто и информации по одному объекту
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer

