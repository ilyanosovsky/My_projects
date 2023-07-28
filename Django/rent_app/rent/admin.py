from django.contrib import admin
from .models import Customer, Vehicle, VehicleType, VehicleSize, Rental, RentalRate, RentalStation, Address
# Register your models here.

admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(VehicleType)
admin.site.register(VehicleSize)
admin.site.register(Rental)
admin.site.register(RentalRate)
admin.site.register(RentalStation)
admin.site.register(Address)

