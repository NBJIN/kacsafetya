from decimal import Decimal
from django.conf import settings


def basket_contents(request):

    basket_items = []
    grand_total = 0
    course_count = 0

    if grand_total < settings.DISCOUNT:
        grand_total = total * Decimal(settings.STANDARD_DISCOUNT_PERCENTAGE*10/100)
        free_discount_delta = FREE_DISCOUNT - total 
    else:
        discount = 0
        free_discount_delta = 0

    grand_total = discount - total

    context = {
        'basket_items', basket_items,
        'grand_total', grand_total,
        'course_count', course_count,
        'settings.DISCOUNT', settings.DISCOUNT,
        'free_discount_delta', free_discount_delta,
        'settings.STANDARD_DISCOUNT_PERCENTAGE', settings.STANDARD_DISCOUNT_PERCENTAGE,
        }

    return context
