import hashlib

from django.shortcuts import render, redirect

from .forms import HashForm
from .models import Hash


def home(request):
    """
    - handles post request to generate Hash object
    - renders home template with HashForm
    """
    if request.method == 'POST':
        filled_form = HashForm(request.POST)
        if filled_form.is_valid():
            text = filled_form.cleaned_data['text']
            hash_text = hashlib.sha256(text.encode('utf-8')).hexdigest()
            try:
                Hash.objects.get(hash=hash_text)
            except Hash.DoesNotExist:
                Hash.objects.create(text=text, hash=hash_text)

    form = HashForm()
    return render(request, 'hashing/home.html', context={'form': form})


def hashing(request, hash_text):
    """
    - get hash object using hash_text
    - renders hash template and pass the hash object
    """
    _hash = Hash.objects.get(hash=hash_text)
    return render(request, 'hashing/hash.html', context={'hash': _hash})
