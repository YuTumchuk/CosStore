from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from cart.models import CartItem
from cart.views import _cart_id
from category.models import Category
from store.models import Products


def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:

        categories = get_object_or_404(Category, slug=category_slug)
        products = Products.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        paged_proudcts = paginator.get_page(page)
        products_count = products.count()
    else:
        products = Products.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        paged_proudcts = paginator.get_page(page)
        products_count = products.count()
    context = {
        'products': paged_proudcts,
        'product_count': products_count,
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Products.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()


    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }

    return render(request, 'store/product-detail.html', context)


def search(request):
    products=None
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Products.objects.order_by('-created_date').filter(Q(description__icontains=keyword)| Q(product_name__icontains=keyword))
    products_count = products.count()
    context = {
        'products': products,
        'product_count': products_count,
    }
    return render(request, 'store/store.html', context)
