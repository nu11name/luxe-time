from django.shortcuts import render
from .models import Product, Manufacturer, SpecialOffer, Category, Type

from django.core.mail import send_mail
from django.conf import settings

from django.core.paginator import Paginator


# Create your views here.


def index_en(request):
    products = Product.objects.all()[:8]

    context = {
        'products': products
    }
    return render(request, 'main/en/index.html', context)


def product_details_en(request, slug):
    product = Product.objects.get(slug=slug)

    context = {
        'product': product
    }
    if request.method == 'POST':
        message1 = request.POST['name']
        message2 = request.POST['email']
        message3 = request.POST['number']
        message4 = request.POST['address']
        message5 = product.title

        message ="Full Name: " + message1 + "\n" + "Email: " + message2 + "\n" + "Number: " + message3 + "\n" + "Address: " + message4 + "\n" + "Product Name : " + message5
        send_mail('Lux time',
                  message,
                  settings.EMAIL_HOST_USER,
                  ['luxetim0@gmail.com'],
                  fail_silently=False)
    return render(request, 'main/en/product-page.html',context)


def catalog_en(request):
    products = Product.objects.all()
    manufacturers = Manufacturer.objects.all()

    product_paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)

    context = {
        'page': page,
        # 'products': products,
        'manufacturers': manufacturers
    }
    return render(request, 'main/en/shop.html', context)


def catalog_brand(request, slug):
    products = Product.objects.filter(brand__slug=slug)
    manufacturers = Manufacturer.objects.all()

    product_paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)

    context = {
        'page': page,
        'products': products,
        'brand': Manufacturer.objects.get(slug=slug).title
    }
    return render(request, 'main/en/shop.html', context)


def catalog_discount(request):
    products = Product.objects.filter(is_sale=True)

    product_paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)

    context = {
        'page': page,

        'products': products,
        'discount': True
    }
    return render(request, 'main/en/shop.html', context)


def catalog_category(request, pk):
    products = Product.objects.filter(category__id=pk)

    product_paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)

    context = {
        'page': page,

        'products': products,
        'category': Category.objects.get(id=pk)
    }
    return render(request, 'main/en/shop.html', context)


def catalog_condition(request, cond):
    if cond == "new":
        products = Product.objects.filter(condition="new")
    else:
        products = Product.objects.filter(condition="used")

    product_paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)

    context = {
        'page': page,

        'products': products,
        'condition': cond
    }
    return render(request, 'main/en/shop.html', context)


def catalog_type(request, slug):
    products = Product.objects.filter(type__slug=slug)

    product_paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)

    context = {
        'page': page,

        'products': products,
        'type': Type.objects.get(slug=slug)
    }
    return render(request, 'main/en/shop.html', context)


def catalog_special_offers(request, slug):
    special_offer = SpecialOffer.objects.filter(slug=slug).first()
    products = special_offer.products.all()

    product_paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)

    context = {
        'page': page,

        'products': products,
        'special_offer': special_offer
    }
    return render(request, 'main/en/shop.html', context)


def catalog_price(request):
    products = Product.objects.all()
    price_range = request.GET.get('range', '').replace('$', '').split(' - ')


    min_price = price_range[0]
    max_price = price_range[1]
    products = products.filter(price__gte=min_price, price__lte=max_price)

    product_paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)


    context = {
        'page': page,

        'products': products,
        'price_range': f'${min_price} - ${max_price}'
    }
    return render(request, 'main/en/shop.html', context)


def about_en(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'main/en/about.html', context)


def services_en(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'main/en/services.html', context)


def about_en(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'main/en/about.html', context)


def contact_en(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'main/en/contact.html', context)



########################################################################################################################



def index_ge(request):
    products = Product.objects.all()[:8]

    context = {
        'products': products
    }
    return render(request, 'main/ge/index.html', context)


def product_details_ge(request, slug):
    product = Product.objects.get(slug=slug)

    context = {
        'product': product
    }
    if request.method == 'POST':
        message1 = request.POST['name']
        message2 = request.POST['email']
        message3 = request.POST['number']
        message4 = request.POST['address']
        message5 = product.title

        message ="Full Name: " + message1 + "\n" + "Email: " + message2 + "\n" + "Number: " + message3 + "\n" + "Address: " + message4 + "\n" + "Product Name : " + message5
        send_mail('Lux time',
                  message,
                  settings.EMAIL_HOST_USER,
                  ['luxetim0@gmail.com'],
                  fail_silently=False)
    return render(request, 'main/ge/product-page.html',context)


def catalog_ge(request):
    products = Product.objects.all()
    manufacturers = Manufacturer.objects.all()

    product_paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)


    context = {
        'page': page,

        'products': products,
        'manufacturers': manufacturers
    }
    return render(request, 'main/ge/shop.html', context)


def catalog_brand_ge(request, slug):
    products = Product.objects.filter(brand__slug=slug)
    manufacturers = Manufacturer.objects.all()

    product_paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)


    context = {
        'page': page,

        'products': products,
        'brand': Manufacturer.objects.get(slug=slug).title
    }
    return render(request, 'main/ge/shop.html', context)


def catalog_discount_ge(request):
    products = Product.objects.filter(is_sale=True)

    product_paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)


    context = {
        'page': page,

        'products': products,
        'discount': True
    }
    return render(request, 'main/ge/shop.html', context)


def catalog_category_ge(request, pk):
    products = Product.objects.filter(category__id=pk)

    product_paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)


    context = {
        'page': page,

        'products': products,
        'category': Category.objects.get(id=pk)
    }
    return render(request, 'main/ge/shop.html', context)


def catalog_condition_ge(request, cond):
    if cond == "new":
        products = Product.objects.filter(condition="new")
    else:
        products = Product.objects.filter(condition="used")

    product_paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)


    context = {
        'page': page,

        'products': products,
        'condition': cond
    }
    return render(request, 'main/ge/shop.html', context)


def catalog_type_ge(request, slug):
    products = Product.objects.filter(type__slug=slug)


    product_paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)


    context = {
        'page': page,

        'products': products,
        'type': Type.objects.get(slug=slug)
    }
    return render(request, 'main/ge/shop.html', context)


def catalog_special_offers_ge(request, slug):
    special_offer = SpecialOffer.objects.filter(slug=slug).first()
    products = special_offer.products.all()

    product_paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)

    context = {
        'page': page,

        'products': products,
        'special_offer': special_offer
    }
    return render(request, 'main/ge/shop.html', context)


def catalog_price_ge(request):
    products = Product.objects.all()
    price_range = request.GET.get('range', '').replace('$', '').split(' - ')




    min_price = price_range[0]
    max_price = price_range[1]

    products = products.filter(price__gte=min_price, price__lte=max_price)


    product_paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)



    context = {
        'page': page,

        'products': products,
        'price_range': f'${min_price} - ${max_price}'
    }
    return render(request, 'main/ge/shop.html', context)


def about_ge(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'main/ge/about.html', context)


def services_ge(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'main/ge/services.html', context)


def about_ge(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'main/ge/about.html', context)


def contact_ge(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'main/ge/contact.html', context)



########################################################################################################################



def index_ru(request):
    products = Product.objects.all()[:8]

    context = {
        'products': products
    }
    return render(request, 'main/ru/index.html', context)


def product_details_ru(request, slug):
    product = Product.objects.get(slug=slug)

    context = {
        'product': product
    }
    if request.method == 'POST':
        message1 = request.POST['name']
        message2 = request.POST['email']
        message3 = request.POST['number']
        message4 = request.POST['address']
        message5 = product.title

        message ="Full Name: " + message1 + "\n" + "Email: " + message2 + "\n" + "Number: " + message3 + "\n" + "Address: " + message4 + "\n" + "Product Name : " + message5
        send_mail('Lux time',
                  message,
                  settings.EMAIL_HOST_USER,
                  ['luxetim0@gmail.com'],
                  fail_silently=False)
    return render(request, 'main/ru/product-page.html',context)


def catalog_ru(request):
    products = Product.objects.all()
    manufacturers = Manufacturer.objects.all()

    product_paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)


    context = {
        'page': page,

        'products': products,
        'manufacturers': manufacturers
    }
    return render(request, 'main/ru/shop.html', context)


def catalog_brand_ru(request, slug):
    products = Product.objects.filter(brand__slug=slug)
    manufacturers = Manufacturer.objects.all()

    product_paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)


    context = {
        'page': page,

        'products': products,
        'brand': Manufacturer.objects.get(slug=slug).title
    }
    return render(request, 'main/ru/shop.html', context)


def catalog_discount_ru(request):
    products = Product.objects.filter(is_sale=True)

    product_paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)


    context = {
        'page': page,

        'products': products,
        'discount': True
    }
    return render(request, 'main/ru/shop.html', context)


def catalog_category_ru(request, pk):
    products = Product.objects.filter(category__id=pk)

    product_paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)


    context = {
        'page': page,

        'products': products,
        'category': Category.objects.get(id=pk)
    }
    return render(request, 'main/ru/shop.html', context)


def catalog_condition_ru(request, cond):
    if cond == "new":
        products = Product.objects.filter(condition="new")
    else:
        products = Product.objects.filter(condition="used")

    product_paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)


    context = {

        'page': page,

        'products': products,
        'condition': cond
    }
    return render(request, 'main/ru/shop.html', context)


def catalog_type_ru(request, slug):
    products = Product.objects.filter(type__slug=slug)

    product_paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)


    context = {

        'page': page,

        'products': products,
        'type': Type.objects.get(slug=slug)
    }
    return render(request, 'main/ru/shop.html', context)


def catalog_special_offers_ru(request, slug):
    special_offer = SpecialOffer.objects.filter(slug=slug).first()
    products = special_offer.products.all()

    product_paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)


    context = {

        'page': page,

        'products': products,
        'special_offer': special_offer
    }
    return render(request, 'main/ru/shop.html', context)


def catalog_price_ru(request):
    products = Product.objects.all()
    price_range = request.GET.get('range', '').replace('$', '').split(' - ')




    min_price = price_range[0]
    max_price = price_range[1]

    products = products.filter(price__gte=min_price, price__lte=max_price)

    product_paginator = Paginator(products, 12)
    page_num = request.GET.get('page')
    page = product_paginator.get_page(page_num)


    context = {

        'page': page,

        'products': products,
        'price_range': f'${min_price} - ${max_price}'
    }
    return render(request, 'main/ru/shop.html', context)


def about_ru(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'main/ru/about.html', context)


def services_ru(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'main/ru/services.html', context)


def about_ru(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'main/ru/about.html', context)


def contact_ru(request):
    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'main/ru/contact.html', context)
