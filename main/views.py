import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from main.models import Item
from main.forms import ItemForm
from django.urls import reverse
from django.core import serializers
from django.contrib import messages       
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)

    if items:
        last_item = items.last()
    else:
        last_item = None

    context = {
        'name': request.user.username,
        'class': 'PBP D',
        'items': items,
        'last_item': last_item,
    }

    return render(request, "main.html", context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login_user'))
    return response

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login_user')
    context = {'form':form}
    return render(request, 'register.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    item.delete()

    return redirect('main:show_main')

def inc_amount(request, item_id):
    item = get_object_or_404(Item, pk=item_id, user=request.user)

    item.amount += 1
    item.save()

    return redirect('main:show_main')


def dec_amount(request, item_id):
    item = get_object_or_404(Item, pk=item_id, user=request.user)

    if item.amount > 1:
        item.amount -= 1
        item.save()
    else:
        delete_item(request, item_id)

    return redirect('main:show_main')


def show_html(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("html", data), content_type="application/html")

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

def get_item_json(request):
    item_item = Item.objects.all()
    return HttpResponse(serializers.serialize('json', item_item))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        price = request.POST.get("price")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, amount=amount, price=price, description=description, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            price = int(data["price"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)