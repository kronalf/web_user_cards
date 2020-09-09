from django.db import models


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Наименование отдела/цеха")

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"

    def __str__(self):
        return self.name


class Floor(models.Model):
    number = models.CharField(max_length=10, unique=True, verbose_name="Номер этажа")

    class Meta:
        verbose_name = "Этаж"
        verbose_name_plural = "Этажи"

    def __str__(self):
        return str(self.number)


class Person(models.Model):
    department = models.ForeignKey('Department', on_delete=models.CASCADE, verbose_name="ID Отдел")
    position = models.CharField(max_length=200, verbose_name="Должность")
    first_name = models.CharField(max_length=200, verbose_name="Имя")
    last_name = models.CharField(max_length=200, verbose_name="Фамилия")
    other_name = models.CharField(max_length=200, verbose_name="Отчество")
    full_name = models.CharField(max_length=603, verbose_name="Полное имя")
    login = models.CharField(max_length=200, verbose_name="Имя пользователя")
    password = models.CharField(max_length=16, verbose_name="Пароль")
    email = models.EmailField(verbose_name="Почтовый адрес")
    floor = models.ForeignKey('Floor', on_delete=models.CASCADE, verbose_name="ID Этажа размещения")
    number_room = models.CharField(max_length=10, verbose_name="Номер кабинета")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return str(self.full_name)
