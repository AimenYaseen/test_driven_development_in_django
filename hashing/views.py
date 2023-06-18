from django.shortcuts import render
from .forms import HashForm


def home(request):
    """
    renders home template
    """
    form = HashForm()
    return render(request, 'hashing/home.html', context={'form': form})
