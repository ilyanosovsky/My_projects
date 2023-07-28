import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mini_project.settings')
import django
django.setup()

from rent.models import Customer
from faker import Faker

fake = Faker(locale=['en_US', 'it_IT', 'fr_FR'])

def create_customers(number:int):

    for _ in range(number):

        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone_number = fake.msisdn()
        address = fake.address()
        city = fake.city()
        country = fake.country()

        customer = Customer(first_name = first_name,
                            last_name = last_name,
                            email = email,
                            phone_number = phone_number, 
                            address = address,
                            city = city,
                            country = country)
        customer.save()

    print(f"CREATED {number} Customers")

create_customers(100)