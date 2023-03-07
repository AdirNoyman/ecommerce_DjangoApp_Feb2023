from django.shortcuts import render
from . models import Category

# Create your views here.


def store(request):

    return render(request, 'store/store.html')


def categories(request):
    # Get all categories entries from the DB
    all_categories = Category.objects.all()

    return {'all_categories': all_categories}
