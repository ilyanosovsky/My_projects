from django.shortcuts import render
from .forms import CustomerForm, VehicleForm, RentalForm
from .models import Customer, Vehicle, Rental

# add a customer
def add_customer_view(request):
    # POST
    if request.method == 'POST':
        form_filled = CustomerForm(request.POST)
        if form_filled.is_valid():
            form_filled.save()
        else:
            print(form_filled.errors)
            
    # GET
    customer_form = CustomerForm()
    context = {'form': customer_form}
    return render(request, 'add_customer.html', context)

# add a vehicle to the database
def add_vehicle_view(request):
    # POST
    if request.method == 'POST':
        form_filled = VehicleForm(request.POST)
        if form_filled.is_valid():
            form_filled.save()
        else:
            print(form_filled.errors)
            
    # GET
    vehicle_form = VehicleForm()
    context = {'form': vehicle_form}
    return render(request, 'add_vehicle.html', context)

# add a rental
def add_rental_view(request):
    # POST
    if request.method == 'POST':
        form_filled = RentalForm(request.POST)
        if form_filled.is_valid():
            form_filled.save()
        else:
            print(form_filled.errors)
            
    # GET
    rental_form = RentalForm()
    context = {'form': rental_form}
    return render(request, 'add_rental.html', context)

# show all rentals, in order of return date
def rental_list_view(request):
    rentals = Rental.objects.order_by('return_date')
    context = {'rentals': rentals}
    return render(request, 'rental.html', context)

# show all information about a rental (customer details, vehicle details, rental details)
def rental_detail_view(request, rental_id):
    rental = Rental.objects.get(id=rental_id)
    customer = Customer.objects.get(id=rental.customer.id)
    vehicle = Vehicle.objects.get(id=rental.vehicle.id)
    context = {'rental': rental, 'customer': customer, 'vehicle': vehicle}
    return render(request, 'rental_detail.html', context)

# show all customers, in alphabetical order
def customer_list_view(request):
    customers = Customer.objects.order_by('last_name')
    context = {'customers': customers}
    return render(request, 'customer_list.html', context)

# show all information about a customer
def customer_detail_view(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    rentals = Rental.objects.filter(customer=customer_id)
    context = {'customer': customer, 'rentals': rentals}
    return render(request, 'customer_detail.html', context)

# show all vehicles, in alphabetical order
def vehicle_list_view(request):
    vehicles = Vehicle.objects.order_by('vehicle_type')
    context = {'vehicles': vehicles}
    return render(request, 'vehicle_list.html', context)

# show all information about a vehicle
def vehicle_detail_view(request, vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id)
    rentals = Rental.objects.filter(vehicle=vehicle_id)
    context = {'vehicle': vehicle, 'rentals': rentals}
    return render(request, 'vehicle_detail.html', context)
    