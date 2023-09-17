from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item

def show_main(request):
    items = Item.objects.all

    context = {
        'name': 'Henry Soedibjo',
        'class': 'PBP A',
        'items': items,
        'amount': '100',
        'description': 'henrysoed Investment Portofolio Inventory for individu task 2 PBP'
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
