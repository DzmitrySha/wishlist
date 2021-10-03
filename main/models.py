from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    """ Таблица "Товар" в базе данных

    id записи
    Название товара
    Ссылка на товар
    Цена товара
    Дата и время создания записи о товаре

    """
    title = models.CharField(max_length=120)
    link = models.URLField()
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_created=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class WishList(models.Model):
    """ Таблица "Список подарков"

    id - создаст Django автоматически
    owner - Char
    products - ManytoMany
    is_hidden - bool
    """
    title = models.CharField(max_length=120)
    product = models.ManyToManyField(Product)
    is_hidden = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class About(models.Model):
    """ Таблица "О проекте" в базе данных

    id записи
    Название проекта
    О проекте
    Адрес проекта
    Дата и время создания проекта

    """
    title = models.CharField(max_length=120)
    about = models.TextField()
    address = models.CharField(max_length=150)
    create_at = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.title
