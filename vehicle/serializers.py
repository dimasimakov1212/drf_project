from rest_framework import serializers

from vehicle.models import Car, Moto, Milage


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


class MilageSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для модели Milage
    """
    class Meta:
        model = Milage
        fields = '__all__'
