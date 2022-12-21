# -*- coding: utf8 -*-

import requests
from . import Mimo


class Sender(Mimo):
    """Communication with sender resource."""

    def __init__(self):
        super().__init__()

    def list(self, requested: bool = False, /):
        """List all senders registred in MIMO."""
        if requested is False:
            url = self._make_url('sender-id/list-all')
        else:
            url = self._make_url('sender-id/list-all/requested')
        res = requests.get(url)
        return self._mimo_response_object(res)

    def create(self, **payload):
        """Create a new sender."""
        url = self._make_url('sender-id/request')
        res = requests.post(url, json=payload)
        return self._mimo_response_object(res)

    def view(self, sender_name: str, make_default: bool = False, /):
        """Retrive all information about sender."""
        if make_default is True:
            url = self._make_url('sender-id/default')
            res = requests.get(url, params={'sender': sender_name})
        else:
            url = self._make_url('sender-id/list-one')
            res = requests.get(url, params={'sender': sender_name})
        return self._mimo_response_object(res)

    def delete(self, senders_ids: list = None):
        """Delete an sender."""
        url = self._make_url('sender-id/delete')
        senders = self._join(senders_ids)
        res = requests.get(url, params={'senders': senders})
        return self._mimo_response_object(res)
