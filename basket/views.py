from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from courses.models import Courses
from basket.models import Basket

# Create your views here.


def view_basket(request):
    """ View to return basket page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of courses to the basket """

    course = get_object_or_404(Courses, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)
