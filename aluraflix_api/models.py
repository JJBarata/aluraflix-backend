from django.db import models

# Create your models here.
class Video(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID'
    )
    titulo = models.CharField(
        max_length=150,
        blank=False,
        null=False
    )
    descricao = models.CharField(
        max_length=500,
        blank=False,
        null=False      
    )
    url = models.URLField(
        max_length=200,
        blank=False,
        null=False
    )
    
    def __str__(self):
        return self.titulo
    
