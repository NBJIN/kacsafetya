from django.shortcuts import render, redirect, reverse, HttpResponse
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


def update_basket(request, item_id):
    """ update the quantity of a course to the correct amount  """

    # course = get_object_or_404(Courses, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    elif quantity == 0:
        del basket[item_id]
        if not basket[item_id]:
            bag.pop(item_id)
    else:
        if quantity > 0:
            basket[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def delete_from_basket(request, item_id):
    """ Delete an item from basket  """

    try:
        basket = request.session.get('basket', {})

        del basket[item_id]
        if not basket[item_id]:
            bag.pop(item_id)
        else:
            bag.pop[item_id]

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
