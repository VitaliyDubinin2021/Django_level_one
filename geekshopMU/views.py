from django.shortcuts import render


def index(request):
    return render(request, 'geekshopMU/index.html')


def contacts(request):
    return render(request, 'geekshopMU/contacts.html')
