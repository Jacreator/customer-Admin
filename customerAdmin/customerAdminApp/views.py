from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .forms import OrderForm
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

    # this is used to hold all the data in a dictionary
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

    context = {'customers': customers,
               'orders': orders, 'order_count': order_count, }
    return render(request, 'customerAdminApp/customer.html', context)


def createOrder(request, user_id):
    OredeFormSet = inlineformset_factory(
        Customer, Order, fields=('product', 'status'), extra=10)
    customer = Customer.objects.get(id=user_id)
    formset = OredeFormSet(queryset=Order.objects.none(), instance=customer)
    if request.method == 'POST':
        formset = OredeFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset': formset}
    return render(request, 'customerAdminApp/orderForm.html', context)


def updateOrder(request, user_id):
    order = Order.objects.get(id=user_id)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'customerAdminApp/orderForm.html', context)


def deleteOrder(request, user_id):
    orders = Order.objects.get(id=user_id)
    if request.method == "POST":
        orders.delete()
        return redirect('/')
    context = {'item': orders}
    return render(request, 'customerAdminApp/delete.html', context)
