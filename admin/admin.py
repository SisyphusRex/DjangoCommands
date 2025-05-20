from django.contrib import admin

from .models import Flight, Airport, Passenger

class FlightAdmin(admin.ModelAdmin):
  list_display = ("id", "origin", "destination", "duration") # this allows you to see more attributes of objects

class PassengerAdmin(admin.ModelAdmin):
  filter_horizontal = ("flights",) # allows easier manipulation of many to many relationships


admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassngerAdmin)
