# -*- coding: utf8 -*-

import requests
from . import Mimo


class Contact(Mimo):
    """Communication with contacts resource."""

    def __init__(self):
        super().__init__()

    def list(self):
        """List all contacts registered in MIMO."""
        url = self._make_url('contact/list-all')
        res = requests.get(url)
        return self._mimo_response_object(res)

    def create(self, **payload):
        """Create one contact in MIMO."""
        url = self._make_url('contact/add')
        res = requests.post(url, json=payload)
        return self._mimo_response_object(res)

    def update(self, **payload):
        """Update one contact in MIMO."""
        url = self._make_url('contact/edit')
        res = requests.post(url, json=payload)
        return self._mimo_response_object(res)

    def view(self, phone_number: str):
        """Retrive one contact basead in phone number."""
        url = self._make_url('contact/list-one')
        res = requests.get(url, params={'phone': phone_number})
        return self._mimo_response_object(res)

    def delete(self, phones_numbers: list = None):
        """
        Delete all contacts or once list 
        of contacts basead in phones numbers.
        """
        if phones_numbers is None:
            url = self._make_url('contact/delete/all')
            res = requests.get(url)
            return self._mimo_response_object(res)
        else:
            url = self._make_url('contact/delete')
            phones = self._join(phones_numbers)
            res = requests.get(url, params={'phones': phones})
            return self._mimo_response_object(res)
