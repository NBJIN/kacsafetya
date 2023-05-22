from django.http import HttpResponse

from .models import Purchase, PurchaseOrderItem
from courses.models import Courses
from dashboard.models import UserDashboard

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

        # Update dashboard details when save_info is checked
        dashboard = None 
        username = intent.metadata.username
        if username != 'AnonymousUser':
            dashboard = UserDashboard.objects.get(user__username=username)
            if save_info:
                dashboard.default_address1 = shipping_details.address.line1
                dashboard.default_address2 = shipping_details.address.line2
                # dashboard.default_address3 = shipping_details.address.county
                dashboard.default_postcode = shipping_details.address.postal_code
                dashboard.default_telephone = shipping_details.phone
                dashboard.save()

        purchase_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                purchase = Purchase.objects.get(
                    fullname__iexact=shipping_details.name,
                    # company__iexact=shipping_details.company,
                    address1__iexact=shipping_details.address.line1,
                    address2__iexact=shipping_details.address.line2,
                    # address3__iexact=shipping_details.address.county,
                    postcode__iexact=shipping_details.address.postal_code,
                    telephone__iexact=shipping_details.phone,
                    email__iexact=billing_details.email,
                    grand_total=grand_total,
                    # course_title__iexact=billing_details.course_title,
                    # quantity__iexact=billing_details.course_title,
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
                    fullname=shipping_details.name,
                    user_dashboard=dashboard,
                    # company=shipping_details.company,
                    address1=shipping_details.address.line1,
                    address2=shipping_details.address.line2,
                    # address3=shipping_details.address.county,
                    postcode=shipping_details.address.postcode,
                    telephone=shipping_details.phone,
                    email=billing_details.email,
                    # course_title=billing_details.course_title,
                    # quantity=billing_details.course_title,
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
                if purchase:
                    purchase.delete()
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
