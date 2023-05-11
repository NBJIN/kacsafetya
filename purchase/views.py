from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import PurchaseForm
from .models import Purchase, PurchaseOrderItem
from courses.models import Courses
from basket.contexts import basket_contents

import stripe


def purchase(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'fname': request.POST['fname'],
            'lname': request.POST['lname'],
            'company': request.POST['company'],
            'address1': request.POST['address1'],
            'address2': request.POST['address2'],
            'address3': request.POST['address3'],
            'postcode': request.POST['postcode'],
            'telephone': request.POST['telephone'],
            'email': request.POST['email'],
            'course_title': request.POST['course_title'],
            'quantity': request.POST['quantity'],
        }
        purchase_form = PurchaseForm(form_data)
        if purchase_form.is_valid():
            purchase = purchase_form.save()
            for item_id, item_data in basket.items():
                try:
                    courses = Courses.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        purchase_order_item = PurchaseOrderItem(
                            purchase_no=purchase_no,
                            courses=courses,
                            quantity=item_data,
                        )
                        purchase_order_item.save()
                    else:
                        purchase_order_item.save()
                except Courses.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your basket wasn't found in our database. "
                        "Make contact for assistance")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))
            request.sesstion['save_info'] = 'save-info' in request.POST
            return redirect(reverse('purchase_success', args[purchase.purchase_no]))
        else:
            messages.error(request, 'There was an error with your form. \
            Please check your details.')
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "No items in your bag at present")
            return redirect(reverse('all_courses'))

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY, 

        )
        purchase_form = PurchaseForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')
    template = 'purchase/purchase.html'
    context = {
        'purchase_form': purchase_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def purchase_success(request, purchase_no):
    """
    view to return a successful purchase
    """
    save_info = request.session.get('save_info')
    purchase = get_object_or_404(Purchase, purchase_no=purchase_no)
    messages.success(request, f'Purchase succfully processed \
        Your purchase order number is {purchase_no}. Confirmation \
        of your purchase has been sent to {purchase.email}')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'purchase/purchase_success.html'
    context = {
        'purchase': purchase,
    }

    return render(request, template, context)
