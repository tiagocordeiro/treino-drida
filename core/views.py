from django.shortcuts import render

from .models import Product

def home(request):
    return render(request, 'home.html')

def produtos_list(request):
    produtos = Product.objects.all()
    context = {'produtos': produtos,
                'teste': 'Apenas um teste', }
    return render(request, 'products/list.html', context)
