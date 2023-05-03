from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import ProductForm


def purchase(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "No items in your bag at present")
        return redirect(reverse('all_courses'))

    purchase_form = PurchaseForm()
    template = 'purchase/purchase.html'
    context = {
        'purchase_form': purchase_form,

    }

    return render(request, template, context)
