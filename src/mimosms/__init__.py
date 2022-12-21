# -*- coding: utf8 -*-

import os
import requests


class Mimo:
    """
    Basic communication with the MIMO SMS service.
    """

    def __init__(self) -> None:
        try:
            self.__TOKEN = os.environ['MIMO_API_TOKEN']
            self.__HOST = os.environ['MIMO_API_HOST']
        except KeyError as error:
            raise error

    def charge_credits(self, voucher: str):
        """Charge accounts of user using voucher code."""
        url = self._make_url('credit/recharge')
        res = requests.get(url, params={'voucher': voucher})
        return self._mimo_response_object(res)

    def view_credits(self):
        """View the credit of user."""
        url = self._make_url('credit/')
        res = requests.get(url)
        return self._mimo_response_object(res)

    def transfer_credits(self, username: str, balance: int):
        """View the credit of user."""
        url = self._make_url('credit/transfer')
        res = requests.get(
            url, params={'username': username, 'balance': balance})
        return self._mimo_response_object(res)

    def logout(self):
        """Log out of session"""
        url = self._make_url('user/logout')
        res = requests.get(url)
        return self._mimo_response_object(res)

    def _get_hostname(self):
        return self.__HOST

    def _get_token(self):
        return self.__TOKEN

    def _make_url(self, endpoint: str):
        host = self._get_hostname()
        if host.endswith("/"):
            host.removesuffix("/")
        return f"{host}{endpoint}?token={self._get_token()}"

    def _join(self, elements):
        return ','.join(elements)

    def _mimo_response_object(self, response: requests.Response):
        status_code = response.status_code
        response_body = {'status': status_code}
        if 'sender' in response.json():
            json_response = response.json()
            data = {}
            data['id'] = json_response.get('id')
            data['sender'] = json_response.get('sender')
            data['text'] = json_response.get('text')
            response_body['data'] = data
        else:
            response_body |= response.json()
        return response_body
