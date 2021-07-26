from django.db import models

class Categoria(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='categoriaID'
    )
    titulo = models.CharField(
        max_length=150,
        blank=False,
        null=False
    )
