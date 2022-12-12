from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from lists.models import Item

# Create your views here.


class HomeView(View):
    def get(self, request) -> HttpResponse:
        items = Item.objects.all()
        return render(request, "home.html", {"items": items})

    def post(self, request) -> HttpResponse:
        new_item = Item.objects.create(text=request["item_text"])
        new_item.save()

        return redirect("/")
