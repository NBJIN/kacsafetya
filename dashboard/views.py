from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserDashboard
from .forms import UserDashboardForm


def dashboard(request):
    """
    Display the users dashboard
    """
    dashboard = get_object_or_404(UserDashboard, user=request.user)

    if request.method == 'POST':
        form = UserDashboardForm(request.POST, instance=dashboard)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Dashboard has been updated successfully')

    form = UserDashboardForm(instance=dashboard)
    purchase = dashboard.purchase.all()

    template = 'dashboard/dashboard.html'
    context = {
        'form': form,
        'purchase': purchase,
        'on_dashboard_page': True
    }

    return render(request, template, context)
