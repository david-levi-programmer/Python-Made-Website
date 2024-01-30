from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# What the user should see
def index(request):
    products = Product.objects.all()
    return render(request,
                  'index.html', {'products':products})


def new(request):
    return HttpResponse("Exciting new products, coming soon!")
