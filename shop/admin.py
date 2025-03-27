from django.contrib import admin
from .models import Product

admin.site.register(Product)  # Регистрируем модель в админке

