from django.contrib import admin
from django.urls import path

from hashing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('hash/<str:hash_text>', views.hashing, name='hash'),
    path('quickhash', views.quickhash, name='quickhash'),
]
