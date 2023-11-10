from django.db import models


class Statementes(models.Model):
    objects = None
    number = models.CharField('Номер машины', max_length=50)
    status = models.CharField('Статус заявления', max_length=50)
    comment = models.TextField('Нарушение')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Заявление'
        verbose_name_plural = 'Заявления'
