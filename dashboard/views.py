from django.shortcuts import render, get_object_or_404

from .models import UserDashboard
from .forms import UserDashboardForm


def dashboard(request):
    """
    Display the users dashboard
    """
    dashboard = get_object_or_404(UserDashboard, user=request.user)

    form = UserDashboardForm(instance=dashboard)
    purchase = dashboard.purchase.all()

    template = 'dashboard/dashboard.html'
    context = {
        'form': form,
        'purchase': purchase,
    }

    return render(request, template, context)
