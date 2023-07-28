from django.contrib import admin
from django.urls import path
from rent.views import (add_customer_view,
                        add_vehicle_view,
                        add_rental_view,
                        rental_list_view,
                        rental_detail_view,
                        customer_list_view,
                        customer_detail_view,
                        vehicle_list_view,
                        vehicle_detail_view,)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('rent/customer/add', add_customer_view),
    path('rent/vehicle/add', add_vehicle_view),
    path('rent/rental/add', add_rental_view),
    path('rent/rental/', rental_list_view),
    path('rent/rental/<int:rental_id>', rental_detail_view),
    path('rent/customer/', customer_list_view),
    path('rent/customer/<int:customer_id>', customer_detail_view),
    path('rent/vehicle/', vehicle_list_view),
    path('rent/vehicle/<int:vehicle_id>', vehicle_detail_view),
]
