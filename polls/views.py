from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Product

def index(request):
    latest_product_list = Product.objects.order_by('id')[:4]
    context = {
        'latest_product_list': latest_product_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'polls/detail.html', {'product': product})