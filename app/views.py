from django.shortcuts import render
from django.http import HttpResponse

def frontpage(request):
    return HttpResponse('<p2>Welcome to our awesome application!</p2>') 

# def base(request):
    # return render(request, "components/base.html")

def home_view(request):
    return render(request, 'components/home.html', {'page_title': 'Home'})

def dashboard_view(request):
    return render(request, 'components/dashboard.html', {'page_title': 'Dashboard'})

def product_list_view(request):
    products = [
        {'id': 1, 'name': 'Product A'},
        {'id': 2, 'name': 'Product B'},
    ]
    return render(request, 'components/products/product_list.html', {'page_title': 'Products', 'products': products})

def product_detail_view(request, pk):
    # In a real app, you'd fetch from a database
    product = {'id': pk, 'name': f'Product {chr(64 + pk)}'}
    return render(request, 'components/products/product_detail.html', {'page_title': f'Product {pk}', 'product': product})