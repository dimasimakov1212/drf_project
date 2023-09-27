from rest_framework import serializers

from vehicle.models import Car


class CarSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для модели Car
    """
    class Meta:
        model = Car
        fields = '__all__'
