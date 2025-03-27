from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def clear_cart(request):
    """ Очищает корзину """
    request.session['cart'] = {}
    request.session.modified = True
    return redirect('view_cart')

def product_list(request):
    """ Отображает список всех товаров """
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def add_to_cart(request, product_id):
    """ Добавляет товар в корзину или увеличивает его количество """
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    cart[str(product.id)] = cart.get(str(product.id), 0) + 1
    request.session['cart'] = cart
    request.session.modified = True

    return redirect('view_cart')

def view_cart(request):
    """ Отображает содержимое корзины """
    cart = request.session.get('cart', {})
    
    # Получаем товары по их ID
    product_ids = [int(pid) for pid in cart.keys()]
    products = Product.objects.filter(id__in=product_ids)

    # Подсчет общей стоимости корзины
    cart_total = sum(product.price * cart[str(product.id)] for product in products)

    return render(request, 'shop/cart.html', {'products': products, 'cart': cart, 'cart_total': cart_total})

def remove_from_cart(request, product_id):
    """ Уменьшает количество товара в корзине или удаляет его полностью """
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        if cart[str(product_id)] > 1:
            cart[str(product_id)] -= 1
        else:
            del cart[str(product_id)]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('view_cart')
