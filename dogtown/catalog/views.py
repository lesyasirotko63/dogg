from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
import time
import hashlib

from .models import Order, Item

# Create your views here.

def index(request):
    """View function for home page of site."""

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_visits': num_visits,
    }

    context = {}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def store(request):
    """View function for home page of site."""

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_visits': num_visits,
    }

    context = {}

    # Render the HTML template store.html with the data in the context variable
    return render(request, 'store.html', context=context)

def akita(request):
    """View function for home page of site."""

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_visits': num_visits,
    }

    context = {}

    # Render the HTML template akita.html with the data in the context variable
    return render(request, 'akita.html', context=context)

def kelpi(request):
    """View function for home page of site."""

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_visits': num_visits,
    }

    context = {}

    # Render the HTML template kelpi.html with the data in the context variable
    return render(request, 'kelpi.html', context=context)

def beagle(request):
    """View function for home page of site."""

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_visits': num_visits,
    }

    context = {}

    # Render the HTML template beagle.html with the data in the context variable
    return render(request, 'beagle.html', context=context)

def bobtail(request):
    """View function for home page of site."""

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_visits': num_visits,
    }

    context = {}

    # Render the HTML template bobtail.html with the data in the context variable
    return render(request, 'bobtail.html', context=context)

def dalmatian(request):
    """View function for home page of site."""

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_visits': num_visits,
    }

    context = {}

    # Render the HTML template dalmatian.html with the data in the context variable
    return render(request, 'dalmatian.html', context=context)

def pitbull(request):
    """View function for home page of site."""

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_visits': num_visits,
    }

    context = {}

    # Render the HTML template pitbull.html with the data in the context variable
    return render(request, 'pitbull.html', context=context)

def bulldog(request):
    """View function for home page of site."""

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_visits': num_visits,
    }

    context = {}

    # Render the HTML template bulldog.html with the data in the context variable
    return render(request, 'bulldog.html', context=context)

def cocker(request):
    """View function for home page of site."""

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_visits': num_visits,
    }

    context = {}

    # Render the HTML template cocker.html with the data in the context variable
    return render(request, 'cocker.html', context=context)

def place_order(request, item_name):
    # YOUR_OBJECT.objects.filter(pk=pk).update(views=F('views')+1)
    print("We've placed an order for your item " + item_name)
    h1 = hashlib.sha1((item_name + str(request.user) + str(datetime.now())).encode("utf-8"))
    order_id = h1.hexdigest()
    h2 = hashlib.sha1((item_name + str(500)).encode("utf-8"))
    item_id = h2.hexdigest()
    item = Item.objects.get_or_create(item_id = item_id, name = item_name, price = 500)
    order = Order(item = item[0], customer = request.user, date = datetime.now(), order_id = order_id)
    order.save()

    context = {
        "order_received": True,
        "item": item_name
    }
    return render(request, 'store.html', context=context)