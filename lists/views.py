from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views import View

from lists.models import Item


class HomeView(View):
    def get(self, request) -> HttpResponse:
        items = Item.objects.all()
        return render(request, "home.html", {"items": items})


class ListView(View):
    def get(self, request) -> HttpResponse:
        items = Item.objects.all()
        return render(request, "list.html", {"items": items})


class NewListView(View):
    def get(self, request) -> HttpResponseRedirect:
        Item.objects.create(text=request.POST["item_text"])
        return redirect("/lists/the-only-list-in-the-world")
