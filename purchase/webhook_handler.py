from django.http import HttpResponse

from .models import Purchase, PurchaseOrderItem
from courses.models import Courses

import json
import time

class StripeWH_Handler:
    """ Handle Stripe Webhooks"""

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
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )
         # need to check the following code
        customer_details = stripe_charge.customer_details # updated
        contact_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2) # updated


        # Clean data in the shipping details - need to check the following code 
        for field, value in contact_details.address.items():
            if value == "":
                contact_details.address[field] = None 

        purchase_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                purchase = Purchase.objects.get(
                    fname_name__iexact=contact_details.fname,
                    lname_name__iexact=contact_details.lname,
                    company_name__iexact=contact_details.company,
                    address1_iexact=contact_details.address.address1,
                    address2_iexact=contact_details.address.address2,
                    address3_iexact=contact_details.address.address3,
                    postcode__iexact=contact_details.address.postcode,
                    telephone__iexact=contact_details.telephone,
                    email__iexact=contact_details.email,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                purchase_exists = True
                break
                
            except Purchase.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook recieved: {event["type"]} | SUCCESS: Verified purchase already in the database',
                status=200)
        else:
            try:
                purchase = Purchase.objects.create(
                    fname=contact_details.fname,
                    lname=contact_details.lname,
                    company=contact_details.company,
                    address1=contact_details.address.address1,
                    address2=contact_details.address.address2,
                    address3=contact_details.address.address3,
                    postcode=contact_details.address.postcode,
                    telephone=contact_details.telephone,
                    email=contact_details.email,
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
