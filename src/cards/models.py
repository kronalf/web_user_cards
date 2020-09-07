from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=200, verbose_name="Имя")
    last_name = models.CharField(max_length=200, verbose_name="Фамилия")
    other_name = models.CharField(max_length=200, verbose_name="Отчество")

    class Meta:
        verbose_name="Пользователь"
        verbose_name_plural = "Пользователи"

class Department(models.Model):
    name = models.CharField(max_length=200,verbose_name="Наименование отдела/цеха")

    class Meta:
        verbose_name="Отдел"
        verbose_name_plural = "Отделы"

class Floor(models.Model):
    number = models.IntegerField(verbose_name="Номер этажа")

    class Meta:
        verbose_name="Этаж"
        verbose_name_plural = "Этажи"