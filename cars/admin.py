from django.contrib import admin

# Register your models here.
from .models import Car

# Register the pet table
admin.site.register(Car)