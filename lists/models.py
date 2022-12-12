from django.db import models
from django.db.models import TextField


class Item(models.Model):
    text: TextField[str, str] = TextField(default="")
