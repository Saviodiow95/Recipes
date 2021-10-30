from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Chef(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Chef'
        verbose_name_plural = 'Chefes'


class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ('1', 'Fácil'),
        ('2', 'Médio'),
        ('3', 'Difícil')
    ]

    name = models.CharField(max_length=50, verbose_name='Nome')
    chef = models.ForeignKey(Chef, verbose_name="Chef", on_delete=models.PROTECT)
    description = models.TextField(verbose_name='Descrição', null=True, blank=True)
    ingredients = models.TextField(verbose_name='Ingredientes')
    time = models.IntegerField(verbose_name='Tempo de preparo (em minutos)')
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY_CHOICES, verbose_name='Dificuldade de preparo')
    method = models.TextField(verbose_name='Método de preparo')
    portions = models.IntegerField(verbose_name='Numero de Porções que a Receita rende', default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'
