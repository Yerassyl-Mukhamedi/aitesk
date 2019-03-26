from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import EmailMessage, send_mail
from django.template.loader import get_template
from django.http import HttpResponse
from .models import Category, Product

from .forms import ContactForm

def index(request, category_slug=None):
    category=None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    products_list = Product.objects.order_by('?')[:2]
    menu_list = Product.objects.order_by('?')[:1]
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
    categories = Category.objects.filter( sub_category = True)
    menu_list = Product.objects.order_by('?')[:1]

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
        main_category = Category.objects.filter(slug=category_slug)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'main_category': main_category,
        'menu_list' : menu_list,
    }
    return render(request, 'polls/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    
    best_offer = Product.objects.all()
    menu_list = Product.objects.order_by('?')[:1]

    context = {
        'product': product,
        'best_offer' : best_offer,
        'menu_list' : menu_list,
    }
    return render(request, 'polls/product/detail.html', context)



def catalog(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    menu_list = Product.objects.order_by('?')[:1]
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


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['erasyl490@gmail.com'], fail_silently=False,)
            return HttpResponse('Thanks for contacting us!')
    else:
        form = ContactForm()

    return render(request, 'polls/contact.html', {'form': form})


def about(request):
    menu_list = Product.objects.order_by('?')[:1]

    context = {
        'menu_list' : menu_list,
    }


    return render(request, 'polls/about.html', context)