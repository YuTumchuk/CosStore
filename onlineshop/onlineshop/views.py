from store.models import Products
from django.shortcuts import render


def home (request):
    products = Products.objects.all().filter(is_available=True)
    context = {
        'products': products,
    }
    return render(request, template_name='index.html', context=context)

