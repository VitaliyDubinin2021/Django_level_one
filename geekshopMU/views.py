from django.shortcuts import render


def index(request):
    title = 'Магазин атрибутики'
    context = {
        'title': title,
    }
    return render(request, 'geekshopMU/index.html', context=context)


def contacts(request):
    title = 'Контактная информация'
    context = {
        'title': title,
    }
    return render(request, 'geekshopMU/contacts.html', context=context)
