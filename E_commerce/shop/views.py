from django.shortcuts import render

from .models import Products
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    Product_objects = Products.objects.all()
    
    # Search Code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        Product_objects = Product_objects.filter(title__icontains = item_name)

    # Paginator code
    paginator = Paginator(Product_objects,4)
    page = request.GET.get('page')
    Product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', {'Product_objects': Product_objects})


def Detail(request, id):
    Detail_objects = Products.objects.get(id=id)
    context = {
        'details_objects': Detail_objects
    }
    return render(request, 'shop/detail.html', context)


def Addcart(request):
    Cart_detail = Products.objects.all()

    

    context = {
        'Cart_detail': Cart_detail,
    }

    return render(request, 'shop/addcart.html', context)

def Checkout(request):

    return render(request, 'shop/checkout.html')
