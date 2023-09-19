from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from main.models import Item
from main.forms import ItemForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from main.models import Item

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()

        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def delete_item(request, item_id):
    # Get the item to be deleted or return a 404 error if it doesn't exist
    item = get_object_or_404(Item, pk=item_id)

    # Delete the item
    item.delete()

    # Redirect to a success page or wherever you'd like
    return redirect('main:show_main')

def show_main(request):
    items = Item.objects.all()

    if items:
        last_item = items.last()
    else:
        last_item = None

    context = {
        'name': 'Syazantri Salsabila',
        'class': 'PBP D',
        'items': items,
        'last_item': last_item,
    }

    return render(request, "main.html", context)

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
