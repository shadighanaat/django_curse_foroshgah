from django.shortcuts import render

import requests
import json

from django.shortcuts import get_object_or_404, redirect
from django.conf import settings
from django.http import HttpResponse

from orders.models import Order

def payment_process(request):
    # Get order id from session
    order_id = request.session.get('order_id')
    # Get the order object
    order = get_object_or_404(Order, id=order_id)

    toman_total_price = order.get_total_price()
    rial_total_price = toman_total_price * 10

    zarinpal_request_url = 'https://api.zarinpal.com/pg/v4/payment/request.json'

    request_header = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    request_data = {
        'merchant_id': settings.ZARINPAL_MERCHANT_ID,
        'amount': rial_total_price,
        'description': f'#{order.id}: {order.user.first_name} {order.user.last_name}',
        'callback_url': 'http://jetshop.com',
    }

    res = requests.post(url=zarinpal_request_url, data=json.dumps(request_data), headers=request_header)
    
    # Ensure that the response contains JSON and is a dictionary
    try:
        response_json = res.json()
        data = response_json.get('data', {})  # Using .get() to safely access 'data'
    except ValueError:
        return HttpResponse('Invalid response from Zarinpal')

    if isinstance(data, dict):  # Ensure that 'data' is a dictionary
        authority = data.get('authority')
        if authority:
            order.authority = authority
            order.save()
            return redirect(f'https://www.zarinpal.com/pg/StartPay/{authority}')
        else:
            return HttpResponse('Error: Authority key not found in Zarinpal response')
    else:
        return HttpResponse('Error: Unexpected data structure in Zarinpal response')

# def payment_process(request):
#     # Get order id from session
#     order_id = request.session.get('order_id')
#     # Get the order object
#     order = get_object_or_404(Order, id=order_id)

#     toman_total_price = order.get_total_price()
#     rial_total_price = toman_total_price * 10

#     zarinpal_request_url = 'https://api.zarinpal.com/pg/v4/payment/request.json'

#     request_header = {
#         "accept": "application/json",
#         "content-type": "application/json"
#     }

#     request_data = {
#         'merchant_id': settings.ZARINPAL_MERCHANT_ID,
#         'amount': rial_total_price,
#         'description': f'#{order.id}: {order.user.first_name} {order.user.last_name}',
#         'callback_url': 'http:/jetshoponline.com',
#     }

#     res = requests.post(url=zarinpal_request_url, data=json.dumps(request_data), headers=request_header)
#     response_data = res.json()
#     print(response_data) 
  
#     data = res.json()['data']
#     authority = data['authority']
#     order.authority = authority
#     order.save()

#     if 'errors' not in data or len(data['errors']) == 0:
#         return redirect('https://www.zarinpal.com/pg/StartPay/{authority}'.format(authority=authority))
#     else:
#         return HttpResponse('Error from zarinpal')