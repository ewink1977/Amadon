from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    product_data = Product.objects.get(id=request.POST["id"])
    price_data = float(product_data.price)
    total_charge = quantity_from_form * price_data
    print(f"Charging credit card ${ total_charge }")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect("thanks")

def thanks(request):
    total_charge = Order.objects.last()
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
    return render(request, 'store/checkout.html', context)
