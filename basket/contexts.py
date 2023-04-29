from decimal import Decimal 
from django.conf import settings

def basket_contents(request):

    basket_items = []
    total = 0
    course_count = 0

    if total > settings.Discount:
        discount = total * Decimal(settings.STANDARD_DISCOUNT*10/100)
        free_discount_delta = FREE_STANDARD_DISCOUNT - total 
    else:
        discount = 0
        free_standard_discount = 0

    grand_total = discount - total 

    context = {basket_items, total, course_count }

    return context
