from django.shortcuts import render

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