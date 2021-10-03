from django.shortcuts import render, get_object_or_404
from .models import Product, About, WishList
# Create your views here.


def index(request):
    title = Product.title
    product_items = Product.objects.all()
    context = {
        'title': title,
        'product_items': product_items,
    }
    return render(request=request, template_name='index.html', context=context)


def about(request):
    title = 'О проекте'
    all_items = About.objects.all()
    context = {
        'title': title,
        'all_items': all_items,
    }
    return render(request=request, template_name='about.html', context=context)


def list_page(request, pk):
    wishlist = get_object_or_404(WishList, pk)

    title = 'Списки листов желаний'
    context = {
        'title': title,
        'wishlist': wishlist,
    }
    return render(request=request, template_name='wish_list.html', context=context)
