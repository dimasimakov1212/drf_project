from django.conf import settings
from django.db import models


class Car(models.Model):
    """
    Класс для создания авто
    """
    car_title = models.CharField(max_length=150, verbose_name='название')
    car_description = models.TextField(verbose_name='описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='владелец',
                              blank=True, null=True)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.car_title}'

    class Meta:
        verbose_name = 'Автомобиль'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Автомобили'  # Настройка для наименования набора объектов
        ordering = ('car_title',)  # сортировка по наименованию


class Moto(models.Model):
    """
    Класс для создания мотоцикла
    """
    moto_title = models.CharField(max_length=150, verbose_name='название')
    moto_description = models.TextField(verbose_name='описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='владелец',
                              blank=True, null=True)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.moto_title}'

    class Meta:
        verbose_name = 'Мотоцикл'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Мотоциклы'  # Настройка для наименования набора объектов
        ordering = ('moto_title',)  # сортировка по наименованию


class Milage(models.Model):
    """
    Класс для создания пробега
    """
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True, verbose_name='авто',
                            related_name='milage')
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, null=True, blank=True, verbose_name='мото',
                             related_name='milage')

    milage = models.PositiveIntegerField(verbose_name='пробег')
    year = models.PositiveSmallIntegerField(verbose_name='год регистрации')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.car if self.car else self.moto} - {self.year}'

    class Meta:
        verbose_name = 'пробег'  # Настройка для наименования одного объекта
        verbose_name_plural = 'пробег'  # Настройка для наименования набора объектов
        ordering = ('-year',)  # сортировка
