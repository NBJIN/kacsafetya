from django.http import HttpResponse


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
        # need to check the following code 
        customer_details = intent.charges.data[0].customer_details
        contact_details = intent.contact
        grand_total = round(intent.data.charges[0].amount / 100, 2)

        # Clean data in the shipping details - need to check the following code 
        for field, value in contact_details.address.items():
            if value == "":
                contact_details.address[field] = None 

        purchase_exists = False
        try:
            purchase = Purchase.objects.get(
                fname_name__iexact=contact_details.fname,
                lname_name__iexact=contact_details.lname,
                company_name__iexact=contact_details.company,
                address1_iexact=contact_details.address1,
                address2_iexact=contact_details.address2,
                address3_iexact=contact_details.address3,
                postcode__iexact=contact_details.postcode,
                telephone__iexact=contact_details.telephone,
                email__iexact=contact_details.email,
            )
            purchase_exists = True
            return HttpResponse(
                content=f'Webhook recieved: {event["type"]} | SUCCESS: Verified order already in the database',
                status=200)
        except Purchase.DoesNotExist:
               for item_id, item_data in basket.items():
                try:
                    courses = Courses.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        purchase_order_item = PurchaseOrderItem(
                            # purchase_no=purchase_no,
                            purchase=purchase,
                            courses=courses,
                            quantity=item_data,
                        )
                        purchase_order_item.save()
                  









        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
