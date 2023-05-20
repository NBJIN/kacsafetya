from django.http import HttpResponse

from .models import Purchase, PurchaseOrderItem
from courses.models import Courses

import json
import time
import stripe


class StripeWH_Handler:
    """ Handle Stripe Webhooks"""
    # print('StripeWH_Handler')

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """

        # print('handle_payment_intent_succeeded')

        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )
        # need to check the following code
        billing_details = stripe_charge.billing_details  # updated
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)  # updated

        # Clean data in the shipping details - need to check the following code
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        purchase_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                purchase = Purchase.objects.get(
                    fname__iexact=shipping_details.fname,
                    lname__iexact=shipping_details.lname,
                    company__iexact=shipping_details.company,
                    address1__iexact=shipping_details.address.address1,
                    address2__iexact=shipping_details.address.address2,
                    address3__iexact=shipping_details.address.address3,
                    postcode__iexact=shipping_details.address.postcode,
                    telephone__iexact=shipping_details.telephone,
                    email__iexact=billing_details.email,
                    grand_total=grand_total,
                    course_title__iexact=billing_details.course_title,
                    quantity__iexact=billing_details.course_title,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                purchase_exists = True
                break

            except Purchase.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if purchase_exists:
            return HttpResponse(
                content=f'Webhook recieved: {event["type"]} | SUCCESS: Verified purchase already in the database',
                status=200)
        else:
            purchase = None
            try:
                purchase = Purchase.objects.create(
                    fname=shipping_details.fname,
                    lname=shipping_details.lname,
                    company=shipping_details.company,
                    address1=shipping_details.address.address1,
                    address2=shipping_details.address.address2,
                    address3=shipping_details.address.address3,
                    postcode=shipping_details.address.postcode,
                    telephone=shipping_details.telephone,
                    email=billing_details.email,
                    course_title=billing_details.course_title,
                    quantity=billing_details.course_title,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(basket).items():
                    courses = Courses.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        purchase_order_item = PurchaseOrderItem(
                            purchase=purchase,
                            courses=courses,
                            quantity=item_data,
                        )
                        purchase_order_item.save()
                    # else:
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
