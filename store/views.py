from django.shortcuts import render
from . models import Category, Product
from django.shortcuts import get_object_or_404

# Create your views here.


def store(request):
    # Get all products entries from the DB
    all_products = Product.objects.all()
    context = {'all_products': all_products}
    return render(request, 'store/store.html', context)


def categories(request):
    # Get all categories entries from the DB
    all_categories = Category.objects.all()

    return {'all_categories': all_categories}


def product_page(request, slug):
    #  Try to find and get the requested product from the DB
    # find the product by comparing the product's slug in the DB to the product slug we got from the request (url endpoint)
    product = get_object_or_404(Product, slug=slug)

    context = {'product': product}

    return render(request, 'store/product.html', context)
