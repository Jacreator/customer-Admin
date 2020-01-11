from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_ordering = orders.count()
    total_customers = customers.count()
    pending = orders.filter(status='Pending').count()
    delivered = orders.filter(status='Delivered').count()
    out = orders.filter(status='Out for Delivery').count()


    #this is used to hold all the data in a dictionary
    context = {
        'orders': orders, 'customers': customers,
        'orders_ordering': total_ordering, 'total_customers': total_customers,
        'pending': pending, 'delivered': delivered, 'out': out,
        }
    return render(request, 'customerAdminApp/dashboard.html', context)

def product(request):
    products = Product.objects.all()
    return render(request, 'customerAdminApp/products.html', {'products': products})

def customer(request, user_pk):
    customers = Customer.objects.get(id=user_pk)
    orders = customers.order_set.all()
    order_count = orders.count()
    context = {'customers': customers, 'orders': orders, 'order_count': order_count}
    return render(request, 'customerAdminApp/customer.html', context)