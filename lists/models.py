from typing import Any

from django.db import models
from django.db.models import ForeignKey, TextField


class List(models.Model):
    text: TextField[str] = TextField(default="", null=True)


class Item(models.Model):
    text: TextField[str] = TextField(default="")
    list: ForeignKey[Any] = ForeignKey(List, default=None, on_delete=models.CASCADE)
