from django.contrib import admin

from .models import District, Bus, Passenger

# Register your models here.
admin.site.register(District)
admin.site.register(Bus)
admin.site.register(Passenger)
