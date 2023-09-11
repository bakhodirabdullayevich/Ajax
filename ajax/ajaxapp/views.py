from django.shortcuts import render
from django.http import JsonResponse
from .models import Category, Item
from .forms import ItemForm


def item_form(request):
    form = ItemForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

    return render(request, 'index.html', {'form': form})


def get_items_by_category(request):
    category_id = request.GET.get('category_id')
    items = Item.objects.filter(category_id=category_id)
    item_list = [{'id': item.id, 'name': item.name} for item in items]
    return JsonResponse({'items': item_list})
