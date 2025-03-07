from django.shortcuts import render

def administrador(request):
    return render(request, 'base.html')


# Compare this snippet from reming/urls.py: