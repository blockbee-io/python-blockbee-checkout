"""
BlockBee's Checkout Python Helper
"""

import requests
from requests.models import PreparedRequest


class Helper:
    BLOCKBEE_URL = 'https://api.blockbee.io/'
    BLOCKBEE_HOST = 'api.blockbee.io'

    def __init__(self, api_key, parameters, bb_params):
        if parameters is None:
            parameters = {}

        if bb_params is None:
            bb_params = {}

        if api_key is None:
            raise Exception("API Key Missing")

        self.parameters = parameters
        self.bb_params = bb_params
        self.api_key = api_key

    def payment_request(self, redirect_url, value):
        if redirect_url is None or value is None:
            return None

        if self.parameters:
            req = PreparedRequest()
            req.prepare_url(redirect_url, self.parameters)
            redirect_url = req.url

        params = {
            'redirect_url': redirect_url,
            'apikey': self.api_key,
            'value': value,
            **self.bb_params}

        _request = Helper.process_request('', endpoint='checkout/request', params=params)
        if _request['status'] == 'success':
            return {
                'success_token': _request['success_token'],
                'payment_url': _request['payment_url']
            }
        return None

    def deposit_request(self, notify_url):
        if notify_url is None:
            return None

        if self.parameters:
            req = PreparedRequest()
            req.prepare_url(notify_url, self.parameters)
            notify_url = req.url

        params = {
            'notify_url': notify_url,
            'apikey': self.api_key,
            **self.bb_params}

        _request = Helper.process_request('', endpoint='deposit/request', params=params)
        if _request['status'] == 'success':
            return {
                'payment_url': _request['payment_url']
            }

        return None

    @staticmethod
    def process_request(coin='', endpoint='', params=None):
        if coin != '':
            coin += '/'

        response = requests.get(
            url="{base_url}{coin}{endpoint}/".format(
                base_url=Helper.BLOCKBEE_URL,
                coin=coin.replace('_', '/'),
                endpoint=endpoint,
            ),
            params=params,
            headers={'Host': Helper.BLOCKBEE_HOST},
        )

        return response.json()
