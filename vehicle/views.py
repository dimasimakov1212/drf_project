from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from vehicle.models import Car, Moto, Milage
from vehicle.permissions import IsOwnerOrStaff
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
    permission_classes = [IsAuthenticated]  # создание мото доступно только авторизованным пользователям

    def perform_create(self, serializer):
        """
        Определяем порядок создания нового объекта
        """
        new_moto = serializer.save()
        new_moto.owner = self.request.user  # задаем владельца мото
        new_moto.save()


class MotoListAPIView(generics.ListAPIView):
    """
    класс для вывода списка мото на основе generics
    """
    serializer_class = MotoSerializer
    queryset = Moto.objects.all()
    permission_classes = [IsAuthenticated]  # просмотр списка мото доступно только авторизованным пользователям


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

    permission_classes = [IsOwnerOrStaff]  # просмотр списка мото доступно только владельцам или менеджеру


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


class MilageListAPIView(generics.ListAPIView):
    """
    класс для списка пробегов
    """
    serializer_class = MilageSerializer
    queryset = Milage.objects.all()

    filter_backends = [DjangoFilterBackend, OrderingFilter]  # Бэкенд для обработки фильтра
    filterset_fields = ('car', 'moto')  # Набор полей для фильтрации
    ordering_fields = ['year']


class MotoMilageListAPIView(generics.ListAPIView):
    """
    класс для вывода списка пробегов мото на основе generics
    """
    serializer_class = MotoMilageSerializer
    queryset = Milage.objects.filter(moto__isnull=False)
