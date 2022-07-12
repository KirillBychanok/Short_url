from django.contrib.auth.models import User
from django.db import models


class CollectUrl(models.Model):
    '''Модель для хранения URL и ее короткой версии'''
    url = models.CharField(max_length=255, verbose_name='URL')
    short_url = models.CharField(max_length=255, verbose_name='Short_url', default='Пусто', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = 'URLs'
        ordering = ['-created_at']