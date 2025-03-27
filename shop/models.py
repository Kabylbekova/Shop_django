from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)  # Название товара
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    description = models.TextField(blank=True)  # Описание
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # Картинка
    created_at = models.DateTimeField(auto_now_add=True)  # Дата добавления

    def __str__(self):
        return self.name

