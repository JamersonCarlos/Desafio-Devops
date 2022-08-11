from django.shortcuts import render, redirect
from .models import Item
from redis import Redis


redis = Redis(host='redis', port=6379)


def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', { 
        'items':items
    })
