from django.urls import path
from .views import item_form


urlpatterns = [
    path('', item_form, name='item_form'),
]