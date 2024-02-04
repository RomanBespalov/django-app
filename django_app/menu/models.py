from django.db import models


class MenuItem(models.Model):
    """Модель для хранения данных о меню."""
    name = models.CharField(
        max_length=50,
        verbose_name='Название',
    )
    url = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Ссылка',
    )
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ['id']

    def __str__(self):
        return self.name
