from django.shortcuts import render
from . models import ProductCard

def Dukan (request) :

    mens_product = ProductCard.objects.filter(categories = 'Mens')

    return render (request, 'mens.html', {'products' : mens_product})

def Ladies (request) :

    ladies_product = ProductCard.objects.filter(categories = 'Ladies')

    return render (request, 'ladies.html', {'products' : ladies_product})