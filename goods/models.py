#! coding: utf-8
from django.db import models

class Producers(models.Model):
    Name = models.CharField("Название", max_length=150)

    def __unicode__(self):
        return self.Name

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = 'Производители'


class Categories(models.Model):
    Name = models.CharField("Название", max_length=150)
    Parent = models.ForeignKey('self', verbose_name='Родитель', blank=True, null=True)

    def __unicode__(self):
        return self.Name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = 'Категории'

class Wares(models.Model):
    Code = models.CharField("Артикул", max_length=50)
    Name = models.CharField("Название", max_length=150)
    Producer = models.ForeignKey(Producers, verbose_name='Производитель')
    Image  = models.ImageField("Фото", upload_to="images", blank=True, null=True)
    Category = models.ForeignKey(Categories, verbose_name='Категория')
    Description = models.TextField("Описание", blank=True, null=True)

    def __unicode__(self):
        return self.Name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = 'Товары'

class Properties(models.Model):
    Name = models.CharField("Название", max_length=150)

    def __unicode__(self):
        return self.Name

    class Meta:
        verbose_name = "Свойство"
        verbose_name_plural = 'Свойства'

class PropertiesValues(models.Model):
    Property = models.ForeignKey(Properties, verbose_name='Свойство')
    Value = models.TextField()

    def __unicode__(self):
        return self.Value

    class Meta:
        verbose_name = "Значение свойства"
        verbose_name_plural = 'Значение свойств'

class PropertiesByCategories(models.Model):
    Name = models.CharField("Название", max_length=150)
    Category = models.ForeignKey(Categories, verbose_name='Категория')
    Property = models.ForeignKey(Properties, verbose_name='Свойство')

    def __unicode__(self):
        return self.Name

    class Meta:
        verbose_name = "Свойства по категориям товара"
        verbose_name_plural = 'Свойства по категориям товара'

class WaresProperties(models.Model):
    Ware = models.ForeignKey(Wares, verbose_name='Товар')
    Property = models.ForeignKey(Properties, verbose_name='Свойство')
    Value = models.ForeignKey(PropertiesValues, verbose_name='Значение свойства')

    def __unicode__(self):
        return self.Ware.Name

    class Meta:
        verbose_name = "Значение свойств товара"
        verbose_name_plural = 'Значения свойств товара'

class WaresImages(models.Model):
    Title = models.CharField("Заголовок", max_length=150)
    Ware = models.ForeignKey(Wares, verbose_name='Товар')
    Image = models.ImageField("Фото", upload_to="images", blank=True, null=True)

    def __unicode__(self):
        return self.Title

    class Meta:
        verbose_name = "Фотография товара"
        verbose_name_plural = 'Фотографии товара'

class Actions(models.Model):
    Title = models.CharField("Заголовок", max_length=150)
    Image = models.ImageField("Фото", upload_to="images")
    Description = models.TextField("Описание")

    def __unicode__(self):
        return self.Title

    class Meta:
        verbose_name = "Описание акции"
        verbose_name_plural = 'Акции'

class ActionWares(models.Model):
    Action = models.ForeignKey(Actions, verbose_name='Акция')
    Ware = models.ForeignKey(Wares, verbose_name='Товар')

    def __unicode__(self):
        return self.Action

    class Meta:
        verbose_name = "Акционный товар"
        verbose_name_plural = 'Акционные товары'