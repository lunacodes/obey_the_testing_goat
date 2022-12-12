from django.http import (
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
from django.shortcuts import redirect, render
from django.views import View

from lists.models import Item, List


class HomeView(View):
    def get(self, request) -> HttpResponse:
        items = Item.objects.all()
        return render(request, "home.html", {"items": items})


class ListView(View):
    def get(self, request) -> HttpResponse:
        list_ = List.objects.get(id=list_id)
        return render(request, "list.html", {"list": list_})


class NewListView(View):
    # def get(self, request) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
    #     return redirect(f'/lists/{list_.id}/')

    def post(self, request) -> HttpResponseRedirect | HttpResponsePermanentRedirect:
        list_ = List.objects.create()
        Item.objects.create(text=request.POST["item_text"], list=list_)
        return redirect(f"/lists/{list_.id}/")


class AddItemView(View):
    # def __init__(self, request, list_id):
    #     pass

    def post(self, request, list_id):
        list_ = List.objects.get(id=list_id)
        Item.objects.create(text=request.POST["item_text"], list=list_)
        return redirect(f"/lists/{list_.id}/")
