from django.contrib import admin

# Register your models here.
from store import models
admin.site.register(models.Product)