from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'landing/index.html')
