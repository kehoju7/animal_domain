from django.contrib import admin

from .models import Animal, Description


admin.site.register(Animal)
admin.site.register(Description)