from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Project
from .models import Contact
from .choises import price_choices, type_choices


def home(request):
    listings = Project.objects.order_by('-project_date').filter(is_published=True).filter(is_main_page=True)
    context = {
        'projects': listings,
        'price_choices': price_choices,
        'types': type_choices,
    }
    return render(request, 'dombrusapp/home.html', context)


def project(request, project_id):
    listing_item = get_object_or_404(Project, pk=project_id)
    context = {
        'project': listing_item
    }
    return render(request, 'dombrusapp/project.html', context)


def brus(request):
    listings = Project.objects.order_by('-project_date').filter(is_published=True).filter(type='Br')
    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'projects': paged_listings
    }
    return render(request, 'dombrusapp/brus.html', context)


def bani(request):
    listings = Project.objects.order_by('-project_date').filter(is_published=True).filter(type='Ba')
    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'projects': paged_listings
    }
    return render(request, 'dombrusapp/bani.html', context)


def karkas(request):
    listings = Project.objects.order_by('-project_date').filter(is_published=True).filter(type='Ka')
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'projects': paged_listings
    }
    return render(request, 'dombrusapp/karkas.html', context)


def contacts(request):
    contact_lists = Contact.objects.all()
    context = {
        'contacts': contact_lists
    }
    return render(request, 'dombrusapp/contact.html', context)


def search(request):
    queryset_list = Project.objects.order_by('-project_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    if 'size' in request.GET:
        size = request.GET['size']
        if size:
            queryset_list = queryset_list.filter(size__icontains=size)

    if 'type' in request.GET:
        type_value = request.GET['type']
        if type_value:
            queryset_list = queryset_list.filter(type__iexact=type_value)

    # if 'state' in request.GET:
    #     state = request.GET['state']
    #     if state:
    #         queryset_list = queryset_list.filter(state__iexact=state)
    #
    # if 'bedrooms' in request.GET:
    #     bedrooms = request.GET['bedrooms']
    #     if bedrooms:
    #         queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'projects': queryset_list,
        'values': request.GET,
        'price_choices': price_choices,
        'types': type_choices,
    }
    return render(request, 'dombrusapp/search.html', context)
