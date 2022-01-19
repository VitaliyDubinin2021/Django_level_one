from basketapp.models import Basket


def basket(request):
    print(f'Контекстный процессор отработал!')
    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    return {
        'basket': basket,
    }