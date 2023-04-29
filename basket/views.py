from django.shortcuts import render

# Create your views here.


def view_basket(request):
    """ View to return basket page """

    return render(request, 'basket/basket.html')
