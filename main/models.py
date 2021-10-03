from django.db import models

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

