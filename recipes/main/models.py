from django.db import models


# Create your models here.

class Recipes(models.Model):

    title = models.CharField('Название блюда', max_length=100)
    description = models.CharField('Краткое описание', max_length=250)
    ingredients = models.TextField('Ингредиенты')
    instructions = models.TextField('Рецепт')
    cook_time = models.IntegerField('Время приготовления')
    tags = models.CharField('Тэги', max_length=50)
    photo = models.ImageField(upload_to='static/main/img/meals/', default=None, blank=True, verbose_name='Фото')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/recipe/{self.id}"

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
