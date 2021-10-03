from django.shortcuts import render
from .models import Product
# Create your views here.


def index(request):
    title = Product.title
    product_items = Product.objects.all()
    context = {
        'title': title,
        'product_items': product_items,
    }
    return render(request=request, template_name='index.html', context=context)