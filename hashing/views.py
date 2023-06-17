from django.shortcuts import render


def home(request):
    """
    renders home template
    """
    return render(request, 'hashing/home.html')
