from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey("VehicleType", on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    real_cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.ForeignKey("VehicleSize", on_delete=models.CASCADE) 

    def __str__(self):
        return f"{self.vehicle_type} {self.real_cost} {self.size}"
    

class VehicleType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class VehicleSize(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
    

class Rental(models.Model):
    rental_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(auto_now_add=True)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    vehicle = models.ForeignKey("Vehicle", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.rental_date} {self.return_date} {self.customer} {self.vehicle}"
    

class RentalRate(models.Model):
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
    vehicle_type = models.ForeignKey("VehicleType", on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey("VehicleSize", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.daily_rate} {self.vehicle_type} {self.vehicle_size}"


class RentalStation(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    address = models.ForeignKey("Address", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.capacity} {self.address}"
    

class Address(models.Model):
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.address} {self.address2} {self.city} {self.country} {self.postal_code}"