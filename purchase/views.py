from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import PurchaseForm


def purchase(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "No items in your bag at present")
        return redirect(reverse('all_courses'))

    purchase_form = PurchaseForm()
    template = 'purchase/purchase.html'
    context = {
        'purchase_form': purchase_form,
        'stripe_public_key': 'pk_test_51MkRbADXf5h0wE6pVKuwXnUgvGX4IJilzaVpBltzeFkJBEc6Bam50b7t9xto2u6G4tYbbOHnebMKIgPj1NEc71HY00KCkNss9a',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
