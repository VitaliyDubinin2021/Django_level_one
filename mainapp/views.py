from django.shortcuts import render


def products(request):
    title = 'Каталог продукции'
    links_menu = [
        {'href': 'products/', 'name': 'Все продукты'},
        {'href': 'products_huge', 'name': 'Для взрослых'},
        {'href': 'products_kids', 'name': 'Для детей'},
    ]

    context = {
        'title': title,
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', context=context)

