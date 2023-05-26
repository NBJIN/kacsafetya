from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserDashboard
from .forms import UserDashboardForm

from purchase.models import Purchase


def dashboard(request):
    """
    Display the users dashboard
    """
    dashboard = get_object_or_404(UserDashboard, user=request.user)

    if request.method == 'POST':
        form = UserDashboardForm(request.POST, instance=dashboard)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Dashboard has been updated successfully with your details')
        else:
            messages.error(request, 'Failed to update dashboard please check form.')
    else:
        form = UserDashboardForm(instance=dashboard)
    purchase = dashboard.purchase.all()

    template = 'dashboard/dashboard.html'
    context = {
        'form': form,
        'purchase': purchase,
        'on_dashboard_page': True
    }

    return render(request, template, context)


def purchase_records(request, purchase_no):
    purchase = get_object_or_404(Purchase, purchase_no=purchase_no)

    messages.info(request, (
        f'This is a previous pruchase confirmation for purchase number {purchase_no}. '
        'An email confirmation same was sent on the purchase date.'
    ))

    template = 'purchase/purchase_success.html'
    context = {
        'purchase': purchase,
        'from_dashboard': True,
    }

    return render(request, template, context)
