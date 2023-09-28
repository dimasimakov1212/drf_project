from rest_framework import serializers

from vehicle.models import Car, Moto


class CarSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для модели Car
    """
    class Meta:
        model = Car
        fields = '__all__'


class MotoSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для модели Moto
    """
    class Meta:
        model = Moto
        fields = '__all__'
