from django.db import models


class Car(models.Model):
    """
    Класс для создания авто
    """
    car_title = models.CharField(max_length=150, verbose_name='название')
    car_description = models.TextField(verbose_name='описание')

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

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.moto_title}'

    class Meta:
        verbose_name = 'Мотоцикл'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Мотоциклы'  # Настройка для наименования набора объектов
        ordering = ('moto_title',)  # сортировка по наименованию
