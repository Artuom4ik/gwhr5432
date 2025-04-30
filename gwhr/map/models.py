from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    coordinates = models.JSONField(verbose_name='Координаты')
    additional_data = models.JSONField(default=dict, verbose_name='Дополнительные данные')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')

    def __str__(self):
        return self.name
