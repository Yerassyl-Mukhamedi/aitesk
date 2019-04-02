from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import EmailMessage, send_mail
from django.template.loader import get_template
from django.http import HttpResponse
from .models import Category, Product

from .forms import *

def index(request, category_slug=None):
    category=None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    products_list = Product.objects.order_by('?')[:2]
    menu_list = Product.objects.order_by('?')[:1]
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)


    if request.method == 'POST':
        if 'call' in request.POST:
            form = CallForm(request.POST)
            if form.is_valid():
                sender_name = form.cleaned_data['name']
                sender_phone = form.cleaned_data['phone']
                sender_email = 'oinf305@gmail.com'
                
                message = "Заявка на звонок: \n Имя: {0}\n\n Номер:  {1}".format(sender_name, sender_phone)
                send_mail('New Enquiry', message, sender_email, ['erasyl490@gmail.com'], fail_silently=False,)
                return HttpResponse('Спасибо за обращение, с вами свяжутся в ближайшее время!')
        else: 
            form = CallForm(request.POST)
            if form.is_valid():
                sender_name = form.cleaned_data['name']
                sender_name1 = form.cleaned_data['name1']
                sender_phone = form.cleaned_data['phone']
                sender_email = 'oinf305@gmail.com'

                message = "Заявка на звонок: \n Имя: {0}\n Номер:  {1} \n Название товара:{2}".format(sender_name, sender_phone, sender_name1)
                send_mail('New Enquiry', message, sender_email, ['erasyl490@gmail.com'], fail_silently=False,)
                return HttpResponse('Спасибо за заказ, с вами свяжутся в ближайшее время!')
    else:
        form = CallForm()
    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'products_list' : products_list,
        'menu_list' : menu_list,
        'form': form,
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

    if request.method == 'POST':
        if 'call' in request.POST:
            form = CallForm(request.POST)
            if form.is_valid():
                sender_name = form.cleaned_data['name']
                sender_phone = form.cleaned_data['phone']
                sender_email = 'oinf305@gmail.com'
                
                message = "Заявка на звонок: \n Имя: {0}\n\n Номер:  {1}".format(sender_name, sender_phone)
                send_mail('New Enquiry', message, sender_email, ['erasyl490@gmail.com'], fail_silently=False,)
                return HttpResponse('Спасибо за обращение, с вами свяжутся в ближайшее время!')
        else: 
            form = CallForm(request.POST)
            if form.is_valid():
                sender_name = form.cleaned_data['name']
                sender_name1 = form.cleaned_data['name1']
                sender_phone = form.cleaned_data['phone']
                sender_email = 'oinf305@gmail.com'

                message = "Заявка на звонок: \n Имя: {0}\n Номер:  {1} \n Название товара:{2}".format(sender_name, sender_phone, sender_name1)
                send_mail('New Enquiry', message, sender_email, ['erasyl490@gmail.com'], fail_silently=False,)
                return HttpResponse('Спасибо за заказ, с вами свяжутся в ближайшее время!')
    else:
        form = CallForm()

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'main_category': main_category,
        'menu_list' : menu_list,
        'form' : form,
    }
    return render(request, 'polls/product/list.html', context)


def product_detail(request, id, slug):
    if request.method == 'POST':
        if 'call' in request.POST:
            form = CallForm(request.POST)
            if form.is_valid():
                sender_name = form.cleaned_data['name']
                sender_phone = form.cleaned_data['phone']
                sender_email = 'oinf305@gmail.com'
                
                message = "Заявка на звонок: \n Имя: {0}\n\n Номер:  {1}".format(sender_name, sender_phone)
                send_mail('New Enquiry', message, sender_email, ['erasyl490@gmail.com'], fail_silently=False,)
                return HttpResponse('Спасибо за обращение, с вами свяжутся в ближайшее время!')
        else: 
            form = CallForm(request.POST)
            if form.is_valid():
                sender_name = form.cleaned_data['name']
                sender_name1 = form.cleaned_data['name1']
                sender_phone = form.cleaned_data['phone']
                sender_email = 'oinf305@gmail.com'

                message = "Заявка на звонок: \n Имя: {0}\n Номер:  {1} \n Название товара:{2}".format(sender_name, sender_phone, sender_name1)
                send_mail('New Enquiry', message, sender_email, ['erasyl490@gmail.com'], fail_silently=False,)
                return HttpResponse('Спасибо за заказ, с вами свяжутся в ближайшее время!')
    else:
        form = CallForm()


    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    
    best_offer = Product.objects.all()
    menu_list = Product.objects.order_by('?')[:1]

    context = {
        'product': product,
        'best_offer' : best_offer,
        'menu_list' : menu_list,
        'form': form,
    }
    return render(request, 'polls/product/detail.html', context)



def catalog(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    menu_list = Product.objects.order_by('?')[:1]
    best_offer = Product.objects.order_by('?')[:4]


    if request.method == 'POST':
        if 'call' in request.POST:
            form = CallForm(request.POST)
            if form.is_valid():
                sender_name = form.cleaned_data['name']
                sender_phone = form.cleaned_data['phone']
                sender_email = 'oinf305@gmail.com'
                
                message = "Заявка на звонок: \n Имя: {0}\n\n Номер:  {1}".format(sender_name, sender_phone)
                send_mail('New Enquiry', message, sender_email, ['erasyl490@gmail.com'], fail_silently=False,)
                return HttpResponse('Спасибо за обращение, с вами свяжутся в ближайшее время!')
        else: 
            form = CallForm(request.POST)
            if form.is_valid():
                sender_name = form.cleaned_data['name']
                sender_name1 = form.cleaned_data['name1']
                sender_phone = form.cleaned_data['phone']
                sender_email = 'oinf305@gmail.com'

                message = "Заявка на звонок: \n Имя: {0}\n Номер:  {1} \n Название товара:{2}".format(sender_name, sender_phone, sender_name1)
                send_mail('New Enquiry', message, sender_email, ['erasyl490@gmail.com'], fail_silently=False,)
                return HttpResponse('Спасибо за заказ, с вами свяжутся в ближайшее время!')
    else:
        form = CallForm()


    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'menu_list' : menu_list,
        'best_offer' : best_offer,
        'form' : form,
    }

    return render(request, 'polls/catalog.html', context)


def contact(request):
    if request.method == 'POST':
        if 'call' in request.POST:
            form = CallForm(request.POST)
            if form.is_valid():
                sender_name = form.cleaned_data['name']
                sender_phone = form.cleaned_data['phone']
                sender_email = 'oinf305@gmail.com'
                
                message = "Заявка на звонок: \n Имя: {0}\n\n Номер:  {1}".format(sender_name, sender_phone)
                send_mail('New Enquiry', message, sender_email, ['erasyl490@gmail.com'], fail_silently=False,)
                return HttpResponse('Спасибо за обращение, с вами свяжутся в ближайшее время!')
        elif 'contact' in request.POST:
            form = CallForm(request.POST)
            if form.is_valid():
                sender_name = form.cleaned_data['name']
                sender_phone = form.cleaned_data['phone']
                sender_email = 'oinf305@gmail.com'
                
                message = "Заявка на звонок: \n Имя: {0}\n\n Номер:  {1}".format(sender_name, sender_phone)
                send_mail('New Enquiry', message, sender_email, ['erasyl490@gmail.com'], fail_silently=False,)
                return HttpResponse('Спасибо за обращение, с вами свяжутся в ближайшее время!')
        # else: 
        #     form = CallForm(request.POST)
        #     if form.is_valid():
        #         sender_name = form.cleaned_data['name']
        #         sender_name1 = form.cleaned_data['name1']
        #         sender_phone = form.cleaned_data['phone']
        #         sender_message = form.cleaned_data['message']
        #         sender_email = 'oinf305@gmail.com'

        #         message = "Заявка на звонок: \n Имя: {0}\n Номер:  {1} \n Название товара:{2}{3}".format(sender_name, sender_phone, sender_name1, sender_message)
        #         send_mail('New Enquiry', message, sender_email, ['erasyl490@gmail.com'], fail_silently=False,)
        #         return HttpResponse('Спасибо за заказ, с вами свяжутся в ближайшее время!')
    else:
        form = CallForm()

    return render(request, 'polls/contact.html', {'form': form})


def about(request):
    menu_list = Product.objects.order_by('?')[:1]

    if request.method == 'POST':
        if 'call' in request.POST:
            form = CallForm(request.POST)
            if form.is_valid():
                sender_name = form.cleaned_data['name']
                sender_phone = form.cleaned_data['phone']
                sender_email = 'oinf305@gmail.com'
                
                message = "Заявка на звонок: \n Имя: {0}\n\n Номер:  {1}".format(sender_name, sender_phone)
                send_mail('New Enquiry', message, sender_email, ['erasyl490@gmail.com'], fail_silently=False,)
                return HttpResponse('Спасибо за обращение, с вами свяжутся в ближайшее время!')
        else: 
            form = CallForm(request.POST)
            if form.is_valid():
                sender_name = form.cleaned_data['name']
                sender_name1 = form.cleaned_data['name1']
                sender_phone = form.cleaned_data['phone']
                sender_email = 'oinf305@gmail.com'

                message = "Заявка на звонок: \n Имя: {0}\n Номер:  {1} \n Название товара:{2}".format(sender_name, sender_phone, sender_name1)
                send_mail('New Enquiry', message, sender_email, ['erasyl490@gmail.com'], fail_silently=False,)
                return HttpResponse('Спасибо за заказ, с вами свяжутся в ближайшее время!')
    else:
        form = CallForm()
    context = {
        'menu_list' : menu_list,
        'form' : form,
    }


    return render(request, 'polls/about.html', context)