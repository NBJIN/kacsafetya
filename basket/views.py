from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from courses.models import Courses
from basket.models import Basket

# Create your views here.


def view_basket(request):
    """ View to return basket page """
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of courses to the basket """
    courses = Courses.objects.get(pk=item_id)

    course = get_object_or_404(Courses, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # redirect_url = request.POST.get('add_to_basket')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request,
                         f'Updated {courses.title} quantity to '
                         f'{basket[item_id]}')
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {courses.title} to your basket')
    request.session['basket'] = basket
    return redirect(redirect_url)


def update_basket(request, item_id):
    """ update the quantity of a course to the correct amount  """

    courses = get_object_or_404(Courses, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request,
                         f'Updated {courses.title} quantity to '
                         f'{basket[item_id]}')
    elif quantity == 0:
        del basket[item_id]
        if not basket[item_id]:
            basket.pop(item_id)
            messages.info(request,
                          f'Successfully deleted '
                          f'{courses.title} from your basket')
    else:
        if quantity > 0:
            basket[item_id] = quantity
            messages.success(request,
                             f'updated {courses.title} '
                             f'quantity to {basket[item_id]}')
        else:
            basket.pop(item_id)
            messages.success(request,
                             f'Successfully removed {courses.title} '
                             f'from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def delete_from_basket(request, item_id):
    """ Delete an item from basket  """

    try:
        courses = get_object_or_404(Courses, pk=item_id)
        basket = request.session.get('basket', {})

        del basket[item_id]
        if not basket[item_id]:
            basket.pop(item_id)
            messages.success(request,
                             f'Successfully removed {courses.title} '
                             f'from your basket')
        else:
            basket.pop[item_id]
            messages.success(request,
                             f'Successfully removed {courses.title} '
                             f'from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
