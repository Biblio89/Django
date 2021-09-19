from django.db import models

class Task(models.Model):
    title = models.CharField('Название', max_length= 100)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class Task2(models.Model):
    title = models.CharField('Название2', max_length= 100)
    task = models.TextField('Описание2')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача2'
        verbose_name_plural = 'Задачи2'