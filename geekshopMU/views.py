from django.shortcuts import render
from mainapp.models import Product

def index(request):
    title = 'Магазин атрибутики'
    products = Product.objects.all()[:3]
    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'geekshopMU/index.html', context=context)


def contacts(request):
    title = 'Контактная информация',
    # 'products': products
    context = {
        'title': title,
    }
    return render(request, 'geekshopMU/contacts.html', context=context)
