from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from courses.models import Courses


def basket_contents(request):

    basket_items = []
    grand_total = 0
    total = 0
    courses_count = 0
    # FREE_DISCOUNT = 0
    # discount = 0
    basket = request.session.get('basket', {})
    discount = total * 10 / 100

    # for item_id, quantity in basket.items():
    # #     courses = get_object_or_404(Courses, pk=item_id)
    #     total += quantity * courses.fee
    #     courses_count += quantity
    #     basket_items.append({
    #         'item_id': item_id,
    #         'quantity': quantity,
    #         'courses': courses,
    #     })

    if total > settings.FREE_DISCOUNT: # if my total is greater than 200
        discount = total * Decimal(settings.STANDARD_DISCOUNT_PERCENTAGE * 10/100)  # grand total is = to total
        free_discount_delta = settings.FREE_DISCOUNT - total  # free discount delta is equal to free discount minus total
    # free_discount_delta = settings.FREE_DISCOUNT - total

    else:
        discount = 0
        free_discount_delta = 0

    grand_total = total + discount

    context = {
        'basket_items': basket_items,
        'grand_total': grand_total,
        'total': total,
        'courses_count': courses_count,
        'discount': discount,
        'free_discount': settings.FREE_DISCOUNT,
        'free_discount_delta': free_discount_delta,
        'standard_discount_percentage': settings.STANDARD_DISCOUNT_PERCENTAGE,
    }

    return context
