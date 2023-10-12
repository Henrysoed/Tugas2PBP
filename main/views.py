from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, HttpResponseNotFound
from main.forms import ItemForm
from django.urls import reverse
from django.core import serializers
from main.models import Item
from django.db.models import Sum
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import datetime

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    temp = sum([x.amount for x in items])
    if(len(items) == 0):
        temp = 0

    context = {
        'name': request.user.username,
        'class': 'PBP A', # Kelas PBP kamu
        'banyak_jenis' : len(items),
        'banyak_item' : temp,
        'items': items,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
    
        # Mengeluarkan pesan sukses menyimpan item
        item_name = form.cleaned_data['name']
        item_amount = form.cleaned_data['amount']
        messages.success(request, f"Kamu berhasil menyimpan {item_name} sebanyak {item_amount}.")
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def add(request, id):
    a = Item.objects.get(pk=id)
    a.amount += 1
    a.save()
    return redirect('main:show_main')

def remove(request, id):
    data = Item.objects.get(pk=id)
    if(data.amount>0):
        data.amount -= 1
        data.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    data.save()
    return HttpResponseRedirect(reverse('main:show_main'))

# def remove_all(request, id):
#     a = Item.objects.get(pk=id)
#     a.delete()
#     return redirect('main:show_main')

def get_item_json(request):
    item_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', item_item))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, price=price, amount=amount, description=description, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def delete_item_ajax(request, id):
    if request.method == 'DELETE':
        a = Item.objects.get(pk=id)
        a.delete()
        return HttpResponse(b"DELETE", status=201)
    return HttpResponseNotFound()
