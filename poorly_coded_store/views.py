from django.shortcuts import render
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(request.POST["price"])
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    orders_temp = Order.objects.all()
    all_orders = 0
    for orders in orders_temp:
        all_orders += 1
    orders_sum = 0
    for orders in orders_temp:
        orders_sum += orders.total_price 
    context = {
        "orderinfo" : total_charge,
        "ordercount" : all_orders, 
        "ordertotal" : orders_sum,
    }
    return render(request, "store/checkout.html", context)