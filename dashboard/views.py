from django.shortcuts import render, get_object_or_404

from .models import UserDashboard


def dashboard(request):
    """
    Display the users dashboard
    """
    dashboard = get_object_or_404(UserDashboard, user=request.user)
    template = 'dashboard/dashboard.html'
    context = {
        'dashboard': dashboard,
    }

    return render(request, template, context)
