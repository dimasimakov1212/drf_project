from rest_framework import viewsets, generics

from vehicle.models import Car, Moto, Milage
from vehicle.serializers import CarSerializer, MotoSerializer, MilageSerializer, MotoMilageSerializer, \
    MotoCreateSerializer


class CarViewSet(viewsets.ModelViewSet):
    """
    ViewSet-класс для вывода списка авто и информации по одному объекту
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class MotoCreateAPIView(generics.CreateAPIView):
    """
    класс для создания мото на основе generics
    """
    # serializer_class = MotoSerializer
    serializer_class = MotoCreateSerializer  # используем переопределенный сериализатор


class MotoListAPIView(generics.ListAPIView):
    """
    класс для вывода списка мото на основе generics
    """
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoRetrieveAPIView(generics.RetrieveAPIView):
    """
    класс для вывода одного мото на основе generics
    """
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoUpdateAPIView(generics.UpdateAPIView):
    """
    класс для изменения одного мото на основе generics
    """
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()


class MotoDestroyAPIView(generics.DestroyAPIView):
    """
    класс для удаления одного мото на основе generics
    """
    queryset = Moto.objects.all()


class MilageCreateAPIView(generics.CreateAPIView):
    """
    класс для создания пробега на основе generics
    """
    serializer_class = MilageSerializer


class MotoMilageListAPIView(generics.ListAPIView):
    """
    класс для вывода списка мото на основе generics
    """
    serializer_class = MotoMilageSerializer
    queryset = Milage.objects.filter(moto__isnull=False)
