from django.conf import settings
from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product

from django.shortcuts import get_object_or_404

# Makes dict available to all apps
def bag_items(request):

    bag_items = []
    total = 0
    product_nu = 0
    grand_total = 0
    delivery = Decimal(settings.DELIVERY_COST)
    bag = request.session.get('bag', {})
    # user = request.session.get('user', {})

    for item_id, qty in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += qty * product.price
        # product_count += qty
        bag_items.append({
            'item_id': item_id,
            'qty': qty,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        grand_total = total + delivery
        free_delivery_delta = Decimal(settings.FREE_DELIVERY_THRESHOLD) - total
    else:
        delivery = 0
        free_delivery_delta = 0
        grand_total = total
        print("not enough")
        # insert code to let user know how much more to spend to get free deliv

    context = {
        'bag_items': bag_items,
        'total': total,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'product_nu': product_nu,
        'grand_total': grand_total,
        'free_delivery_threshold': Decimal(settings.FREE_DELIVERY_THRESHOLD),
    }

    return context
