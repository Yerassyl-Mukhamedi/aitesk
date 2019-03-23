from django.shortcuts import render, get_object_or_404
from .models import Category, Product



def index(request, category_slug=None):
    category=None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    products_list = Product.objects.order_by('category')[:2]
    menu_list = Product.objects.order_by('category')[:1]
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'products_list' : products_list,
        'menu_list' : menu_list,
    }
    return render(request, 'polls/index.html', context)

def product_list(request, category_slug):
    category = None
    main_category = Category.objects.filter(parent=None)
    products = Product.objects.filter(available=True)
    categories = Category.objects.filter( sub_category = True )

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
        main_category = Category.objects.filter(slug=category_slug)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'main_category': main_category,
    }
    return render(request, 'polls/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    context = {
        'product': product
    }
    return render(request, 'polls/product/detail.html', context)



def catalog(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    menu_list = Product.objects.order_by('category')[:1]
    best_offer = Product.objects.order_by('?')[:4]

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'menu_list' : menu_list,
        'best_offer' : best_offer,
    }

    return render(request, 'polls/catalog.html', context)

