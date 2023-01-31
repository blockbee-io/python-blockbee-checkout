import BlockBeeCheckout

apikey = ''  # <- Insert your API Key here to run the tests

bb = BlockBeeCheckout.Helper(apikey, {
    'order_id': 1346
}, {})

"""
Request payment URL
"""
# request_payment = bb.payment_request('https://webhook.site/ab8a5cb9-46aa-41d4-909b-3d27117147b3', 1)
# print(request_payment)

"""
Request deposit URL
"""

# request_deposit = bb.deposit_request('https://webhook.site/ab8a5cb9-46aa-41d4-909b-3d27117147b3')
# print(request_deposit)
