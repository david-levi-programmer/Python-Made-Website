from django.http import HttpResponse
from django.shortcuts import render


# What the user should see
def index(request):
    return HttpResponse('Hello, world!')


def new(request):
    return HttpResponse("Exciting new products, coming soon!")
