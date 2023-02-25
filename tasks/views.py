from django.shortcuts import render, redirect 
from django.utils.html import escape
from django.http import HttpResponse

from tasks.models import Collection


# Create your views here.
# def index(request):
#     context = {}
#     context["collections"] = Collection.objects.order_by("name")
#     return render(request, 'tasks/index.html', context={})
def index(request):
    context = {}

    collection = Collection.get_default_collection()
    collection.name
    context["collections"] = Collection.objects.order_by("slug")
    return render(request, 'tasks/index.html', context)


def add_collection(request):
    collection_name = escape(request.POST.get("collection-name"))
    collection, create = Collection.objects.get_or_create(name=collection_name)
    print(collection_name)
    if not create:
        return HttpResponse("la collection existe deja.",status=409)
    print("test")
    return HttpResponse(f'<h2>{collection_name}</h2>')
