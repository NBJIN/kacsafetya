from django.shortcuts import render


def dashboard(request):
    """
    Display the users dashboard
    """
    template = 'dashboard/dashboard.html'
    context = {}

    return render(request, template, context)
