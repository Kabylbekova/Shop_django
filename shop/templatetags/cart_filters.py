from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Фильтр для умножения двух чисел."""
    try:
        return float(value) * int(arg)  # Преобразуем количество в int, а цену в float
    except (ValueError, TypeError):
        return 0

@register.filter
def get(dictionary, key):
    """Фильтр для безопасного получения значения из словаря."""
    if isinstance(dictionary, dict):
        return dictionary.get(str(key), 0)  # Возвращает 0, если ключа нет
    return 0
