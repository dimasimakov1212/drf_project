from rest_framework import serializers

from vehicle.models import Car, Moto, Milage
from vehicle.services import convert_currencies
from vehicle.validators import TitleValidator


class MilageSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для модели Milage
    """
    class Meta:
        model = Milage
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для модели Car
    """
    # определяем дополнительное поле в модели Car
    last_milage = serializers.IntegerField(source='milage.all.first.milage', read_only=True)  # данные о пробеге
    # milage = MilageSerializer(source='milage_set', many=True)
    # параметр source теперь не нужен, т.к. в модели определили related_name='milage'
    milage = MilageSerializer(many=True, read_only=True)

    usd_price = serializers.SerializerMethodField()  # определяем поле вывода стоимости авто в долларах

    class Meta:
        model = Car
        fields = '__all__'

    def get_usd_price(self, instance):
        return convert_currencies(instance.amount)


class MotoSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для модели Moto
    """
    # определяем дополнительное поле в модели Moto
    last_milage = serializers.SerializerMethodField()  # данные о пробеге

    class Meta:
        model = Moto
        fields = '__all__'

    def get_last_milage(self, instance):
        """
        Метод определения поля last_milage
        :param instance:
        :return:
        """
        # if instance.milage_set.all().first():
        # объект milage_set теперь не нужен, т.к. в модели определили related_name='milage'
        if instance.milage.all().first():
            # return instance.milage_set.all().first().milage
            return instance.milage.all().first().milage
        else:
            return 0


class MotoMilageSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для пробега мотоцикла
    """
    moto = MotoSerializer()

    class Meta:
        model = Milage
        fields = ('milage', 'year', 'moto',)


class MotoCreateSerializer(serializers.ModelSerializer):
    """
    Класс сериализатора для создания мотоцикла
    """
    # milage = MilageSerializer(many=True)

    class Meta:
        model = Moto
        fields = '__all__'

        validators = [
            TitleValidator(field='moto_title'),
            serializers.UniqueTogetherValidator(fields=['moto_title'], queryset=Moto.objects.all())
        ]

    # def create(self, validated_data):
    #     """
    #     Переопределяем метод create
    #     :param validated_data:
    #     :return:
    #     """
    #     milage = validated_data.pop('milage')   # включаем поле 'milage'
    #
    #     moto_item = Moto.objects.create(**validated_data)
    #
    #     for m in milage:
    #         Milage.objects.create(**m, moto=moto_item)
    #
    #     return moto_item
